"""Render the AI Infrastructure & Architecture curriculum site.

Consumes site/data/curriculum.json + site/data/lmi.json and writes:
  - site/index.html
  - site/courses/aiinfra-<code>.html   (one per course)

Design system: site/styles.css (ported from johnnyphung.com). This module
only emits HTML structure to use those existing classes — no new CSS beyond
the one small, brief-authorized :focus-visible touch.
"""
import html
import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DATA = SITE / "data"
EXPORTS_SRC = ROOT.parent / "exports"
EXPORTS_DST = SITE / "exports"

FONTS_HREF = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap"
STYLESHEET_HREF = "styles-20260708-accessible-docs.css"
APP_HREF = "app-20260708-footer-outline.js"
ADDENDUM_SLUG = "ai-foundry-integration-addendum"
DOCUMENTS = [
    {
        "slug": "aiinfra-program-readiness-curriculum-alignment-report",
        "title": "AIINFRA Program Readiness and Curriculum Alignment Report",
        "nav_title": "Program Readiness Report",
        "eyebrow": "program readiness report",
        "source": ROOT / "AIINFRA_Program_Readiness_Curriculum_Alignment_Report.md",
        "source_note": "Prepared for Academic Senate, curriculum, and workforce review.",
        "download": "downloads/aiinfra-program-readiness-curriculum-alignment-report.docx",
        "reader_summary": [
            "Use this as the public program-readiness and Senate evidence report.",
            "It frames AIINFRA as a stackable noncredit CDCP plus credit CTE pathway.",
            "It names local launch gates for COCI, LMI, workload, accessibility, security, cost, and employer validation.",
        ],
    },
    {
        "slug": "academic-senate-report-ai-foundry-evaluation",
        "title": "Academic Senate Report - AI Foundry Evaluation for AIINFRA",
        "nav_title": "Academic Senate Report",
        "eyebrow": "academic senate report",
        "source": DATA / "documents" / "academic-senate-report-ai-foundry-evaluation.md",
        "source_note": "Prepared July 7, 2026.",
        "download": "downloads/academic-senate-report-ai-foundry-evaluation.docx",
        "reader_summary": [
            "Use this as the Senate-facing AI Foundry pilot rationale.",
            "It ties foundry acquisition to workload, security, accessibility, cost, and capstone governance.",
            "The curriculum stays vendor-neutral while procurement can compare named platforms.",
        ],
    },
    {
        "slug": ADDENDUM_SLUG,
        "title": "AI Foundry Integration Addendum - Vendor-Neutral Curriculum Language",
        "eyebrow": "ai foundry addendum",
        "source": DATA / "documents" / "ai-foundry-integration-addendum.md",
        "source_note": "Vendor-neutral student and faculty language.",
        "download": "downloads/ai-foundry-integration-addendum.docx",
        "reader_summary": [
            "Use this as the student-facing definition of an AI Foundry.",
            "It standardizes compute-profile language without naming vendors.",
            "It adds reusable foundry evidence and rubric language for assignments.",
        ],
    },
]


def canvas_exports():
    if not EXPORTS_SRC.exists():
        return {}
    exports = {}
    for path in sorted(EXPORTS_SRC.glob("aiinfra-*-*.imscc")):
        match = re.match(r"aiinfra-(\d{3})-", path.name)
        if match:
            exports[match.group(1)] = path
    return exports


def copy_canvas_exports():
    exports = canvas_exports()
    if not exports:
        return exports
    EXPORTS_DST.mkdir(parents=True, exist_ok=True)
    for stale in EXPORTS_DST.glob("aiinfra-*-*.imscc"):
        stale.unlink()
    for src in exports.values():
        shutil.copy2(src, EXPORTS_DST / src.name)
    return exports


def format_file_size(path):
    size = path.stat().st_size
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{size} {unit}"
        size /= 1024


def esc_title(s):
    """Escape <, >, ", ' but leave a bare '&' literal in course/program titles.

    All 10 course titles were checked and contain only '&' (never <, >, quotes,
    or an '&' immediately followed by a valid entity/charref pattern), so this
    is HTML5-safe. It exists solely so the rendered title text matches the
    curriculum.json string byte-for-byte, which build/tests/test_render.py
    checks with a literal `c["title"] in h` substring assertion.
    """
    return html.escape(s, quote=True).replace("&amp;", "&")


# ---------------------------------------------------------------------------
# shell: head / header / footer
# ---------------------------------------------------------------------------

def head(title, desc, depth):
    """depth=0 -> index (assets at './'); depth=1 -> course pages (assets at '../')."""
    p = "../" if depth else ""
    return f'''<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" type="image/svg+xml" href="{p}assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS_HREF}" rel="stylesheet">
  <link rel="stylesheet" href="{p}{STYLESHEET_HREF}">
</head>'''


def header(active, depth):
    p = "../" if depth else ""
    home = p if p else "#top"
    careers_href = (p + "index.html#careers") if depth else "#careers"
    courses_href = (p + "index.html#courses") if depth else "#courses"
    foundry_href = (p + "index.html#foundry") if depth else "#foundry"
    pathway_href = (p + "index.html#pathway") if depth else "#pathway"
    doc_links = "\n      ".join(
        f'<a class="nav-doc" href="{p}documents/{doc["slug"]}.html">{html.escape(doc.get("nav_title", doc["title"]))}</a>'
        for doc in DOCUMENTS[:2]
    )
    def cls(name):
        return "nav-link" + (" is-active" if active == name else "")
    return f'''<header class="site-header">
    <a class="brand" href="{home if depth else '#top'}">AI Infrastructure &amp; Architecture</a>
    <nav class="nav" aria-label="Primary">
      <a class="nav-cta" href="{p}index.html">Program overview</a>
      <a class="{cls('courses')}" href="{courses_href}">Courses</a>
      <a class="{cls('foundry')}" href="{foundry_href}">Foundry</a>
      <a class="{cls('careers')}" href="{careers_href}">Careers</a>
      <a class="{cls('pathway')}" href="{pathway_href}">Pathway</a>
      {doc_links}
    </nav>
  </header>'''


def footer(depth, courses):
    p = "../" if depth else ""
    def preview_for(c):
        weeks = c.get("weeks") or []
        outline = [f'Week {w["n"]}: {w["title"]}' for w in weeks[:3]]
        capstone = next((w for w in weeks if w.get("n") == c.get("capstoneWeek")), None)
        if capstone:
            outline.append(f'Week {capstone["n"]}: {capstone["title"]}')
        return {
            "code": str(c["code"]),
            "title": c["title"],
            "subtitle": c["subtitle"],
            "href": f'{p}courses/aiinfra-{c["code"]}.html',
            "meta": f'Semester {c["semester"]} / {c["hours"]} hours / {c["unitEquivalent"]} unit equivalent',
            "slos": (c.get("slos") or c.get("objectives") or [])[:3],
            "outline": outline[:4],
        }
    previews = [preview_for(c) for c in courses]
    preview_json = json.dumps(previews).replace("<", "\\u003c")
    first = previews[0]
    links = "\n".join(
        f'          <a href="{p}courses/aiinfra-{c["code"]}.html" data-footer-course-preview="{c["code"]}">AIINFRA {c["code"]}<span class="handle">{esc_title(c["title"])}</span></a>'
        for c in courses
    )
    slos = "\n".join(f'              <li>{html.escape(item)}</li>' for item in first["slos"])
    outline = "\n".join(f'              <li>{html.escape(item)}</li>' for item in first["outline"])
    return f'''<footer class="footer" id="connect" aria-labelledby="footer-title">
    <div class="container">
      <div class="footer-top">
        <div class="footer-left">
          <div class="footer-head">
            <span class="eyebrow">// stackable, non-credit, no cost</span>
            <h2 id="footer-title">Build the systems <span class="grad">modern AI runs on.</span></h2>
          </div>
          <nav class="footer-links" aria-label="Course quick links">
{links}
          </nav>
        </div>
        <div class="footer-course-panel" aria-live="polite" data-footer-course-panel>
          <span class="eyebrow">course outline of record snapshot</span>
          <div class="footer-course-titleline">
            <span class="footer-course-code" data-footer-course-code>AIINFRA {html.escape(first["code"])}</span>
            <a class="footer-course-open" href="{html.escape(first["href"])}" data-footer-course-link>Open course</a>
          </div>
          <h3 id="footer-course-preview-title" data-footer-course-title>{esc_title(first["title"])}</h3>
          <p data-footer-course-subtitle>{html.escape(first["subtitle"])}</p>
          <p class="footer-course-meta" data-footer-course-meta>{html.escape(first["meta"])}</p>
          <div class="footer-course-branches">
            <div>
              <span class="branch-label">Student learning outcomes</span>
              <ul data-footer-course-slos>
{slos}
              </ul>
            </div>
            <div>
              <span class="branch-label">Outline preview</span>
              <ol data-footer-course-outline>
{outline}
              </ol>
            </div>
          </div>
        </div>
        <script type="application/json" id="footer-course-data">{preview_json}</script>
      </div>
      <div class="footer-bar">
        <span>&copy; JohnnyRobot LLC &middot; AI Infrastructure and Architecture certificate</span>
        <span>built accessible &middot; WCAG 2.2 AA &middot; open tools &amp; foundry-ready projects</span>
      </div>
    </div>
  </footer>'''


def page(title, desc, depth, active, body_html, extra_head_scripts=""):
    skip_target = "#main"
    return f'''<!DOCTYPE html>
<html lang="en">
{head(title, desc, depth)}
<body>
  <a class="skip-link" href="{skip_target}">Skip to content</a>
  {header(active, depth)}
  <main id="main">
{body_html}
  </main>
  {footer(depth, json.loads((DATA / "curriculum.json").read_text(encoding="utf-8"))["courses"])}
  {extra_head_scripts}
  <script src="{"../" if depth else ""}{APP_HREF}"></script>
</body>
</html>'''


# ---------------------------------------------------------------------------
# document-page builders
# ---------------------------------------------------------------------------

def inline_md(text):
    """Tiny inline Markdown formatter for trusted local curriculum/report docs."""
    placeholders = []

    def stash(markup):
        token = f"@@INLINE{len(placeholders)}@@"
        placeholders.append((token, markup))
        return token

    text = re.sub(
        r"`([^`]+)`",
        lambda m: stash(f"<code>{html.escape(m.group(1))}</code>"),
        text,
    )
    text = html.escape(text)
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda m: stash(
            f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>'
        ),
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    for token, markup in placeholders:
        text = text.replace(token, markup)
    return text


def slugify(text):
    text = re.sub(r"`|\*|_", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "section"


def table_html(lines, table_number):
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) < 2:
        return ""
    head, body = rows[0], rows[2:]
    ths = "".join(f"<th scope=\"col\">{inline_md(cell)}</th>" for cell in head)
    trs = []
    for row in body:
        if len(row) < len(head):
            row = row + [""] * (len(head) - len(row))
        tds = "".join(f"<td>{inline_md(cell)}</td>" for cell in row[:len(head)])
        trs.append(f"<tr>{tds}</tr>")
    return (
        f'<div class="doc-table-wrap" tabindex="0" role="group" aria-label="Scrollable report table {table_number}"><table class="doc-table">'
        f'<caption class="vh">Report table {table_number}</caption>'
        f"<thead><tr>{ths}</tr></thead><tbody>{''.join(trs)}</tbody>"
        "</table></div>"
    )


def markdown_to_html(markdown, title):
    lines = markdown.splitlines()
    if lines and lines[0].lstrip().startswith("# "):
        first = lines[0].lstrip()[2:].strip()
        if first == title:
            lines = lines[1:]

    out = []
    headings = []
    used_ids = {}
    table_number = 1
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]+\|?\s*$", lines[i + 1]):
            table_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].rstrip())
                i += 1
            out.append(table_html(table_lines, table_number))
            table_number += 1
            continue

        m = re.match(r"^(#{1,5})\s+(.+)$", stripped)
        if m:
            level = max(2, min(len(m.group(1)), 6))
            heading_text = m.group(2).strip()
            base_id = slugify(heading_text)
            used_ids[base_id] = used_ids.get(base_id, 0) + 1
            heading_id = base_id if used_ids[base_id] == 1 else f"{base_id}-{used_ids[base_id]}"
            headings.append({"level": level, "text": heading_text, "id": heading_id})
            out.append(f'<h{level} id="{heading_id}">{inline_md(heading_text)}</h{level}>')
            i += 1
            continue

        if stripped.startswith(">"):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f'<blockquote>{" ".join(inline_md(q) for q in quote_lines)}</blockquote>')
            continue

        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i].strip()):
                item = re.sub(r"^[-*]\s+", "", lines[i].strip())
                items.append(f"<li>{inline_md(item)}</li>")
                i += 1
            out.append(f"<ul>{''.join(items)}</ul>")
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                items.append(f"<li>{inline_md(item)}</li>")
                i += 1
            out.append(f"<ol>{''.join(items)}</ol>")
            continue

        para = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (
                not nxt
                or nxt.startswith("#")
                or nxt.startswith(">")
                or nxt.startswith("|")
                or re.match(r"^[-*]\s+", nxt)
                or re.match(r"^\d+\.\s+", nxt)
            ):
                break
            para.append(nxt)
            i += 1
        out.append(f"<p>{inline_md(' '.join(para))}</p>")

    return "\n".join(part for part in out if part), headings


def render_document(doc):
    markdown = pathlib.Path(doc["source"]).read_text(encoding="utf-8")
    article, headings = markdown_to_html(markdown, doc["title"])
    download_link = ""
    if doc.get("download"):
        download_link = (
            f'<a class="document-source-link" href="../{html.escape(doc["download"])}" '
            f'download aria-label="Download accessible Word document for {html.escape(doc["title"])}">'
            "Download accessible Word document</a>"
        )
    summary_items = "\n".join(
        f'            <li>{html.escape(item)}</li>' for item in doc.get("reader_summary", [])
    )
    top_headings = [h for h in headings if h["level"] == 2] or headings
    toc_items = "\n".join(
        f'              <li><a href="#{html.escape(h["id"])}">{inline_md(h["text"])}</a></li>'
        for h in top_headings[:14]
    )
    toc = ""
    if toc_items:
        toc = f'''<div class="document-toc-panel">
          <nav class="document-toc" aria-labelledby="document-toc-title">
            <h2 id="document-toc-title">Sections</h2>
            <ol>
{toc_items}
            </ol>
          </nav>
        </div>'''
    body = f'''<section class="hero document-hero" aria-labelledby="document-title">
      <div class="container hero-inner">
        <a class="back" href="../index.html">&larr; Program overview</a>
        <p class="eyebrow">// {html.escape(doc["eyebrow"])}</p>
        <h1 id="document-title">{html.escape(doc["title"])}</h1>
        <p class="hero-lead">{html.escape(doc["source_note"])}</p>
        {download_link}
      </div>
    </section>
<section class="document-reader-guide" aria-labelledby="reader-guide-title">
      <div class="container document-container">
        <div class="reader-guide">
          <div class="reader-guide-copy">
            <span class="kicker"><span class="idx">guide</span>&nbsp;/ fast orientation</span>
            <h2 id="reader-guide-title">What this document is for</h2>
          </div>
          <ul class="reader-points">
{summary_items}
          </ul>
        </div>
      </div>
    </section>
<section class="section document-section">
      <div class="container document-container">
        <div class="document-shell">
        {toc}
        <article class="document-article" aria-labelledby="document-title">
{article}
        </article>
        </div>
      </div>
    </section>'''
    return page(
        title=doc["title"],
        desc=doc["source_note"],
        depth=1,
        active="documents",
        body_html=body,
    )


# ---------------------------------------------------------------------------
# landing builders
# ---------------------------------------------------------------------------

def hero_program(program):
    stats = program["stats"]
    return f'''<section class="hero" id="top" aria-labelledby="hero-title">
      <div class="container hero-inner">
        <span class="avail"><span class="led" aria-hidden="true"></span>Noncredit &middot; CDCP &middot; enhanced funding</span>
        <p class="eyebrow">// {html.escape(program["credential"])}</p>
        <h1 id="hero-title">Build the infrastructure behind <span class="grad">production-grade AI systems.</span></h1>
        <p class="hero-lead"><strong>{html.escape(program["name"])}</strong> is a {stats["courses"]}-course, {stats["contactHours"]}-contact-hour sequence that takes learners from foundational computing through inference serving, model adaptation, agentic systems, RAG, AI security, and shared AI Foundry operations.</p>
        <div class="hero-chips">
          <span class="chip">Compute &amp; containers</span>
          <span class="chip">Cloud &amp; MLOps</span>
          <span class="chip">Inference serving</span>
          <span class="chip">AI Foundry</span>
          <span class="chip">STEM research studio</span>
          <span class="chip">Agents &amp; RAG</span>
          <span class="chip">AI security &amp; governance</span>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#courses">See the 8 courses<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></a>
          <a class="btn btn-ghost" href="#careers">See labor-market demand</a>
        </div>
        <p class="hero-note">No personal paid hardware required. Foundational labs use open tools and free tiers; advanced projects can use institution-managed shared compute.</p>
      </div>
    </section>'''


def stat_band(program):
    s = program["stats"]
    return f'''<div class="container stats-wrap">
      <div class="stats" role="list" aria-label="Program at a glance">
        <div class="stat" role="listitem"><span class="num">{s["courses"]}</span><span class="cap">courses</span></div>
        <div class="stat" role="listitem"><span class="num">{s["contactHours"]}<span class="u"> hrs</span></span><span class="cap">contact hours</span></div>
        <div class="stat" role="listitem"><span class="num">{s["unitEquivalent"]}-unit<span class="u"> equiv.</span></span><span class="cap">credit equivalent</span></div>
        <div class="stat" role="listitem"><span class="num">{s["semesters"]}<span class="u"> semesters</span></span><span class="cap">stackable pathway</span></div>
      </div>
    </div>'''


def overview(program):
    return f'''<section class="section" id="overview" aria-labelledby="overview-title" style="padding-top:120px;">
      <div class="container">
        <div class="sec-head"><span class="kicker"><span class="idx">01</span>&nbsp;/ overview</span><h2 id="overview-title">What the certificate covers</h2></div>
        <div class="about-body">
          <p class="about-statement">A {program["stats"]["weeksPerCourse"]}-week-per-course sequence from <span class="em">foundational computing</span> to <span class="em">production AI systems.</span></p>
          <div class="about-col">
            <p>{html.escape(program["overview"])}</p>
          </div>
        </div>
      </div>
    </section>'''


def foundry_section(program):
    foundry = program["foundry"]
    research = program["researchStudio"]
    cards = "\n        ".join(
        f'''<article class="foundry-card">
          <span class="foundry-card-k">{html.escape(card["title"])}</span>
          <p>{html.escape(card["body"])}</p>
        </article>'''
        for card in foundry["cards"]
    )
    projects = "\n".join(f'              <li>{html.escape(item)}</li>' for item in research["projects"])
    links = "\n".join(
        f'              <a href="{html.escape(link["url"])}" target="_blank" rel="noopener">{html.escape(link["label"])}</a>'
        for link in research["links"]
    )
    return f'''<section class="section foundry-section" id="foundry" aria-labelledby="foundry-title">
      <div class="container">
        <div class="foundry-intro">
          <div class="foundry-heading">
            <span class="kicker"><span class="idx">02</span>&nbsp;/ ai foundry</span>
            <h2 id="foundry-title">{html.escape(foundry["headline"])}</h2>
          </div>
          <div class="foundry-lower">
            <div class="foundry-copy">
              <p class="note">{html.escape(foundry["summary"])}</p>
              <a class="foundry-question" href="documents/{ADDENDUM_SLUG}.html">What is an AI foundry?</a>
            </div>
            <button class="foundry-shot" type="button" data-lightbox-target="foundry-shot-dialog" aria-label="Open GPU analytics screenshot">
              <img src="assets/ai-foundry-gpu-analytics.png" alt="Screenshot preview of a GPU Performance Analytics dashboard." loading="lazy">
            </button>
          </div>
        </div>
        <dialog class="image-dialog" id="foundry-shot-dialog" aria-label="GPU Performance Analytics screenshot">
          <div class="image-dialog-inner">
            <button class="dialog-close" type="button" data-lightbox-close aria-label="Close image">&times;</button>
            <img src="assets/ai-foundry-gpu-analytics.png" alt="Full-size screenshot preview of a GPU Performance Analytics dashboard.">
          </div>
        </dialog>
        <div class="foundry-grid">
        {cards}
        </div>
        <div class="research-studio" aria-labelledby="research-studio-title">
          <div>
            <span class="kicker"><span class="idx">studio</span>&nbsp;/ stem + cs/cis</span>
            <h3 id="research-studio-title">{html.escape(research["headline"])}</h3>
            <p>{html.escape(research["summary"])}</p>
            <p class="muted">{html.escape(research["dataset"])}</p>
          </div>
          <div class="research-list">
            <h4>Example collaborations</h4>
            <ul>
{projects}
            </ul>
            <div class="resource-links" aria-label="Research dataset links">
{links}
            </div>
          </div>
        </div>
      </div>
    </section>'''


def roadmap(program):
    courses_by_code = None
    sems = []
    for sem in program["semesters"]:
        items = "\n".join(
            f'            <li><a href="courses/aiinfra-{code}.html"><span>AIINFRA {code}</span><span class="code">&rarr;</span></a></li>'
            for code in sem["courses"]
        )
        sems.append(f'''<div class="roadmap-sem">
          <span class="n">Semester {sem["n"]}</span>
          <h3>{html.escape(sem["theme"])}</h3>
          <span class="sem-hours">{sem["hours"]} hrs &middot; {len(sem["courses"])} courses</span>
          <ul>
{items}
          </ul>
        </div>''')
    sems_html = "\n        ".join(sems)
    return f'''<section class="section subtle" id="roadmap" aria-labelledby="roadmap-title">
      <div class="container">
        <div class="sec-head split">
          <div style="display:flex;flex-direction:column;gap:18px;"><span class="kicker"><span class="idx">03</span>&nbsp;/ semester roadmap</span><h2 id="roadmap-title">Four stackable semesters</h2></div>
          <p class="note">Exit after any semester with a coherent, r&eacute;sum&eacute;-ready skill set, or continue to the full credential.</p>
        </div>
        <div class="roadmap">
        {sems_html}
        </div>
      </div>
    </section>'''


def course_grid(courses):
    cards = []
    for c in courses:
        cards.append(f'''<a class="card" href="courses/aiinfra-{c["code"]}.html">
          <span class="cat">AIINFRA {c["code"]} &middot; Semester {c["semester"]}</span>
          <h3>{esc_title(c["title"])}</h3>
          <p>{html.escape(c["subtitle"])}</p>
          <span class="go">View course<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></span>
        </a>''')
    cards_html = "\n        ".join(cards)
    return f'''<section class="section" id="courses" aria-labelledby="courses-title">
      <div class="container">
        <div class="sec-head"><span class="kicker"><span class="idx">04</span>&nbsp;/ the eight courses</span><h2 id="courses-title">Every course in the sequence</h2></div>
        <div class="course-section-grid">
          <div class="grid course-grid">
          {cards_html}
          </div>
        </div>
      </div>
    </section>'''


def lmi_section(lmi, courses):
    soc_sems = {}
    for course in courses:
        for soc in course["socs"]:
            soc_sems.setdefault(soc, set()).add(course["semester"])
    rows = []
    for o in lmi["occupations"]:
        up = "up" if o["growthPct"] >= 0 else "down"
        g = ("+%.1f%%" % o["growthPct"]) if o["growthPct"] >= 0 else ("%.1f%%" % o["growthPct"])
        p = o.get("percentiles") or {}
        top = lmi["meta"]["wageTopCode"]
        def tick(val):
            return f"${val:,}+" if val >= top else f"${val:,}"
        band = (f'<div class="band-inner"><div class="bar"></div><div class="ticks">'
                f'<span>10th {tick(p["p10"])}</span><span>25th {tick(p["p25"])}</span>'
                f'<span>median {tick(p["p50"])}</span><span>75th {tick(p["p75"])}</span>'
                f'<span>90th {tick(p["p90"])}</span></div>'
                f'<p class="note">OEWS current-quarter wage distribution ({html.escape(lmi["meta"]["percentilesAsOf"])}); '
                f'the CA median wage column above is the 2024&ndash;34 <em>projected</em> median, so the two can legitimately differ.</p></div>') if p else \
               '<div class="band-inner"><span class="note">Percentile detail loads live from data.ca.gov.</span></div>'
        sems = ",".join(str(s) for s in sorted(soc_sems.get(o["soc"], set())))
        rows.append(f'''<tr class="lmi-row" data-soc="{o['soc']}" data-median="{o['medianWage']}" data-growth="{o['growthPct']}" data-openings="{o['openings']}" data-sems="{sems}">
  <td><span class="occ">{html.escape(o['title'])}</span><br><span class="soc">{o['soc']}</span></td>
  <td class="num median">${o['medianWage']:,}</td>
  <td class="num growth {up}">{g}</td>
  <td class="num openings">{o['openings']:,}</td></tr>
<tr class="wage-band"><td colspan="4">{band}</td></tr>''')
    m = lmi["meta"]; n = lmi["national"]
    return f'''<section class="section subtle" id="careers"><div class="container">
  <div class="sec-head split"><div><span class="kicker"><span class="idx">05</span>&nbsp;/ careers</span>
  <h2>What this trains you for</h2></div><p class="note">California demand for the roles this certificate builds toward. {html.escape(n['label'])}: {n['value']:,}K ({html.escape(n['period'])}, {n['source']}).</p></div>
  <div class="lmi-controls">
    <span id="lmi-badge" class="live-badge" data-state="snapshot">snapshot &middot; EDD {html.escape(m['verifiedAsOf'])}</span>
    <select id="lmi-filter-sem" aria-label="Filter by semester"><option value="">All semesters</option><option value="1">Semester 1</option><option value="2">Semester 2</option><option value="3">Semester 3</option><option value="4">Semester 4</option></select>
    <select id="lmi-filter-course" aria-label="Filter by course"><option value="">All courses</option></select>
  </div>
  <div class="lmi-table-wrap"><table id="lmi-table" class="lmi-table">
    <caption>Source: {html.escape(m['source'])}. Projections {html.escape(m['projectionsPeriod'])}. Click a row for the wage range.</caption>
    <thead><tr><th scope="col"><button type="button" class="th-sort" data-sort="occ">Occupation (SOC)</button></th><th class="num" scope="col"><button type="button" class="th-sort" data-sort="median">CA median wage</button></th><th class="num" scope="col"><button type="button" class="th-sort" data-sort="growth">Growth &rsquo;24&ndash;&rsquo;34</button></th><th class="num" scope="col"><button type="button" class="th-sort" data-sort="openings">Annual openings</button></th></tr></thead>
    <tbody>{"".join(rows)}</tbody></table></div>
  <p class="hero-note">Wages refresh live from data.ca.gov when available; otherwise the verified snapshot shown. No occupation-level data comes from the BLS API (BLS provides national context only).</p>
</div></section>'''


def pathway(program):
    return f'''<section class="section" id="pathway" aria-labelledby="pathway-title">
      <div class="container">
        <div class="sec-head"><span class="kicker"><span class="idx">06</span>&nbsp;/ credential &amp; pathway</span><h2 id="pathway-title">Credential &amp; pathway</h2></div>
        <div class="about-body">
          <p class="about-statement">A <span class="em">{html.escape(program["credential"])}</span> designed to stack toward credit.</p>
          <div class="about-col">
            <p>{html.escape(program["pathway"])}</p>
            <p class="muted">{html.escape(program["careersNarrative"])}</p>
          </div>
        </div>
      </div>
    </section>'''


# ---------------------------------------------------------------------------
# course-page builders
# ---------------------------------------------------------------------------

def course_hero(c):
    prereq = "None" if c["prereq"] == "none" else f'AIINFRA {c["prereq"]}'
    return f'''<section class="hero course-hero" aria-labelledby="course-title">
      <div class="container hero-inner">
        <a class="back" href="../index.html#courses">&larr; All courses</a>
        <p class="eyebrow">// AIINFRA {html.escape(c["code"])} &middot; Semester {c["semester"]}</p>
        <h1 id="course-title">{esc_title(c["title"])}</h1>
        <p class="hero-lead">{html.escape(c["subtitle"])}</p>
        <p class="hero-note">{html.escape(c["description"])}</p>
      </div>
    </section>'''


def meta_band(c):
    prereq = c.get("requisiteText") or ("Open entry" if c["prereq"] == "none" else f'AIINFRA {c["prereq"]}')
    evidence = c.get("directEvidence", "Course capstone artifact")
    return f'''<div class="container">
      <div class="meta-band">
        <div class="m"><span class="k">Contact hours</span><span class="v">{c["hours"]} hrs</span></div>
        <div class="m"><span class="k">Credit equivalent</span><span class="v">{c["unitEquivalent"]}-unit</span></div>
        <div class="m"><span class="k">Requisite</span><span class="v">{html.escape(prereq)}</span></div>
        <div class="m"><span class="k">Direct evidence</span><span class="v">{html.escape(evidence)}</span></div>
        <div class="m"><span class="k">Length</span><span class="v">{16} weeks</span></div>
      </div>
    </div>'''


def canvas_export_section(c, exports):
    export_path = exports.get(str(c["code"]))
    if not export_path:
        return ""
    filename = export_path.name
    size = format_file_size(export_path)
    note = c.get("canvasExportNote")
    note_html = f'<p><strong>Package note:</strong> {html.escape(note)}</p>' if note else ""
    return f'''<section class="canvas-export-section" id="canvas-export"><div class="container">
  <div class="canvas-export-card">
    <div class="canvas-export-copy">
      <span class="kicker"><span class="idx">download</span>&nbsp;/ canvas package</span>
      <h2>Canvas IMSCC Export</h2>
      <p>Download the complete Canvas import package for AIINFRA {html.escape(c["code"])}.</p>
      {note_html}
      <span class="canvas-export-meta">{html.escape(size)} &middot; .imscc</span>
    </div>
    <a class="canvas-export-link" href="../exports/{html.escape(filename)}" download>
      Canvas IMSCC Export
      <svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"></path><path d="m7 10 5 5 5-5"></path><path d="M5 21h14"></path></svg>
    </a>
  </div>
</div></section>'''


def outcomes(c):
    same = c["slos"] == c["objectives"]
    if same:
        items = "\n".join(f'          <li>{html.escape(o)}</li>' for o in c["objectives"])
        body = f'''<div>
          <h3>Learning outcomes</h3>
          <ol>
{items}
          </ol>
        </div>'''
    else:
        obj_items = "\n".join(f'            <li>{html.escape(o)}</li>' for o in c["objectives"])
        slo_items = "\n".join(f'            <li>{html.escape(s)}</li>' for s in c["slos"])
        body = f'''<div class="outcomes-grid">
          <div>
            <h3>Course objectives</h3>
            <ol>
{obj_items}
            </ol>
          </div>
          <div>
            <h3>Student learning outcomes</h3>
            <ul>
{slo_items}
            </ul>
          </div>
        </div>'''
    return f'''<section class="section" id="outcomes"><div class="container">
  <div class="sec-head"><span class="kicker"><span class="idx">01</span>&nbsp;/ outcomes</span><h2>Outcomes</h2></div>
  {body}
</div></section>'''


def schedule(c):
    rows=[]
    for w in c["weeks"]:
        cls="sched-row"; flag=""
        if w["n"]==c["midtermWeek"]: cls+=" is-midterm"; flag='<span class="flag">Midterm &middot; covers Wks 1&ndash;7</span>'
        if w["n"]==c["capstoneWeek"]: cls+=" is-capstone"; flag='<span class="flag">Capstone</span>'
        rows.append(f'''<div class="{cls}"><div class="wk">Wk {w['n']:02d}</div>
  <div class="body"><div class="t">{html.escape(w['title'])}</div><div class="d">{html.escape(w['summary'])}</div>{flag}</div></div>''')
    return f'''<section class="section" id="schedule"><div class="container">
  <div class="sec-head"><span class="kicker"><span class="idx">02</span>&nbsp;/ schedule</span><h2>16-week schedule</h2></div>
  <div class="sched-list">{"".join(rows)}</div></div></section>'''


def course_controls(c):
    controls = c.get("courseControls") or {}
    if not controls:
        return ""
    cards = []
    for label, key in [
        ("Course boundary", "boundary"),
        ("Assessment artifact", "assessmentArtifact"),
        ("Security/control evidence", "securityEvidence"),
        ("Capstone evidence", "capstoneDeliverables"),
        ("Vendor option", "vendorOption"),
    ]:
        value = controls.get(key)
        if value:
            cards.append(f'''<article class="project-card">
          <span class="project-k">{html.escape(label)}</span>
          <p>{html.escape(value)}</p>
        </article>''')
    cards_html = "\n        ".join(cards)
    return f'''<section class="section foundry-projects" id="course-controls"><div class="container">
  <div class="sec-head split"><div><span class="kicker"><span class="idx">03</span>&nbsp;/ Senate-ready controls</span><h2>Course evidence and boundaries</h2></div>
  <p class="note">These controls make the curriculum reviewable without changing the 10-course sequence.</p></div>
  <div class="project-grid">
        {cards_html}
  </div>
</div></section>'''


def foundry_projects(c):
    projects = c.get("foundryProjects") or []
    if not projects:
        return ""
    idx = "04" if c.get("courseControls") else "03"
    cards = "\n        ".join(
        f'''<article class="project-card">
          <span class="project-k">Foundry project</span>
          <h3>{html.escape(p["title"])}</h3>
          <p>{html.escape(p["summary"])}</p>
          <p class="evidence"><strong>Evidence:</strong> {html.escape(p["evidence"])}</p>
        </article>'''
        for p in projects
    )
    return f'''<section class="section foundry-projects" id="foundry-projects"><div class="container">
  <div class="sec-head split"><div><span class="kicker"><span class="idx">{idx}</span>&nbsp;/ foundry projects</span><h2>Foundry-backed assignments</h2></div>
  <p class="note">These assignments are written in platform-agnostic language. They assess infrastructure evidence, not familiarity with a single vendor console.</p></div>
  <div class="project-grid">
        {cards}
  </div>
</div></section>'''


def tools_section(c):
    idx_num = 3
    if c.get("courseControls"):
        idx_num += 1
    if c.get("foundryProjects"):
        idx_num += 1
    idx = f"{idx_num:02d}"
    groups = []
    for g in c["tools"]:
        tags = "".join(f'<span class="tag">{html.escape(item)}</span>' for item in g["items"])
        groups.append(f'''<div class="tool-group">
          <span class="g">{html.escape(g["group"])}</span>
          <div class="tags">{tags}</div>
        </div>''')
    groups_html = "\n        ".join(groups)
    return f'''<section class="section subtle" id="tools"><div class="container">
  <div class="sec-head"><span class="kicker"><span class="idx">{idx}</span>&nbsp;/ tools</span><h2>Tools &amp; frameworks</h2></div>
  <div class="tools-list" style="display:flex;flex-direction:column;">
        {groups_html}
  </div>
</div></section>'''


def careers_widget(c, lmi):
    occ_by_soc = {o["soc"]: o for o in lmi["occupations"]}
    socs = c["socs"]
    roles = []
    for soc in socs:
        o = occ_by_soc.get(soc)
        if not o:
            continue
        roles.append(f'''<div class="role"><span class="r-t">{html.escape(o["title"])}</span><span class="r-w">${o["medianWage"]:,} median</span></div>''')
    roles_html = "\n        ".join(roles)
    return f'''<section class="section" id="course-careers"><div class="container">
  <div class="careers-widget" data-socs="{html.escape(",".join(socs))}">
    <h3>What this course trains you for</h3>
    <div class="roles">
        {roles_html}
    </div>
    <p class="note">CA median wages, 2024&ndash;34 projections (EDD/OEWS). See the full labor-market dashboard on the <a href="../index.html#careers">program overview</a>.</p>
  </div>
</div></section>'''


def course_nav(c, courses):
    by_code = {x["code"]: x for x in courses}
    links = []
    if c["prereq"] != "none":
        prev = by_code.get(c["prereq"])
        if prev:
            links.append(f'<a class="btn btn-ghost" href="aiinfra-{prev["code"]}.html">&larr; AIINFRA {prev["code"]}: {esc_title(prev["title"])}</a>')
    nxt = c.get("next")
    if nxt:
        nxt_c = by_code.get(str(nxt))
        if nxt_c:
            links.append(f'<a class="btn btn-primary" href="aiinfra-{nxt_c["code"]}.html">AIINFRA {nxt_c["code"]}: {esc_title(nxt_c["title"])} &rarr;</a>')
    links_html = "\n    ".join(links) if links else ""
    return f'''<section class="section" id="course-nav"><div class="container">
  <div class="hero-actions" style="justify-content:space-between;">
    {links_html}
  </div>
  <p class="hero-note"><a href="../index.html">&larr; Back to program overview</a></p>
</div></section>'''


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def render_index(curriculum, lmi):
    program = curriculum["program"]
    courses = curriculum["courses"]
    courses_js = json.dumps([
        {"code": c["code"], "title": c["title"], "socs": c["socs"]} for c in courses
    ])
    body = "\n".join([
        hero_program(program),
        stat_band(program),
        overview(program),
        foundry_section(program),
        roadmap(program),
        course_grid(courses),
        lmi_section(lmi, courses),
        pathway(program),
    ])
    extra = f'<script>window.__COURSES={courses_js};</script>'
    html_out = page(
        title=program["name"],
        desc=program["overview"][:200],
        depth=0,
        active="courses",
        body_html=body,
        extra_head_scripts=extra,
    )
    (SITE / "index.html").write_text(html_out, encoding="utf-8")


def render_course(c, courses, lmi, exports):
    body = "\n".join([
        course_hero(c),
        meta_band(c),
        canvas_export_section(c, exports),
        outcomes(c),
        schedule(c),
        course_controls(c),
        foundry_projects(c),
        tools_section(c),
        careers_widget(c, lmi),
        course_nav(c, courses),
    ])
    html_out = page(
        title=f'AIINFRA {c["code"]}: {c["title"]}',
        desc=c["subtitle"],
        depth=1,
        active="courses",
        body_html=body,
    )
    out_path = SITE / "courses" / f'aiinfra-{c["code"]}.html'
    out_path.write_text(html_out, encoding="utf-8")


def main():
    curriculum = json.loads((DATA / "curriculum.json").read_text(encoding="utf-8"))
    lmi = json.loads((DATA / "lmi.json").read_text(encoding="utf-8"))
    exports = copy_canvas_exports()
    (SITE / "courses").mkdir(parents=True, exist_ok=True)
    (SITE / "documents").mkdir(parents=True, exist_ok=True)
    render_index(curriculum, lmi)
    for c in curriculum["courses"]:
        render_course(c, curriculum["courses"], lmi, exports)
    for doc in DOCUMENTS:
        (SITE / "documents" / f'{doc["slug"]}.html').write_text(render_document(doc), encoding="utf-8")
    print(f'Rendered site/index.html + {len(curriculum["courses"])} course pages + {len(DOCUMENTS)} document pages.')


if __name__ == "__main__":
    main()
