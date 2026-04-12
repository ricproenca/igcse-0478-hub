# Moshikur Website Scraper Plan

## Context

Scrape content from https://moshikur.com/igcse-o-level-cs/ — an IGCSE Computer Science 0478 revision website. The user provides one URL per sub-topic. The scraper extracts text notes, HTML tables, and images from each page and saves everything locally for offline use and auditing against the 0478 syllabus.

---

## Goal

- Scrape each sub-topic page: text content, tables, images
- Save output as clean markdown files, one per sub-topic
- Download images locally alongside the markdown
- Organize output mirroring the 0478 syllabus structure (Topics 1–11)
- After all pages are scraped, produce an audit table showing which 0478 sub-topics have Moshikur coverage and which don't

---

## Input Format

`tools/moshikur_urls.py` — a Python dict mapping sub-topic codes to URLs (user fills this in):

```python
URLS = {
    "1.1": "https://moshikur.com/...",
    "1.2": "https://moshikur.com/...",
    # leave out any sub-topics not covered
}
```

Any sub-topic without an entry is recorded as "No URL provided" in the audit.

---

## Scraper Design

### Script: `tools/moshikur_scraper.py`

**Dependencies:**
- `requests` — HTTP fetching
- `beautifulsoup4` — HTML parsing
- `markdownify` — HTML-to-markdown conversion

**Per-page extraction logic:**
1. Fetch the URL with `requests.get()`
2. Parse with BeautifulSoup, targeting the main content area
3. Strip nav, header, footer, sidebar, comment sections
4. Download all `<img>` images to `study/moshikur/images/<topic>/`; rewrite `src` to relative paths in markdown
5. Convert `<table>` elements to markdown pipe-tables
6. Convert remaining HTML to clean markdown via `markdownify`
7. Write to `study/moshikur/<topic_dir>/<subtopic_slug>.md`

**Content selector priority** (tries each in order):
1. `<main>`
2. `<article>`
3. `.entry-content`
4. `.post-content`
5. `<body>` minus nav/footer

---

## Output Structure

```
study/moshikur/
  topic1_data_representation/
    1_1_number_systems.md
    1_2_text_sound_images.md
    1_3_data_storage_compression.md
  topic2_data_transmission/
    2_1_types_methods_transmission.md
    2_2_error_detection.md
    2_3_encryption.md
  topic3_hardware/
    ...
  topic7_algorithm_design/
    7_1_pdlc.md
    7_2_problem_decomposition.md
    ...
  images/
    topic1/
      img_001.png
    topic7/
      img_001.jpg
  audit/
    coverage_audit.md
```

---

## Audit Report: `study/moshikur/audit/coverage_audit.md`

Auto-generated after all scrapes complete:

| Sub-topic | Title | Output File | Status |
|-----------|-------|-------------|--------|
| 1.1 | Number Systems | `1_1_number_systems.md` | ✅ Scraped |
| 1.2 | Text, Sound and Images | `1_2_text_sound_images.md` | ✅ Scraped |
| 6.3 | Artificial Intelligence | — | ❌ No URL provided |

---

## Files to Create

| File | Purpose |
|------|---------|
| `tools/moshikur_urls.py` | URL config dict — user fills in sub-topic URLs |
| `tools/moshikur_scraper.py` | Main scraper script |
| `tools/requirements_scraper.txt` | Python dependencies |
| `study/moshikur/` | Output directory (created by script) |
| `study/moshikur/audit/coverage_audit.md` | Coverage audit (auto-generated) |

---

## Workflow

1. Fill in `tools/moshikur_urls.py` with sub-topic URLs
2. Install dependencies: `pip install -r tools/requirements_scraper.txt`
3. Run: `python3 tools/moshikur_scraper.py`
4. Script fetches each URL, saves markdown + images, prints progress
5. Review `study/moshikur/audit/coverage_audit.md` for coverage gaps

---

## 0478 Sub-topics to Cover

### Paper 1 (Topics 1–6)
| Code | Sub-topic |
|------|-----------|
| 1.1 | Number Systems |
| 1.2 | Text, Sound and Images |
| 1.3 | Data Storage and Compression |
| 2.1 | Types and Methods of Data Transmission |
| 2.2 | Methods of Error Detection |
| 2.3 | Encryption |
| 3.1 | Computer Architecture |
| 3.2 | Input and Output Devices |
| 3.3 | Data Storage |
| 3.4 | Network Hardware |
| 4.1 | Types of Software and Interrupts |
| 4.2 | Types of Programming Language, Translators and IDEs |
| 5.1 | The Internet and the World Wide Web |
| 5.2 | Digital Currency |
| 5.3 | Cyber Security |
| 6.1 | Automated Systems |
| 6.2 | Robotics |
| 6.3 | Artificial Intelligence |

### Paper 2 (Topics 7–11)
| Code | Sub-topic |
|------|-----------|
| 7.1 | Program Development Life Cycle |
| 7.2 | Problem Decomposition |
| 7.3 | Algorithm Design Methods |
| 7.4 | Standard Methods of Solution |
| 7.5 | Validation and Verification |
| 7.6 | Testing |
| 7.7 | Trace Tables |
| 7.8 | Error Identification |
| 8.1 | Programming Concepts |
| 8.2 | Arrays |
| 8.3 | File Handling |
| 9.1 | Database Design |
| 9.2 | SQL Queries |
| 10.1 | Logic Gates |
| 10.2 | Logic Circuits |
| 11.1 | Writing Pseudocode for Context Scenario |
