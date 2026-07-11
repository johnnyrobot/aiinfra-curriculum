import json, pathlib
ORDER = ["100","101","102","200","201","202","300","301","302","303"]
SEM = {**{c:1 for c in ORDER[:3]}, **{c:2 for c in ORDER[3:6]}, **{c:3 for c in ORDER[6:]}}
SOCS = {  # from spec §8 — only the 8 verified SOCs
 "100":["15-1299","15-1252"], "101":["15-1252","15-1299"], "102":["15-1252","15-1299","15-1244"],
 "200":["15-1241","15-1244","15-1252","15-1299"], "201":["15-1252","15-1299"], "202":["15-2051","15-1299"],
 "300":["15-1252","15-1299"], "301":["15-2051","15-1299"], "302":["15-1299","15-1252"],
 "303":["15-1252","15-2051","11-3021"]}

FOUNDRY_PROJECTS = {
  "200": [
    {
      "title": "Container-to-Cloud Deployment Plan",
      "summary": "Students compare local containers, Kubernetes, managed cloud services, and shared AI Foundry capacity by deployment need rather than by vendor console.",
      "evidence": "Container image, scan report, deployment option matrix, CI/CD run, access/data/logging risk note, and exportability checklist."
    }
  ],
  "201": [
    {
      "title": "Hosted Inference Service",
      "summary": "Teams deploy a production-style inference endpoint on a shared GPU VM or cluster with an authenticated API, containerized model server, monitoring, and right-sizing evidence.",
      "evidence": "Architecture diagram, endpoint demo, GPU memory/utilization, latency, throughput, logs, runbook, and security boundary."
    }
  ],
  "202": [
    {
      "title": "Custom Adapter Training",
      "summary": "Teams train a task-specific LoRA/QLoRA adapter with scheduled foundry GPU time, compare base versus adapted behavior, and package the result for serving or handoff.",
      "evidence": "Dataset card, baseline and post-training evaluation, training logs, adapter artifact, model card, compute profile, and cost comparison."
    },
    {
      "title": "STEM Dataset Preparation Extension",
      "summary": "Students working with STEM partners add domain meaning to dataset prep: units, variables, plausible outputs, unacceptable errors, versioning, and reproducible splits.",
      "evidence": "Data card, domain note, infrastructure note, preprocessing script, data version, random seeds, and evaluation split."
    }
  ],
  "301": [
    {
      "title": "Hosted RAG Chatbot With Optional Voice Agent",
      "summary": "Teams run a persistent domain chatbot with app/API, retrieval pipeline, vector store, model endpoint, evaluation set, tracing, and optional realtime voice services.",
      "evidence": "Hosted demo, ingestion plan, golden evaluation set, traces/logs, retrieval evidence, operational runbook, and privacy/security boundary."
    }
  ],
  "302": [
    {
      "title": "Flat-Fee vs Metered Compute Memo",
      "summary": "Students compare shared annual capacity against metered GPU, token, and managed-service pricing for cohort workloads including inference, RAG, voice, and adapter training.",
      "evidence": "Cohort assumptions, workload estimates, utilization target, break-even analysis, governance risks, and pilot-size recommendation."
    }
  ],
  "303": [
    {
      "title": "AI Foundry Fit Check",
      "summary": "Every capstone proposal states whether shared compute is required, what profile is requested, what services will persist, and what runtime evidence will be collected.",
      "evidence": "Foundry yes/no decision, workload type, compute profile, data classification, access pattern, expected logs/metrics, and fallback plan."
    },
    {
      "title": "STEM Research Infrastructure Studio",
      "summary": "CS/CIS students partner with STEM students or faculty: STEM defines the research question and validation; AIINFRA teams build the reproducible compute, data, benchmark, and monitoring environment.",
      "evidence": "Joint charter, data card, baseline benchmark, reproducibility package, research-facing summary, and technical appendix."
    },
    {
      "title": "Foundry Evidence Appendix",
      "summary": "Foundry-backed capstones document what ran on shared infrastructure and why the selected compute profile was appropriate.",
      "evidence": "Deployment evidence, operational metrics, security/governance notes, cost/right-sizing memo, model or adapter references, and runbook."
    }
  ]
}

REQUISITES = {
  "100": "Open entry; no prior AI or programming experience required.",
  "101": "Advisory/corequisite: AIINFRA 100.",
  "102": "Advisory/corequisite: AIINFRA 101 or equivalent command-line comfort.",
  "200": "Requires AIINFRA 102 or equivalent Linux, Docker, Git, and command-line readiness.",
  "201": "Requires AIINFRA 200 or equivalent container/cloud deployment readiness.",
  "202": "Requires AIINFRA 201 or equivalent model-serving readiness.",
  "300": "Requires AIINFRA 202 or equivalent production AI systems readiness.",
  "301": "Requires AIINFRA 300 or equivalent agent/RAG development readiness.",
  "302": "Requires AIINFRA 301 or equivalent production AI workflow readiness.",
  "303": "Requires the AIINFRA production sequence or equivalent skills.",
}

DIRECT_EVIDENCE = {
  "100": "Infrastructure decision memo",
  "101": "Reproducible dev environment repo",
  "102": "Applied infrastructure lab portfolio",
  "200": "Scanned container and CI/CD deployment",
  "201": "Measured inference-serving deployment",
  "202": "Adapter or quantized model evaluation",
  "300": "Secure agent/MCP tool surface",
  "301": "Production RAG evaluation report",
  "302": "Security/governance review package",
  "303": "Employer-readable capstone portfolio",
}

CANVAS_EXPORT_NOTES = {}

COURSE_CONTROLS = {
  "100": {
    "boundary": "Survey course for AI infrastructure literacy; does not replace CIS programming, data science modeling, cloud administration, or cybersecurity fundamentals.",
    "assessmentArtifact": "AI workload infrastructure decision memo plus a basic containerized development environment.",
    "securityEvidence": "Survey-level OWASP LLM Top 10 and responsible-AI risk note.",
    "capstoneDeliverables": "Prototype-vs-production infrastructure plan, environment proof, cost/access note, and short presentation."
  },
  "101": {
    "boundary": "Focuses on Python, Git, Linux, and notebooks as AI infrastructure tooling, not as a full general programming course.",
    "assessmentArtifact": "Version-controlled repository with Python environment, Git workflow, Linux shell tasks, and notebook reproducibility notes.",
    "securityEvidence": "Secrets hygiene, dependency pinning, .gitignore controls, and local credential-handling checklist.",
    "capstoneDeliverables": "Reproducible repository, setup instructions, dependency lockfile or environment file, and recorded environment walkthrough."
  },
  "102": {
    "boundary": "First-semester applied lab for Linux, local services, troubleshooting, and Docker basics; full Kubernetes and GPU orchestration move to AIINFRA 200/201.",
    "assessmentArtifact": "Local AI/Python service with setup notes, troubleshooting transcript, basic Dockerfile, and runbook.",
    "securityEvidence": "Secrets hygiene, local access boundary, dependency review, and documentation of what should not be committed or baked into images.",
    "capstoneDeliverables": "Repository, local service demo, Docker build evidence, troubleshooting notes, access/control note, and runbook."
  },
  "200": {
    "boundary": "Teaches the deployment bridge from containers to Kubernetes, cloud platforms, and CI/CD; it is not a single-vendor certification bootcamp.",
    "assessmentArtifact": "Containerized AI service with image scan, registry tag, Kubernetes or cloud deployment, and GitHub Actions evidence.",
    "securityEvidence": "Image scanning, least-privilege IAM, secrets controls, OIDC or equivalent CI/CD authentication, and budget/quota guardrails.",
    "capstoneDeliverables": "Deployment notes, scan report, cost estimate, security boundary, CI/CD logs, and local/no-cost fallback evidence.",
    "vendorOption": "Students may specialize in AWS, Azure, or GCP, but required outcomes must have a no-cost or local fallback."
  },
  "201": {
    "boundary": "Focuses on production inference serving and GPU operations; local desktop tools are treated as development and prototype references only.",
    "assessmentArtifact": "Served model endpoint with measured latency, throughput, memory use, scaling notes, and operational logs.",
    "securityEvidence": "Endpoint access control, network boundary, model artifact provenance, resource quotas, and operational runbook.",
    "capstoneDeliverables": "Architecture diagram, endpoint demo, GPU utilization evidence, latency/throughput metrics, logs, and runbook."
  },
  "202": {
    "boundary": "Focuses on model adaptation and deployment readiness, not broad data science theory or from-scratch model research.",
    "assessmentArtifact": "LoRA/QLoRA or quantization artifact with dataset card, evaluation comparison, and serving handoff note.",
    "securityEvidence": "Dataset provenance, PII/privacy review, model/license note, and safe adapter-release checklist.",
    "capstoneDeliverables": "Adapter or quantized model package, evaluation report, model card, serving notes, and reproducibility instructions."
  },
  "300": {
    "boundary": "Focuses on agent infrastructure, APIs, tool security, and MCP integration, not general prompt-writing or chatbot use.",
    "assessmentArtifact": "API-backed CLI or service with MCP-facing tool surface, structured outputs, and observability traces.",
    "securityEvidence": "Tool allowlist, authentication, human approval boundary, secrets handling, and misuse test notes.",
    "capstoneDeliverables": "Repository, MCP/server documentation, demo transcript, security review, traces/logs, and runbook."
  },
  "301": {
    "boundary": "Focuses on retrieval infrastructure, evaluation, and LLMOps; it is not a general database administration or analytics course.",
    "assessmentArtifact": "RAG system with ingestion plan, golden evaluation set, retrieval metrics, traces, and dashboard evidence.",
    "securityEvidence": "Data boundary, PII/privacy controls, retrieval-failure analysis, prompt-injection notes, and access policy.",
    "capstoneDeliverables": "Hosted demo, ingestion plan, evaluation report, traces/logs, dashboard, security boundary, and operational runbook."
  },
  "302": {
    "boundary": "Focuses on AI security, guardrails, governance, and GPU FinOps, complementing rather than duplicating cybersecurity programs.",
    "assessmentArtifact": "Threat model, guardrail test, governance mapping, cost/right-sizing memo, and remediation plan.",
    "securityEvidence": "OWASP LLM Top 10 mapping, prompt-injection test, secrets/access review, model provenance, and incident response note.",
    "capstoneDeliverables": "Governance memo, security scan or red-team report, cost model, accessibility note, and executive-ready risk summary."
  },
  "303": {
    "boundary": "Culminating integration course; students prove they can operate, secure, observe, document, and explain a complete AI infrastructure system.",
    "assessmentArtifact": "Complete production-grade AI system portfolio mapped to program learning outcomes and reviewed against the shared rubric.",
    "securityEvidence": "Full pipeline/security evidence, including scan results, mitigations, access controls, governance note, and incident response path.",
    "capstoneDeliverables": "Public or reviewable repo, CI/CD logs, deployment notes, security scan report, architecture diagram, cost estimate, accessibility note, runbook, and recorded demo.",
    "vendorOption": "Capstones may specialize in AWS, Azure, or GCP, but every required outcome must have a local/no-cost fallback."
  },
}

def prereq(code):
    return "none" if code == "100" else ORDER[ORDER.index(code)-1]
def nxt(code):
    i = ORDER.index(code); return ORDER[i+1] if i+1 < len(ORDER) else None
raw = {c: json.loads(pathlib.Path(f"site/data/_raw/{c}.json").read_text()) for c in ORDER}
courses = []
for c in ORDER:
    r = raw[c]
    courses.append({
        "code": c, "title": r["title"], "subtitle": r["subtitle"], "semester": SEM[c],
        "hours": 54, "unitEquivalent": 3, "prereq": prereq(c), "next": nxt(c),
        "description": r["description"], "objectives": r["objectives"], "slos": r["slos"],
        "weeks": r["weeks"],            # [{n,title,summary}] — summaries added in Step 3/here
        "midtermWeek": 8, "capstoneWeek": 16,
        "tools": r["tools"], "socs": SOCS[c], "foundryProjects": FOUNDRY_PROJECTS.get(c, []),
        "requisiteText": REQUISITES[c], "directEvidence": DIRECT_EVIDENCE[c],
        "courseControls": COURSE_CONTROLS[c],
        "canvasExportNote": CANVAS_EXPORT_NOTES.get(c, ""),
    })
program = {
  "name":"AI Infrastructure and Architecture",
  "credential":"Certificate of Completion — non-credit (CDCP)",
  "stats":{"courses":10,"contactHours":540,"unitEquivalent":30,"semesters":3,"weeksPerCourse":16,"hoursPerCourse":54},
  "overview": (
    "The AI Infrastructure and Architecture certificate is a 10-course, 540-contact-hour "
    "noncredit sequence (a 30-unit credit equivalent) that takes learners from foundational "
    "AI infrastructure concepts into practical local systems work before moving into "
    "containerized deployment, cloud platforms, production inference serving, model adaptation, "
    "agentic systems, retrieval-augmented generation, and AI security and governance."
    " Each 16-week, 54-hour course pairs lecture with hands-on labs using free and open-source "
    "tools, cloud free tiers, and institution-managed AI Foundry resources for advanced projects, "
    "so no personal paid software or hardware is required to complete the program. Every course "
    "ends in a midterm assessment in week 8 and a capstone project in "
    "week 16, culminating in a final, portfolio-ready capstone course that integrates serving, "
    "evaluation, and governance into one production-grade artifact."
  ),
  "pathway": (
    "The certificate is organized as three stackable semesters — Foundations, Deployment and "
    "Orchestration, and Applied Production Systems — so a learner can exit after any semester "
    "with a coherent, résumé-ready set of skills, or continue straight through to the full "
    "credential. As a noncredit Chancellor's-Office-recognized CDCP (Credit for Prior Learning-"
    "eligible, enhanced-funding) certificate, the program is designed to articulate toward "
    "credit coursework, giving graduates a stackable, non-credit-to-credit on-ramp into an "
    "associate degree or transfer pathway without repeating material they've already mastered."
  ),
  "careersNarrative": (
    "California labor-market data show the occupations this certificate targets among the "
    "fastest-growing in the state: Data Scientists (+37.1%) and Computer & Information "
    "Research Scientists (+26.1%) are projected to grow far faster than the statewide "
    "all-occupations baseline of 8.8%, and Software Developers — the largest target occupation "
    "at 290,800 workers — is projected to add over 200,000 openings through 2034. AI is "
    "simultaneously displacing routine technical roles (Network & Computer Systems "
    "Administrators is the one target occupation in decline) and creating new demand for "
    "workers who can build, deploy, and govern AI systems — precisely the retraining path this "
    "certificate provides."
  ),
  "foundry": {
    "headline": "An AI Foundry turns classroom labs into shared production infrastructure.",
    "summary": (
      "The curriculum remains platform-agnostic, but advanced courses are designed for an "
      "institution-managed AI Foundry: shared GPU compute, persistent project VMs, model-serving "
      "endpoints, notebooks, vector databases, experiment tracking, observability, and faculty "
      "controls. The strongest education case is predictable shared capacity for whole cohorts, "
      "so students can build real systems without personal cloud billing."
    ),
    "cards": [
      {
        "title": "Shared Compute Profiles",
        "body": "Assignments use generic profiles such as one, two, four, or eight-plus 80GB data-center GPUs. Students justify requests by model size, VRAM, concurrency, storage, latency, and whether the task is training, inference, RAG, or voice/agent hosting."
      },
      {
        "title": "Foundry-Required Projects",
        "body": "Hosted inference, RAG chatbots with optional voice agents, custom LoRA/QLoRA adapters, secure agentic workflows, and GPU FinOps benchmarks require persistent services and measured runtime evidence."
      },
      {
        "title": "Academic Senate Rationale",
        "body": "Flat-fee or predictable shared capacity is easier to align with instruction than per-student metered accounts. It supports authentic experimentation while keeping governance, access, logs, and cost controls visible to faculty."
      }
    ]
  },
  "researchStudio": {
    "headline": "STEM + CS/CIS collaboration: students build infrastructure for research.",
    "summary": (
      "STEM students and faculty bring the scientific question, dataset meaning, and validation "
      "criteria. CS/CIS AIINFRA students build the data pipeline, GPU workspace, benchmark or "
      "training environment, monitoring, security boundary, cost model, and reproducibility package."
    ),
    "dataset": "The Well is a public collection of large spatiotemporal physics simulation datasets that can anchor realistic computational-science projects without invented toy data.",
    "projects": [
      "Physics simulation surrogate modeling on a manageable public dataset subset.",
      "Research data portal or dashboard for inspecting predictions, errors, and uncertainty.",
      "Reproducible benchmark comparing local CPU, shared GPU, and managed cloud execution.",
      "Scientific RAG assistant over papers, lab notes, dataset documentation, and benchmark results."
    ],
    "links": [
      {"label": "The Well documentation", "url": "https://polymathic-ai.org/the_well/"},
      {"label": "The Well repository", "url": "https://github.com/polymathicai/the_well"},
      {"label": "The Well paper", "url": "https://arxiv.org/abs/2412.00568"}
    ]
  },
  "semesters":[
    {"n":1,"theme":"Foundations","hours":162,"courses":ORDER[0:3]},
    {"n":2,"theme":"Deployment and Orchestration","hours":162,"courses":ORDER[3:6]},
    {"n":3,"theme":"Applied Production Systems","hours":216,"courses":ORDER[6:10]},
  ],
}
pathlib.Path("site/data/curriculum.json").write_text(
    json.dumps({"program":program,"courses":courses}, indent=2, ensure_ascii=False), encoding="utf-8")
print("wrote curriculum.json")
