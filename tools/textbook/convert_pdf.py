#!/usr/bin/env python3
"""Convert an IGCSE textbook PDF chapter to GitHub-flavoured Markdown.

Usage:
    python tools/textbook/convert_pdf.py <input.pdf> <output.md>

Images are saved to <output_dir>/images/<stem>/ and referenced with
relative paths in the markdown.
"""
import re
import shutil
import sys
import tempfile
from pathlib import Path

import fitz
import pymupdf4llm


# Lines to discard: section banners, chapter number lines, TOC lines
SKIP_LINE_RE = re.compile(
    r"^#{1,3}\s+\*{0,2}(?:"
    r"SECTION \d+"
    r"|Algorithms,\s*programming\s*and\s*logic"
    r"|Chapters?"
    r"|programming"
    r"|logic"
    r")\*{0,2}\s*$",
    re.IGNORECASE,
)
CHAPTER_NUM_RE = re.compile(r"^#{1,3}\s+\*{0,2}\d{1,2}\*{0,2}\s*$")
# Duplicate chapter title line (no section number)
CHAPTER_TITLE_DUP_RE = re.compile(r"^#{1,3}\s+\*{0,2}Algorithm design and problem solving\*{0,2}\s*$", re.IGNORECASE)
PAGE_NUM_RE = re.compile(r"^\d{2,4}\s*$")
RUNNING_HEADER_RE = re.compile(r"^_[^_]+_\s*$")
PICTURE_TEXT_RE = re.compile(
    r"\*{0,2}-{5} Start of picture text -{5}\*{0,2}.*?\*{0,2}-{5} End of picture text -{5}\*{0,2}<br>\n?",
    re.DOTALL,
)
IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
TOC_ITEM_RE = re.compile(r"^-\s+\d+\s+\w")  # e.g. "- 7 Algorithm design..."


def heading_text(line: str) -> str:
    return re.sub(r"^#{1,6}\s+\*{0,2}", "", line).rstrip("* ").strip()


def is_section_heading(text: str) -> bool:
    return bool(re.match(r"^\d+\.\d+\s+\S", text))


def is_subsection_heading(text: str) -> bool:
    return bool(re.match(r"^\d+\.\d+\.\d+\s+\S", text))


def remap_images_in_line(line: str, name_map: dict[str, str], img_rel: str) -> str | None:
    """Return remapped line, or None if the line contains an unmapped (skipped) image."""
    def replace(m: re.Match) -> str:
        alt = m.group(1)
        src = m.group(2)
        basename = Path(src).name
        new_name = name_map.get(basename)
        if new_name:
            return f"![{alt}]({img_rel}/{new_name})"
        return ""  # empty = marker for removal

    result = IMG_RE.sub(replace, line)
    # If we wiped out an image ref and nothing meaningful remains, signal removal
    if "![" not in result and IMG_RE.search(line):
        stripped = result.strip()
        if not stripped or stripped in ("", "▲"):
            return None
    return result


def postprocess(md: str, name_map: dict[str, str], img_rel: str) -> str:
    # Remove OCR'd picture text blocks
    md = PICTURE_TEXT_RE.sub("", md)

    lines = md.split("\n")
    out: list[str] = []
    in_toc = False
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip bare page numbers
        if PAGE_NUM_RE.match(stripped):
            i += 1
            continue

        # Skip running headers (_Section name_)
        if RUNNING_HEADER_RE.match(stripped):
            i += 1
            continue

        # Skip chapter number lines (## **7**)
        if CHAPTER_NUM_RE.match(stripped):
            i += 1
            continue

        # Skip decorative banner lines
        if SKIP_LINE_RE.match(stripped):
            i += 1
            continue

        # Skip duplicate chapter title heading
        if CHAPTER_TITLE_DUP_RE.match(stripped):
            i += 1
            continue

        # Skip TOC-style list items (- 7 Algorithm..., - 8 Programming...)
        if TOC_ITEM_RE.match(stripped):
            i += 1
            continue

        # Fix heading levels
        m = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if m:
            rest = m.group(2)
            text = re.sub(r"^\*{1,2}|(\*{1,2})$", "", rest).strip()

            if text.startswith("Find out more"):
                # Collect sidebar content as blockquote, stop at next real heading
                i += 1
                content_parts: list[str] = []
                while i < len(lines):
                    ns = lines[i].strip()
                    if ns.startswith("#"):
                        break
                    if ns:
                        remapped = remap_images_in_line(ns, name_map, img_rel)
                        if remapped is not None:
                            content_parts.append(remapped)
                    i += 1
                body = " ".join(content_parts)
                out.append(f"> **Find out more:** {body}")
                out.append("")
                continue
            elif is_subsection_heading(text):
                line = f"### {text}"
            elif is_section_heading(text):
                line = f"## {text}"
            # else keep heading as-is

        # Remap image paths (or remove broken refs)
        if "![" in line:
            remapped = remap_images_in_line(line, name_map, img_rel)
            if remapped is None:
                i += 1
                continue
            line = remapped

        out.append(line)
        i += 1

    return "\n".join(out)


def detect_chapter_info(doc: fitz.Document) -> tuple[str, str]:
    """Return (chapter_num, chapter_title) by scanning the first few pages."""
    chapter_num = ""
    title_parts: list[str] = []
    title_size = 0.0

    for page_idx in range(min(3, len(doc))):
        page = doc[page_idx]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b["type"] != 0:
                continue
            for line_blk in b["lines"]:
                for span in line_blk["spans"]:
                    txt = span["text"].strip()
                    if not txt:
                        continue
                    # Chapter number at very large size (≥40pt)
                    if span["size"] >= 40 and re.match(r"^\d+$", txt):
                        chapter_num = txt
                    # Chapter title at ~24-32pt
                    if 23 <= span["size"] <= 32 and len(txt) > 4 and not txt.isdigit():
                        if abs(span["size"] - title_size) < 1 or not title_parts:
                            title_parts.append(txt)
                            title_size = span["size"]

    chapter_title = " ".join(title_parts) if title_parts else "Unknown Chapter"

    # Fallback for chapter number
    if not chapter_num:
        for page in doc:
            for b in page.get_text("dict")["blocks"]:
                if b["type"] != 0:
                    continue
                for line_blk in b["lines"]:
                    for span in line_blk["spans"]:
                        txt = span["text"].strip()
                        m = re.match(r"^(\d+)\.\d+\s", txt)
                        if m:
                            chapter_num = m.group(1)
                            break
                if chapter_num:
                    break
            if chapter_num:
                break

    return chapter_num or "?", chapter_title


def convert(pdf_path: Path, md_path: Path) -> None:
    stem = pdf_path.stem.lower().replace(" ", "_")
    img_dir = md_path.parent / "images" / stem
    img_dir.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    chapter_num, chapter_title = detect_chapter_info(doc)

    with tempfile.TemporaryDirectory() as tmpdir:
        raw_md = pymupdf4llm.to_markdown(
            doc,
            write_images=True,
            image_path=tmpdir,
            image_format="png",
        )

        # Build mapping: original_filename → img_NNN.png, skip tiny decorative icons
        tmp_imgs = sorted(Path(tmpdir).glob("*.png"))
        name_map: dict[str, str] = {}
        idx = 1
        for img in tmp_imgs:
            if img.stat().st_size < 3000:
                continue  # decorative icon
            new_name = f"img_{idx:03d}.png"
            shutil.copy2(img, img_dir / new_name)
            name_map[img.name] = new_name
            idx += 1

    img_rel = f"images/{stem}"
    body = postprocess(raw_md, name_map, img_rel)

    header = (
        f"# CAIE Computer Science IGCSE — Chapter {chapter_num}: {chapter_title}\n\n"
        "---\n\n"
    )
    md_path.write_text(header + body, encoding="utf-8")

    kept = len(name_map)
    skipped = len(tmp_imgs) - kept
    print(f"Written: {md_path}")
    print(f"Images:  {img_dir} ({kept} content images, {skipped} decorative skipped)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.pdf> <output.md>")
        sys.exit(1)
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
