# AI Infrastructure & Architecture — curriculum site

Static site for the JohnnyRobot LLC AI Infrastructure and Architecture curriculum certificate: a landing page (`index.html`), one page per course (`courses/aiinfra-<code>.html`), and supporting report/addendum pages (`documents/*.html`), rendered from JSON/Markdown data by the scripts in `build/`.

## Serve locally

```bash
python3 build/serve.py
```

Serves `site/` at **http://127.0.0.1:8099** (plain `http.server`, no build step required — just open the URL once the process is running).

## Rebuild content

The site is generated, not hand-edited. To change it, edit the source data/templates below and re-run the relevant script.

```bash
# 1. Re-merge course content (site/data/_raw/*.json) into site/data/curriculum.json
python3 build/merge_curriculum.py

# 2. Re-verify labor-market data (EDD projections + OEWS percentiles + BLS national context)
#    into site/data/lmi.json. Requires a BLS API key at build time only.
BLS_API_KEY=... python3 build/refresh_lmi.py

# 3. Render index.html + all course pages from curriculum.json + lmi.json
python3 build/render_site.py
```

Run step 3 any time `curriculum.json`, `lmi.json`, or `site/data/documents/*.md` changes — it fully regenerates `site/index.html`, every `site/courses/aiinfra-*.html`, and every generated document page.

## Tests

```bash
for t in styles curriculum lmi render; do python3 build/tests/test_$t.py; done
```

All four should print `... OK`.

## Deploy

Copy the `site/` directory to any static host (no server-side code, no build step at deploy time). Everything the browser needs — HTML, CSS, JavaScript, JSON data under `site/data/`, generated documents, and Canvas IMSCC exports under `site/exports/` — is static.

## Data provenance

- **Live wage/growth/openings data** refreshes in the browser from `data.ca.gov`'s CKAN API (CORS-open, no key required). If that fetch fails or hasn't resolved, the page falls back to the verified snapshot baked into `site/data/lmi.json` at build time — the dashboard badge reflects which state is active (`● live` vs. `snapshot`).
- **BLS data** (national context line) is fetched server-side only, during `build/refresh_lmi.py`, using `BLS_API_KEY` from the environment. The key is never read by, or shipped in, any file under `site/` — it is build-time-only and does not appear in the repo.
