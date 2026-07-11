import re, pathlib
css = pathlib.Path("site/styles.css").read_text(encoding="utf-8")
required_tokens = ["--accent:#4F46E5", "--bg:#FFFFFF", "--sans", "--mono",
                   "--text:#15161A", "--border:#ECECF1", "--maxw", "--r-pill"]
required_classes = [".site-header", ".hero", ".kicker", ".btn-primary", ".card", ".stats",
                    ".section", ".footer", ".course-hero", ".meta-band", ".sched-row",
                    ".is-midterm", ".is-capstone", ".lmi-table", ".lmi-row", ".wage-band",
                    ".live-badge", ".careers-widget", ".roadmap"]
norm = css.replace(" ", "")
for t in required_tokens:
    assert t.replace(" ", "") in norm, f"missing token {t}"
for c in required_classes:
    assert c in css, f"missing class {c}"
assert "prefers-color-scheme" not in css, "no dark-mode media query allowed (light only)"
assert "prefers-reduced-motion" in css, "must honor reduced motion"
assert ".course-grid{display:grid;grid-template-columns:repeat(3,1fr);" in norm, "course cards should render as a 3-column desktop grid"
assert "@media(max-width:1180px)" in norm and ".course-grid{grid-template-columns:repeat(2,1fr);}" in norm, "course cards need a 2-column medium breakpoint"
print("test_styles OK")
