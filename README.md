# AI Infrastructure & Architecture (AIINFRA) — Certificate Curriculum & Site

Public curriculum, marketing site, and Canvas course exports for the **AI
Infrastructure and Architecture (AIINFRA)** community-college certificate.

🔗 **Live site:** https://aiinfra.johnnyphung.com

## What this is

An 8-course, 4-semester CTE certificate that takes students from AI-systems
foundations through production inference serving, model adaptation, agents/MCP,
RAG/LLMOps, and AI security — ending in a capstone. It is designed to be
**adopted and adapted by other California community colleges** (both a credit CTE
Certificate of Achievement and a noncredit CDCP pathway).

| # | Course | Semester |
|---|---|---|
| AIINFRA 100 | AI Systems & Development Environments | 1 |
| AIINFRA 101 | Applied Infrastructure & Containerization | 1 |
| AIINFRA 200 | Production Inference Serving & GPU Orchestration | 2 |
| AIINFRA 201 | Model Adaptation — Fine-Tuning & Quantization | 2 |
| AIINFRA 300 | Agentic AI & the Model Context Protocol (MCP) | 3 |
| AIINFRA 301 | Production RAG & LLMOps — Observability & Evaluation | 3 |
| AIINFRA 302 | AI Security, Guardrails & Governance | 4 |
| AIINFRA 303 | Capstone Project | 4 |

**54 contact hours per course · 432 total · 24-unit credit-CTE equivalent.**

## Canvas course exports (IMSCC)

Ready-to-import **Common Cartridge** files for all eight courses live in
[`site/exports/`](site/exports/) — each course page on the site links its
cartridge. Import into Canvas (or any IMSCC-compatible LMS) to get the modules,
lecture pages, labs, discussions, and quizzes.

## Repository layout

```
site/            The built, deployable website (static)
  index.html       program landing page
  courses/         one page per course (aiinfra-100 … aiinfra-303)
  documents/       readiness / evaluation reports
  downloads/       .docx report downloads
  exports/         the 8 Canvas IMSCC cartridges
  data/            curriculum.json — the data the site is generated from
build/           generators: render_site.py (data → HTML), generate_docx_downloads.py, tests
```

## Build & deploy

The site is **data-driven**: edit `site/data/curriculum.json`, then regenerate.

```bash
python3 build/render_site.py            # curriculum.json → HTML
python3 build/generate_docx_downloads.py # report markdown → .docx
```

Deployed via Cloudflare Pages:

```bash
wrangler pages deploy site --project-name=infra-cert --branch=main
```

## License

Licensed under **[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)**
(`SPDX-License-Identifier: CC-BY-4.0`). You are free to share and adapt this
curriculum and site — including for another college — with attribution.
