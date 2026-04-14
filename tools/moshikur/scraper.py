"""
scraper.py

Scrapes IGCSE CS revision content from moshikur.com.
Reads URL list from tools/moshikur/urls.py, fetches each page,
extracts text/tables/images and saves as clean markdown.

Usage:
    pip install -r tools/moshikur/requirements.txt
    python3 tools/moshikur/scraper.py

Output: docs/moshikur/<topic_folder>/<slug>.md
        docs/moshikur/images/<topic_folder>/<slug>/img_NNN.ext
        docs/moshikur/audit/coverage_audit.md
"""

import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

# tools/moshikur/scraper.py → parent = tools/moshikur → parent = tools → parent = project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(Path(__file__).parent))

from urls import URLS, SYLLABUS, TOPIC_DIRS, CHAPTER_SYLLABUS_MAP  # noqa: E402

OUTPUT_DIR = PROJECT_ROOT / "docs" / "moshikur"
AUDIT_DIR  = OUTPUT_DIR / "audit"

# ---------------------------------------------------------------------------
# HTTP config
# ---------------------------------------------------------------------------

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}
REQUEST_DELAY = 1.5   # seconds between requests

# ---------------------------------------------------------------------------
# HTML cleanup selectors
# ---------------------------------------------------------------------------

STRIP_SELECTORS = [
    "nav", "header", "footer", "aside", "script", "style", "noscript",
    ".widget", ".sidebar", "#sidebar", ".wp-block-navigation",
    ".comment-section", "#comments", ".cookie-notice", ".site-header",
    ".site-footer", ".breadcrumb", ".breadcrumbs", ".sharedaddy",
    ".post-navigation", ".nav-links", "[class*='related']",
    "[class*='advertisement']", "[class*='social']",
]

CONTENT_SELECTORS = [
    "main", "article", ".entry-content", ".post-content",
    ".content", "#content", ".page-content",
]

# ---------------------------------------------------------------------------
# Folder routing: derive output folder from URL
# ---------------------------------------------------------------------------

def folder_from_url(url: str) -> str:
    """
    Infer which topic folder to use based on the URL path.
    - /igcse-o-level-cs/ch-01-... or /chapter-1-... → TOPIC_DIRS["1"]
    - /pseudocode/...                                → pseudocode
    - anything else                                  → misc
    """
    path = urlparse(url).path.lower()

    m = re.search(r'ch-0*(\d+)|chapter-0*(\d+)', path)
    if m:
        n = str(int(m.group(1) or m.group(2)))
        return TOPIC_DIRS.get(n, f"topic{n}")

    if "/pseudocode" in path:
        return "pseudocode"

    return "misc"


# ---------------------------------------------------------------------------
# Filename slug: derive from descriptive key
# ---------------------------------------------------------------------------

def slugify(key: str) -> str:
    """
    'CH 01 Data Representation'  → 'ch_01_data_representation'
    '3.2.1 INPUT Devices'        → '3_2_1_input_devices'
    '7 PSEUDOCODE ARRAY'         → '7_pseudocode_array'
    """
    s = key.lower()
    s = s.replace(".", "_").replace("/", "_").replace("&", "and")
    s = re.sub(r"[^a-z0-9_]+", "_", s)
    return s.strip("_")


# ---------------------------------------------------------------------------
# Syllabus code extraction
# ---------------------------------------------------------------------------

def extract_syllabus_code(key: str, url: str = ""):
    """
    '1.1 Number System'   → '1.1'   (from an igcse-o-level-cs URL)
    '3.2.1 INPUT Devices' → None    (sub-sub-topic, not in SYLLABUS)
    'CH 01 Data ...'      → None    (chapter overview)
    'PSEUDOCODE'          → None
    Pseudocode pages use their own numbering — not mapped to 0478 codes.
    """
    if "/pseudocode" in url:
        return None
    m = re.match(r'^(\d+\.\d+)(?!\.\d)', key)
    if m:
        code = m.group(1)
        return code if code in SYLLABUS else None
    return None


# ---------------------------------------------------------------------------
# HTML → Markdown conversion helpers
# ---------------------------------------------------------------------------

def find_content(soup: BeautifulSoup) -> BeautifulSoup:
    for selector in STRIP_SELECTORS:
        for el in soup.select(selector):
            el.decompose()
    for selector in CONTENT_SELECTORS:
        el = soup.select_one(selector)
        if el:
            return el
    return soup.body or soup


def html_table_to_markdown(table) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = []
        for cell in tr.find_all(["th", "td"]):
            text = cell.get_text(separator=" ", strip=True)
            text = text.replace("|", "\\|").replace("\n", " ")
            cells.append(text)
        if cells:
            rows.append("| " + " | ".join(cells) + " |")

    if not rows:
        return ""

    col_count = rows[0].count("|") - 1
    separator = "| " + " | ".join(["---"] * col_count) + " |"
    return "\n".join([rows[0], separator] + rows[1:])


def download_image(src: str, base_url: str, dest_dir: Path, index: int):
    url = urljoin(base_url, src)
    ext = Path(urlparse(url).path).suffix or ".jpg"
    filename = f"img_{index:03d}{ext}"
    dest_path = dest_dir / filename
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path.write_bytes(resp.content)
        return str(dest_path.relative_to(OUTPUT_DIR))
    except Exception as exc:
        print(f"    [WARN] image skip ({exc})")
        return None


# ---------------------------------------------------------------------------
# Core scrape
# ---------------------------------------------------------------------------

def scrape_page(key: str, url: str):
    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    content = find_content(soup)

    slug = slugify(key)
    folder = folder_from_url(url)
    img_dir = OUTPUT_DIR / "images" / folder / slug

    for table in content.find_all("table"):
        md_table = html_table_to_markdown(table)
        table.replace_with(BeautifulSoup(f"\n\n{md_table}\n\n", "html.parser"))

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

    markdown = md(str(content), heading_style="ATX", bullets="-")
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

    return markdown, downloaded


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not URLS:
        print("No URLs in tools/moshikur/urls.py. Add URLs and re-run.")
        sys.exit(1)

    results = {}

    for key, url in URLS.items():
        slug = slugify(key)
        folder = folder_from_url(url)
        syllabus_code = extract_syllabus_code(key, url)
        topic_dir = OUTPUT_DIR / folder
        output_file = topic_dir / f"{slug}.md"

        print(f"\n[{key}]")
        print(f"  → {url}")

        try:
            markdown, images = scrape_page(key, url)
            topic_dir.mkdir(parents=True, exist_ok=True)

            header = f"# {key}\n\n> Source: {url}\n\n"
            output_file.write_text(header + markdown, encoding="utf-8")

            rel_path = str(output_file.relative_to(OUTPUT_DIR))
            print(f"  ✅ {rel_path}  ({len(images)} image(s))")

            results[key] = {
                "status": "scraped",
                "folder": folder,
                "file": rel_path,
                "syllabus_code": syllabus_code,
                "images": images,
            }

        except Exception as exc:
            print(f"  ❌ {exc}")
            results[key] = {
                "status": "error",
                "folder": folder,
                "file": None,
                "syllabus_code": syllabus_code,
                "error": str(exc),
            }

        time.sleep(REQUEST_DELAY)

    write_audit(results)
    print("\nDone.")


# ---------------------------------------------------------------------------
# Audit report
# ---------------------------------------------------------------------------

def write_audit(results: dict):
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)

    coverage = {}
    for key, r in results.items():
        if r["status"] != "scraped":
            continue
        code = r.get("syllabus_code")
        if code:
            coverage.setdefault(code, []).append(r["file"])
        for covered_code in CHAPTER_SYLLABUS_MAP.get(key, []):
            coverage.setdefault(covered_code, []).append(r["file"])

    lines = [
        "# Moshikur Coverage Audit — IGCSE 0478",
        "",
        "## 0478 Syllabus Coverage",
        "",
        "| Code | Sub-topic | Moshikur Files | Status |",
        "|------|-----------|----------------|--------|",
    ]

    scraped_count = 0
    for code, title in SYLLABUS.items():
        files = coverage.get(code, [])
        if files:
            file_links = ", ".join(f"`{f}`" for f in files)
            lines.append(f"| {code} | {title} | {file_links} | ✅ Covered |")
            scraped_count += 1
        else:
            lines.append(f"| {code} | {title} | — | ⬜ Not mapped |")

    total = len(SYLLABUS)
    lines += [
        "",
        f"**Direct syllabus coverage: {scraped_count}/{total} sub-topics**",
        "",
    ]

    lines += [
        "## All Scraped Pages",
        "",
        "| Key | Folder | File | Images | Syllabus Code | Status |",
        "|-----|--------|------|--------|---------------|--------|",
    ]

    for key, r in results.items():
        img_count = len(r.get("images", []))
        code_label = r.get("syllabus_code") or "—"
        if r["status"] == "scraped":
            lines.append(
                f"| {key} | {r['folder']} | `{r['file']}` | {img_count} | {code_label} | ✅ |"
            )
        else:
            err = r.get("error", "")[:60]
            lines.append(
                f"| {key} | {r['folder']} | — | — | {code_label} | ❌ {err} |"
            )

    audit_file = AUDIT_DIR / "coverage_audit.md"
    audit_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nAudit written → {audit_file.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
