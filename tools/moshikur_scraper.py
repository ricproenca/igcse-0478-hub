"""
moshikur_scraper.py

Scrapes IGCSE CS revision content from moshikur.com sub-topic pages.
For each URL in moshikur_urls.py, extracts text, tables, and images,
and saves clean markdown to study/moshikur/<topic_dir>/<subtopic>.md.

Usage:
    pip install -r tools/requirements_scraper.txt
    python3 tools/moshikur_scraper.py
"""

import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

# Add project root to path so we can import moshikur_urls from tools/
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "tools"))

from moshikur_urls import URLS, SYLLABUS, TOPIC_DIRS  # noqa: E402

OUTPUT_DIR = PROJECT_ROOT / "study" / "moshikur"
IMAGES_DIR = OUTPUT_DIR / "images"
AUDIT_DIR = OUTPUT_DIR / "audit"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Seconds to wait between page requests (be polite to the server)
REQUEST_DELAY = 1.5

# HTML elements to strip before converting to markdown
STRIP_TAGS = ["nav", "header", "footer", "aside", "script", "style",
              "noscript", ".widget", ".sidebar", "#sidebar",
              ".comment-section", "#comments", ".cookie-notice"]

# Content selectors tried in order
CONTENT_SELECTORS = ["main", "article", ".entry-content", ".post-content",
                     ".content", "#content", "body"]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(code: str, title: str) -> str:
    """Turn '1.1' + 'Number Systems' into '1_1_number_systems'."""
    slug = code.replace(".", "_") + "_" + title.lower()
    slug = re.sub(r"[^a-z0-9_]+", "_", slug)
    return slug.strip("_")


def topic_key(code: str) -> str:
    """Return the topic number prefix: '1.1' → '1', '10.2' → '10'."""
    return code.split(".")[0]


def get_topic_dir(code: str) -> Path:
    key = topic_key(code)
    folder = TOPIC_DIRS.get(key, f"topic{key}")
    return OUTPUT_DIR / folder


def get_images_dir(code: str) -> Path:
    key = topic_key(code)
    folder = TOPIC_DIRS.get(key, f"topic{key}")
    return IMAGES_DIR / folder


def find_content(soup: BeautifulSoup) -> BeautifulSoup:
    """Return the best content container found in the page."""
    # Strip noisy elements first
    for selector in STRIP_TAGS:
        for el in soup.select(selector):
            el.decompose()

    for selector in CONTENT_SELECTORS:
        el = soup.select_one(selector)
        if el:
            return el
    return soup.body or soup


def download_image(src: str, base_url: str, dest_dir: Path, index: int) -> str | None:
    """Download an image and return the relative path from the markdown file."""
    url = urljoin(base_url, src)
    parsed = urlparse(url)
    ext = Path(parsed.path).suffix or ".jpg"
    filename = f"img_{index:03d}{ext}"
    dest_path = dest_dir / filename

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path.write_bytes(resp.content)
        # Return path relative to OUTPUT_DIR so markdown links work from there
        return str(dest_path.relative_to(OUTPUT_DIR))
    except Exception as exc:
        print(f"    [WARN] Failed to download image {url}: {exc}")
        return None


def html_table_to_markdown(table) -> str:
    """Convert a BeautifulSoup <table> to a markdown pipe table."""
    rows = []
    for tr in table.find_all("tr"):
        cells = []
        for cell in tr.find_all(["th", "td"]):
            text = cell.get_text(separator=" ", strip=True)
            text = text.replace("|", "\\|").replace("\n", " ")
            cells.append(text)
        rows.append("| " + " | ".join(cells) + " |")

    if not rows:
        return ""

    # Insert separator after first row (header)
    header = rows[0]
    col_count = header.count("|") - 1
    separator = "| " + " | ".join(["---"] * col_count) + " |"
    lines = [rows[0], separator] + rows[1:]
    return "\n".join(lines)


def scrape_page(code: str, url: str) -> tuple[str, list[str]]:
    """
    Fetch a page and return (markdown_content, list_of_downloaded_image_paths).
    """
    print(f"  Fetching {url}")
    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    content = find_content(soup)
    img_dir = get_images_dir(code)

    # Replace <table> elements with markdown equivalents before markdownify
    # (markdownify's table support can be inconsistent)
    for i, table in enumerate(content.find_all("table")):
        md_table = html_table_to_markdown(table)
        table.replace_with(BeautifulSoup(f"\n\n{md_table}\n\n", "html.parser"))

    # Download images and rewrite src attributes
    downloaded = []
    for i, img in enumerate(content.find_all("img")):
        src = img.get("src") or img.get("data-src") or ""
        if not src:
            continue
        local_path = download_image(src, url, img_dir, i + 1)
        if local_path:
            img["src"] = local_path
            downloaded.append(local_path)
        else:
            img.decompose()

    # Convert HTML → markdown
    markdown = md(str(content), heading_style="ATX", bullets="-")

    # Clean up excessive blank lines
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

    return markdown, downloaded


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not URLS:
        print("No URLs configured in tools/moshikur_urls.py. Add URLs and re-run.")
        sys.exit(1)

    results = {}  # code → {"status": ..., "file": ..., "images": ...}

    for code, url in sorted(URLS.items()):
        title = SYLLABUS.get(code, f"Sub-topic {code}")
        slug = slugify(code, title)
        topic_dir = get_topic_dir(code)
        output_file = topic_dir / f"{slug}.md"

        print(f"\n[{code}] {title}")

        try:
            markdown, images = scrape_page(code, url)
            topic_dir.mkdir(parents=True, exist_ok=True)

            # Add a heading at the top of the file
            header = f"# {code} {title}\n\n> Source: {url}\n\n"
            output_file.write_text(header + markdown, encoding="utf-8")

            rel_path = str(output_file.relative_to(OUTPUT_DIR))
            print(f"  ✅ Saved → {rel_path} ({len(images)} image(s))")
            results[code] = {"status": "scraped", "file": rel_path, "images": images}

        except Exception as exc:
            print(f"  ❌ Error: {exc}")
            results[code] = {"status": "error", "file": None, "error": str(exc)}

        time.sleep(REQUEST_DELAY)

    write_audit(results)
    print("\nDone.")


def write_audit(results: dict):
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    audit_file = AUDIT_DIR / "coverage_audit.md"

    lines = [
        "# Moshikur Coverage Audit — IGCSE 0478",
        "",
        "| Sub-topic | Title | Output File | Images | Status |",
        "|-----------|-------|-------------|--------|--------|",
    ]

    scraped = 0
    for code, title in SYLLABUS.items():
        if code in results:
            r = results[code]
            if r["status"] == "scraped":
                img_count = len(r.get("images", []))
                lines.append(
                    f"| {code} | {title} | `{r['file']}` | {img_count} | ✅ Scraped |"
                )
                scraped += 1
            else:
                lines.append(
                    f"| {code} | {title} | — | — | ❌ Error: {r.get('error', '')} |"
                )
        else:
            lines.append(f"| {code} | {title} | — | — | ⬜ No URL provided |")

    total = len(SYLLABUS)
    lines += [
        "",
        f"**Coverage: {scraped}/{total} sub-topics scraped**",
    ]

    audit_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nAudit written → {audit_file.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
