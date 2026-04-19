Project Exploration Report: igcse-0478-hub

1. Overall Directory Structure

Top-level organization:
/Users/ricproenca/CodeProjects/igcse-0478-hub/
├── .claude/                    # Claude Code configuration
│   └── settings.local.json    # Permissions for web scraping
(moshikur.com)
├── .git/                       # Git repository
├── .venv/                      # Python virtual environment
├── .gitignore
├── .ruff_cache/
├── LICENSE
├── README.md                   # Brief project description
├── docs/                       # Raw source documents and resources
│   ├── textbook/              # PDFs to be converted (10 chapter PDFs)
│   ├── moshikur/              # Scraped web content (from moshikur.com)
│   ├── papers_p1/             # Past paper materials (73 folders)
│   ├── papers_p2/             # Past paper materials (51 folders)
│   ├── pmt/                   # PMT Education notes (4 chapters)
│   └── guides/
├── markdown/                   # Output markdown files
│   ├── pmt_chapter_*.md       # 20 files (10 chapters, definitions +
notes)
│   ├── paper*_*.md            # 22 exam paper files
│   ├── syllabus.md
│   └── textbook/              # EMPTY (destination for PDF conversions)
├── planning/                   # Project planning documents
│   ├── IDEAS.md
│   ├── moshikur_webscrapping.md
│   ├── paper1_plan.md
│   └── paper2_plan.md
└── tools/
    └── moshikur/              # Web scraping tool
        ├── requirements.txt   # Dependencies (requests, beautifulsoup4,
markdownify)
        ├── scraper.py        # Main scraping script (285+ lines)
        └── urls.py           # URL configuration and syllabus mapping

2. Contents of Key Directories

/docs/textbook/ (PDF Source)

10 PDF files (textbook chapters):
- Chapter 01.pdf (1.68 MB)
- Chapter 02.pdf (829 KB)
- Chapter 03.pdf (1.97 MB)
- Chapter 04.pdf (1.07 MB)
- Chapter 05.pdf (1.14 MB)
- Chapter 06.pdf (1.87 MB)
- Chapter 07.pdf (1.35 MB) - most recently modified Apr 19
- Chapter 08.pdf (1.06 MB)
- Chapter 09.pdf (802 KB)
- Chapter 10.pdf (2.94 MB)

Total: ~14.9 MB of textbook content

/markdown/textbook/ (Destination)

Currently empty - this is the target directory for PDF conversions.

/markdown/ (Existing Output Examples)

20 PMT education markdown files:
- pmt_chapter_0X_definitions.md (10 files) - ~60-330 lines each
- pmt_chapter_0X_notes.md (10 files) - ~140-480 lines each
- pmt_master_definitions.md (41 KB)
- syllabus.md (6.9 KB)
- Exam paper files: 22 markdown files from past papers (2021-2025),
including question and answer documents

3. PDF-to-Markdown Conversion Tools & Patterns

Existing Conversion Infrastructure

No dedicated PDF conversion tool exists yet, but the project has a
strong web-scraping pattern:

/tools/moshikur/scraper.py (285+ lines):
- Uses requests to fetch HTML pages
- Uses BeautifulSoup for parsing
- Uses markdownify library to convert HTML to Markdown
- Handles:
    - HTML table conversion to markdown tables
    - Image downloading and embedding
    - Metadata preservation (source URL in headers)
    - Output organization by topic folder
    - Image naming convention: img_NNN.ext

Dependencies available in requirements.txt:
requests>=2.31.0
beautifulsoup4>=4.12.0
markdownify>=0.11.6

Image handling pattern (from /docs/moshikur/):
- Images stored in:
docs/moshikur/images/<topic_folder>/<slug>/img_NNN.ext
- Referenced in markdown as relative paths

4. Existing Markdown Format Patterns

Chapter Notes Format (pmt_chapter_0X_notes.md)

Structure:
- Title: # CAIE Computer Science IGCSE — Chapter X: <Topic>
- Subtitle: ### Advanced Notes
- Horizontal rules: ---
- Main sections: ## 1.1 Topic Name
- Subsections: ### Subtopic
- Complex tables with headers and borders
- Inline code: `code`
- Bold/italic: **bold**, *italic*
- Lists (ordered and unordered)
- Horizontal dividers between sections

Example table format:
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Content  | Content  | Content  |
| Content  | Content  | Content  |

Image reference pattern (from PMT notes):
![Diagram: <description>]
Or in moshikur format:
![description](relative/path/to/img_001.png)

Definitions Format (pmt_chapter_0X_definitions.md)

Structure:
- Title: # Chapter XX Definitions
- Subtitle: *Topic X: <Topic Name>*
- Each definition: ## Term Name followed by body text
- Simple, clean formatting with double line breaks between entries

Exam Papers Format (paper*_*_*.md)

Structure:
- Complex table-based layout with columns:
    - Paper, Question, Sub-parts (a, b, c, etc.)
    - Marks, Topic, Sub-topic, Difficulty
    - AO (Assessment Objective) codes
    - Description of each question
- Tables used extensively for structured data mapping questions to
syllabus

5. Available Tools & Environment

Python Environment:
- Python 3.14 virtual environment active at .venv/
- Available libraries for conversion:
    - requests - HTTP requests
    - beautifulsoup4 - HTML parsing
    - markdownify - HTML to Markdown conversion
    - Can be extended with PDF-specific libraries

No existing PDF tools are configured, which means you'll need to
choose/install a PDF extraction library such as:
- PyPDF2 or pdfplumber for PDF text extraction
- pdf2image + OCR if handling scanned PDFs
- fitz (PyMuPDF) for more advanced PDF processing

Development pattern:
- Scraping-focused architecture (web → Markdown)
- Strong folder/topic routing system
- Image downloading and local storage
- Audit/tracking system for coverage
- Git history shows incremental content generation

6. File Paths Summary

Key paths for PDF conversion:

Purpose: PDF Source Files
Path: /Users/ricproenca/CodeProjects/igcse-0478-hub/docs/textbook/
────────────────────────────────────────
Purpose: Markdown Destination
Path: /Users/ricproenca/CodeProjects/igcse-0478-hub/markdown/textbook/
────────────────────────────────────────
Purpose: Existing Tool
Path:
/Users/ricproenca/CodeProjects/igcse-0478-hub/tools/moshikur/scraper.py
────────────────────────────────────────
Purpose: Tool Dependencies
Path: /Users/ricproenca/CodeProjects/igcse-0478-hub/tools/moshikur/requi
rements.txt
────────────────────────────────────────
Purpose: Example Output (Notes)
Path: /Users/ricproenca/CodeProjects/igcse-0478-hub/markdown/pmt_chapter
_01_notes.md
────────────────────────────────────────
Purpose: Example Output (Definitions)
Path: /Users/ricproenca/CodeProjects/igcse-0478-hub/markdown/pmt_chapter
_01_definitions.md
────────────────────────────────────────
Purpose: Example Output (Exam Papers)
Path: /Users/ricproenca/CodeProjects/igcse-0478-hub/markdown/paper1_2024
_questions.md
────────────────────────────────────────
Purpose: Existing Web Scrape Examples
Path: /Users/ricproenca/CodeProjects/igcse-0478-hub/docs/moshikur/topic1
_data_representation/1_1_number_system.md