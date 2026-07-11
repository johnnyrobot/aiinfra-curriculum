import pathlib, re, json
idx = pathlib.Path("site/index.html").read_text(encoding="utf-8")
for needle in ['id="lmi-table"','id="lmi-badge"','data-state="snapshot"','class="roadmap"',
               '540','30-unit','href="courses/aiinfra-100.html"','href="courses/aiinfra-303.html"',
               '<link rel="stylesheet" href="styles-20260708-accessible-docs.css">','data-sort="growth"',
               'href="documents/aiinfra-program-readiness-curriculum-alignment-report.html"',
               'href="documents/academic-senate-report-ai-foundry-evaluation.html"',
               'href="documents/ai-foundry-integration-addendum.html">What is an AI foundry?</a>']:
    assert needle in idx, f"index.html missing {needle}"
assert idx.index('class="nav-cta" href="index.html">Program overview</a>') < idx.index('href="#courses"'), "Program overview nav must precede Courses"
assert 'course-link-rail' not in idx, "course list must not render a duplicate right-side link rail"
assert idx.count('class="lmi-row"') == 8, "index must bake all 8 occupation rows"
cur = json.loads(pathlib.Path("site/data/curriculum.json").read_text())
for c in cur["courses"]:
    h = pathlib.Path(f"site/courses/aiinfra-{c['code']}.html").read_text(encoding="utf-8")
    assert c["title"] in h, f"{c['code']} title missing"
    assert h.count('class="sched-row') == 16, f"{c['code']} must have 16 schedule rows"
    assert 'class="is-midterm"' in h.replace('sched-row is-midterm','is-midterm') or 'is-midterm' in h, f"{c['code']} midterm flag"
    assert 'is-capstone' in h, f"{c['code']} capstone flag"
    assert 'class="careers-widget"' in h and 'data-socs' in h, f"{c['code']} careers widget"
    assert 'id="course-controls"' in h, f"{c['code']} course controls section"
    assert c["requisiteText"] in h, f"{c['code']} requisite text missing"
    assert c["directEvidence"] in h, f"{c['code']} direct evidence missing"
    controls = c["courseControls"]
    assert controls["assessmentArtifact"][:30] in h, f"{c['code']} assessment artifact missing"
    assert controls["securityEvidence"][:30] in h, f"{c['code']} security evidence missing"
    assert '../styles-20260708-accessible-docs.css' in h and '../app-20260708-footer-outline.js' in h, f"{c['code']} asset links"
    exports = list(pathlib.Path("site/exports").glob(f"aiinfra-{c['code']}-*.imscc"))
    assert len(exports) == 1, f"{c['code']} must have exactly one current canvas export"
    assert 'id="canvas-export"' in h and "Canvas IMSCC Export" in h, f"{c['code']} canvas export section"
    assert f'href="../exports/{exports[0].name}"' in h, f"{c['code']} canvas export link"
    for o in c["objectives"]: assert o.split("(")[0][:30] in h, f"{c['code']} objective missing"
for doc in [
    ("aiinfra-program-readiness-curriculum-alignment-report", "AIINFRA Program Readiness and Curriculum Alignment Report", "aiinfra-program-readiness-curriculum-alignment-report.docx"),
    ("academic-senate-report-ai-foundry-evaluation", "Academic Senate Report", "academic-senate-report-ai-foundry-evaluation.docx"),
    ("ai-foundry-integration-addendum", "AI Foundry Integration Addendum", "ai-foundry-integration-addendum.docx"),
]:
    h = pathlib.Path(f"site/documents/{doc[0]}.html").read_text(encoding="utf-8")
    assert doc[1] in h, f"{doc[0]} document content missing"
    assert "app.notion.com" not in h and "Open source in Notion" not in h, f"{doc[0]} must not link to Notion"
    assert f'../downloads/{doc[2]}" download' in h, f"{doc[0]} Word download missing"
    assert pathlib.Path(f"site/downloads/{doc[2]}").is_file(), f"{doc[0]} Word file missing"
    assert 'class="reader-guide"' in h and 'class="document-shell"' in h, f"{doc[0]} reader layout missing"
    assert 'class="document-toc"' in h and '<h2 id=' in h, f"{doc[0]} accessible headings/toc missing"
    assert '<caption class="vh">' in h or doc[0] != "aiinfra-program-readiness-curriculum-alignment-report", f"{doc[0]} table captions missing"
    assert 'class="doc-table-wrap" tabindex="0" role="group"' in h or doc[0] != "aiinfra-program-readiness-curriculum-alignment-report", f"{doc[0]} keyboard table access missing"
    assert '../styles-20260708-accessible-docs.css' in h and '../app-20260708-footer-outline.js' in h, f"{doc[0]} asset links"
print("test_render OK")
