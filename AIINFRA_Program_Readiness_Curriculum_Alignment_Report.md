# AIINFRA Program Readiness and Curriculum Alignment Report

**Prepared for:** Academic Senate, curriculum, and workforce review
**Scope:** Regulatory/accreditation compliance, California labor-market justification, curriculum alignment, and Academic Senate readiness for a stackable AI Infrastructure & Architecture pathway: a noncredit CDCP Certificate of Completion plus a credit CTE Certificate of Achievement pathway.
**Evidence basis:** Research findings with adversarial verification verdicts. Claims marked *refuted* have been dropped or corrected; claims marked *uncertain* are hedged and collected in §7 for human verification.

> **Evidence note.** The initial automated CCCCO research pass returned unusable placeholder data (a search-tool auth failure), so **§2 was re-researched by hand against primary Chancellor's Office / Title 5 / Education Code sources on 2026-07-02** and is now verified — see references **[C1]–[C6]**. The ACCJC (§3), labor-market (§4), and industry/skills (§5–§6) sections rest on verified primary sources and are cited with confidence.

> **Academic Senate readiness update.** Internal approval-evidence materials were drafted to support this report and future local submission work. This public report summarizes the pieces reviewers need to see: credit and noncredit program narratives, COR addenda, an LMI/TOP/CIP/SOC crosswalk, faculty workload and upskilling commitments, security/accessibility/student-cost controls, assessment and capstone rubrics, employer-validation thresholds, and downstream templates for COCI, regional consortium, CDCP, and sustainability signoff.

---

## 1. Executive Summary

The AIINFRA certificate proposal has a strong foundation — Python/Git dev environments, containers/Kubernetes, cloud ML platforms, self-hosting, provider APIs, Model Context Protocol (MCP), and vector-DB/RAG workflows. To read as a current, approval-ready AI infrastructure program, it should emphasize the **2025–2026 production-agentic-systems stack** rather than a narrower "run models locally + basic RAG" view. The biggest technical risk is treating prototyping tools (Ollama, LM Studio, AnythingLLM/Open WebUI, N8N/Langflow/Flowise) as production infrastructure, while a course branded "AI Infrastructure and Architecture" is expected to cover high-throughput inference serving, GPU orchestration at scale, LLMOps observability, guardrails/security, and AI governance [10][12][15][19][20].

The program readiness work is best understood as two linked products: **curriculum alignment** and **approval readiness**. The earlier version of the curriculum treated the first-semester 100-series as parallel courses while also writing them as a prerequisite ladder. This revision resolves that contradiction by **consolidating the foundation tier**: the old intro and developer-environment courses were merged into AIINFRA 100 (AI Systems & Development Environments), and the old container-lab and cloud/CI/CD courses were merged into AIINFRA 101 (Applied Infrastructure & Containerization). The result is a cleaner 8-course sequence delivered two courses per semester over four semesters as a strictly linear prerequisite chain. The internal approval-evidence work supplies the missing governance layer: prerequisite ladder, course-boundary language, direct assessment evidence, workload commitments, employer-reviewed capstone standards, no-student-cost lab controls, and local-fill approval templates.

**Headline recommendations:**

1. **Adopt the stackable credential path.** Maintain the noncredit CDCP Certificate of Completion as the fast, no-cost access tier, and develop a credit CTE Certificate of Achievement pathway as the transcripted upper tier. Noncredit remains the fastest, lowest-friction way to ship and update a fast-moving AI curriculum, while the credit pathway gives students, employers, and the Senate a clearer long-term credential signal [5][22][23].
2. **Reframe the "local model" and "low-code" content as dev-only**, and add production serving (vLLM/TGI/TensorRT-LLM), GPU orchestration (GPU Operator, DRA, KAI Scheduler), and disaggregated inference (NVIDIA Dynamo) [15][16][17].
3. **Add the missing production competencies**: agent frameworks (code-first), LLMOps observability/eval, fine-tuning/quantization, modern multi-stage RAG with rerankers and evals, guardrails/security (OWASP LLM Top 10 2025), AI governance (NIST AI RMF / ISO 42001 / EU AI Act), and GPU FinOps [10][12][14][19][20][26].
4. **Expand MCP coverage** — it is *current and correctly placed*; MCP is now under the Linux Foundation's Agentic AI Foundation and is an industry standard, so deepen it (server-building, tool security) rather than replace it [11].
5. **Anchor SLOs, program review, and disaggregated completion/job-placement tracking from day one** to satisfy ACCJC Standard 2 and Eligibility Requirement 11 even though no ACCJC filing is required for a non-credit offering [6][7].
6. **Ground the labor-market justification** in verified EDD data: Data Scientists (+37.1%) and Computer & Information Research Scientists (+26.1%) are the fastest-growing target occupations statewide, Software Developers is the largest-employment and a top-5 bachelor's-level opening occupation, and Network/Systems Administrators is the lone decliner (−4.5%) — reinforcing a *retrain-toward-cloud/MLOps* thesis [1][2][3][8][9].
7. **Attach approval-ready governance evidence before launch.** The program should not advance as a full launch until local reviewers complete COCI/COR fields, TOP/SAM/CIP verification, CDCP domain verification, regional consortium endorsement where required, faculty funding and upskilling commitments, accessibility/security signoffs, student-cost controls, and employer-validation artifacts.

---

## 2. Regulatory & Compliance Update (CCCCO)

> **Verified section (re-researched 2026-07-02).** The items below are sourced to primary Chancellor's Office / Title 5 / Education Code references **[C1]–[C6]** listed in §9.

### 2.1 Governing handbook — PCAH 8th Edition (November 2019)

- The controlling reference for CCCCO curriculum/program approval is the **Program and Course Approval Handbook (PCAH), 8th Edition (November 2019)** — still the current edition as of mid-2026 [C1]. It is organized into **credit** and **noncredit** components and governs course/program submission, approval, chaptering, and maintenance. Build the program narrative and Course Outlines of Record (CORs) to the PCAH 8th-edition **noncredit** specifications.
- Approval flows **college curriculum committee → district governing board → CCCCO Curriculum & Instruction Unit** (Curriculum Inventory submission) [C1][C2]. Noncredit certificates are approved through this CCCCO noncredit process; they are **outside ACCJC substantive-change jurisdiction** (§3.3) [5] but **not** outside Title 5 / CCCCO approval — a separate, required track.

### 2.2 Noncredit certificate types & CDCP enhanced funding

Statutory/regulatory basis: **Ed Code §84760.5** (defines CDCP categories), **Ed Code §84750.5** (uniform FTES apportionment; **§84750.5(d)(4)(A)(i)** codifies CDCP funding at **credit parity**, enacted by **SB 860 (2014)**, effective 2015–16), and **Title 5 §55151** (CDCP program approval) [C3][C4].

- **Enhanced (credit-parity) funding** is available only for noncredit courses in **four instructional domains** — ESL, Elementary & Secondary Basic Skills, **Short-Term Vocational**, and **Workforce Preparation** — **and only when the courses are sequenced (≥2) into an approved certificate** [C3].
- **Certificate of Completion** = a course sequence leading to **improved employment** (short-term vocational / workforce prep). **← Correct classification for the AI Infrastructure certificate.**
- **Certificate of Competency** = a sequence that prepares students to **transition into credit coursework** (credit certificate, associate degree, or transfer) [C3].
- **Bottom line:** the 432-hour AI Infrastructure certificate — classified **Short-Term Vocational → Certificate of Completion** — is CDCP-eligible for enhanced (credit-parity) funding **once CCCCO-approved and documented as leading to improved employment with a demonstrated labor-market need** (which §4 supplies). This confirms and now properly sources the original proposal's funding premise. Enhanced funding is **not automatic** — it follows CCCCO approval of the certificate and its course sequence [C3][C4].

### 2.3 Course Outline of Record (COR) & Distance Education

- Each noncredit COR must meet **Title 5 §55002(c)** standards (objectives, content, methods of instruction and evaluation, SLOs) and the PCAH 8th-edition noncredit COR fields [C1]. The program already includes a **COR template** — align it to these fields.
- **Distance Education:** each course offered online needs a **DE addendum** (Title 5 §55200 et seq.), and instruction must meet the federal **Regular and Substantive Interaction (RSI)** standard (34 CFR 600.2) [4]. Note the separate ACCJC **50%-of-courses DE** substantive-change trigger in §3.3 [4][5].

### 2.4 Compliance checklist mapped to existing program sections

| Requirement | Governing source | Maps to program section | Status / action |
|---|---|---|---|
| PCAH-conformant non-credit program narrative | PCAH 8th Edition, Nov 2019 [C1] (verified 2026-07-02) | Overview, Requirements | Confirm non-credit fields in local submission |
| CDCP category mapping (short-term vocational / workforce prep) | Ed Code / Title 5 (verify) | Overview, Career Pathways | **Add explicit category justification** |
| Labor-market need documentation | CCCCO non-credit approval | Career Pathways, References | Use §4 EDD data |
| COR fields per PCAH non-credit template | PCAH | COR template | Verify field completeness |
| DE addendum + RSI per course | 34 CFR 600.2 (RSI) [4] | Implementation | Add DE addenda if online |
| SLOs + program review + disaggregated data | ACCJC Std 2 / ER 11 [6][7] | Evaluation (SLO/program review) | **Strengthen — §3** |
| Program discontinuance / teach-out | ACCJC Std 2, item 2viii [8-refs below] | Implementation | Add teach-out plan |
| Advisory committee / industry alignment | ACCJC 2.2 [6] | Implementation (advisory) | Confirm active advisory board |

### 2.5 Credential-structure analysis and recommendation

Three options were weighed:

| Option | Unit/hour implication | Approval path | Funding | Assessment |
|---|---|---|---|---|
| **A. Keep non-credit CDCP Certificate of Completion** (status quo) | 432 contact hours (108h × 4 = 8×54h), no units | CCCCO non-credit approval; **no ACCJC substantive-change** [5] | Enhanced CDCP FTES *if* category-eligible (verify) | Fastest to launch/update; lowest student barrier; best for rapidly-changing AI content |
| **B. Add a for-credit Certificate of Achievement** | Would require conversion to units (~16+ units triggers ACCJC review for credit) [refs below] | CCCCO credit approval **plus** ACCJC administrative approval if ≥16 units and significant resources [refs below] | Standard credit apportionment; transferability | Slower; heavier COR/curriculum-committee load; but confers transcripted, transferable credit |
| **C. Stackable non-credit → credit pathway** (recommended) | Keep 432h non-credit foundation; layer credit certificates on top | Non-credit now; phase in credit later | CDCP enhanced funding on the non-credit tier; credit apportionment on upper tiers | Matches Grossmont/De Anza precedents [22][23]; lowest-barrier entry with an achievement ceiling |

**Recommendation: Option C (stackable non-credit → credit).** Launch/maintain the current non-credit CDCP Certificate of Completion as the accessible entry tier (preserving the ACCJC non-credit exemption and enhanced CDCP funding, pending category verification), and **design the courses so they can later articulate into a for-credit Certificate of Achievement / AS**. This mirrors the two strongest verified CCC precedents:

- **Grossmont College** (Fall 2025) — first CCC Applied AI AS with a **noncredit → degree stack** (AI Fundamentals and AI Developer non-credit Certificates of Completion → Certificate of Achievement/AS, 32 units), including a dedicated *Applied AI in Cloud Computing* course [22].
- **De Anza College** (Fall 2026) — stackable no-cost non-credit foundational certificate → technical certificates (ML, deep learning, NLP, prompt engineering, AI agents) → AS in Applied AI; reported ~222-hour Applied AI Certificate of Completion [23] *(medium confidence — see §7)*.

**Credit-conversion thresholds to plan around (Title 5 §55070, as amended 2025)** [C5][C5a]: a credit **grouping of ≥16 semester units** of degree-applicable coursework **must** be Chancellor-approved and can **only** be titled **"Certificate of Achievement"** (transcriptable); only ≥16-unit certificates are **federal Title IV financial-aid eligible**. A district **may optionally** submit **8 to <16 semester units** for Certificate-of-Achievement approval. Sequences **<8 units** (or not submitted) are locally-approved certificates that **cannot** use the "Certificate of Achievement / Completion / Competency" titles or appear on the transcript, and a certificate **cannot** consist solely of basic-skills courses. *(The April 2025 §55070 revision refined wording — "grouping" vs "sequence," the intersegmental-GE definition — but kept these unit thresholds.)* Separately, **ACCJC** treats a new ≥16-unit credit certificate requiring significant institutional resources as an **Administrative Approval** substantive change; **non-credit tiers remain exempt throughout** [5].

### 2.6 Approval-evidence implementation of Option C

The approval-evidence work implements Option C as a **two-pathway structure** rather than a wholesale course rewrite:

- **Noncredit CDCP Certificate of Completion:** preserves the consolidated 432-hour, 8-course pathway as the lower-barrier workforce access route, with no student-paid cloud/GPU/API spend and CDCP domain justification to be verified in the local CCCCO submission.
- **Credit CTE Certificate of Achievement:** drafts a 24-unit planning narrative using the 8 AIINFRA courses as 3-unit equivalents, pending local hours-to-units verification, COR entry, and COCI review. Because 24 units exceeds the ≥16-unit thresholds in §2.5, this tier requires Chancellor's Office approval as a Certificate of Achievement, is federal Title IV financial-aid eligible once approved, and — if it requires significant institutional resources — triggers ACCJC Administrative Approval substantive-change review [5][C5][C5a].
- **Local approval evidence:** identifies the missing artifacts reviewers normally expect before launch: COCI field completion, curriculum committee and board approvals, TOP/SAM/CIP verification during the TOP-to-CIP transition, advisory minutes, regional consortium evidence where required, accessibility/security signoffs, faculty workload commitments, and student-cost controls.
- **Maintenance controls:** adds a one-year launch review, annual LMI refresh, biennial COR review, employer/advisory validation cycle, and a sunset/teach-out clause for tools or courses that become obsolete.

---

## 3. Accreditation (ACCJC)

### 3.1 The 2024 Standards touchpoints

The 2024 ACCJC Accreditation Standards (adopted June 2023; June 2025 edition) are organized into four standards: **Standard 1 (Institutional Mission and Effectiveness), Standard 2 (Student Success), Standard 3 (Infrastructure and Resources), Standard 4 (Governance and Decision-Making)** [6]. **Standard 2** governs instructional program design for this certificate:

- **2.1** — academic programs must be in fields of study consistent with the institution's mission, with appropriate breadth, depth, and expected learning outcomes (ER 3, ER 9, ER 12) [6].
- **2.2** — the institution, relying on faculty and other stakeholders, designs and delivers programs reflecting **relevant discipline and industry standards** (ER 3, 9, 11, 14) — directly supports justifying the AI curriculum against current industry practice (which §5–§6 supply) [6].
- **2.5** — scheduling must ensure certificate programs can be completed in the expected period of time (ER 9) [6].
- **2.9** — the institution conducts **systematic review and assessment** of program quality (ER 11, 14) — the program-review/SLO engine [6].
- **1.3** and required documentation **item 1v** — institution-set standards for **certificate completion** specifically, alongside course completion, degree/transfer, job placement, and licensure pass rates, reviewed via **meaningfully-disaggregated data** [6].

### 3.2 SLO / assessment obligations (ER 9 and ER 11)

**Eligibility Requirement 11** is the program-level SLO/assessment anchor: publish each program's expected SLOs and any program-specific achievement outcomes, and demonstrate through **regular, systematic assessment** that completers achieve them — including **review of meaningfully-disaggregated data to identify and close achievement gaps** [7]. **ER 9** requires programs of **sufficient content and length**, at appropriate rigor, culminating in identified outcomes [7].

**Action:** Even though a non-credit certificate triggers no ACCJC filing, the college must still (a) publish program SLOs, (b) run a program-review cycle, and (c) track completion and job-placement data disaggregated by student group, in the program's **Evaluation** section [6][7]. *(Caveat: ER 9/ER 11 documentation is framed around degree programs; applying it to a non-credit certificate is a reasonable inference but not named explicitly in the ERs — see §7.)*

### 3.2a Program assessment and Senate evidence package

The approval-evidence work turns the assessment recommendation into a reviewable evidence system. Each course receives one direct evidence artifact mapped to program learning outcomes, and the capstone rubric becomes the common standard for employer-readable performance evidence. The minimum assessment package should include:

- a PLO/SLO matrix spanning all 8 courses;
- one direct artifact per course, such as a Git repository, container build, cloud deployment, security scan, RAG evaluation report, MCP server, governance memo, or capstone portfolio;
- a shared rubric covering infrastructure correctness, security, observability, reproducibility, cost awareness, accessibility, and professional documentation;
- disaggregated course completion, certificate completion, capstone completion, and job/placement follow-up measures;
- an annual program-improvement memo that records what faculty changed in response to evidence.

### 3.3 Substantive-change implications

- **Non-credit programs are exempt from ACCJC's substantive-change process** — no notification, administrative approval, or committee review. This is confirmed verbatim in the Substantive Change Manual (May 2026), which lists "Non-credit courses and/or programs" as an exempt category [5]. *(Correction per verdict: the manual lists **five** exempt categories, not four; the load-bearing conclusion — non-credit triggers no substantive-change filing — holds [5].)*
- **Distance Education exception applies regardless:** if **50% or more of the courses** are delivered via distance/correspondence education, advance notice through the substantive-change process is still expected, and the **first course in a DE modality** requires Administrative Approval; federal **RSI** requirements apply [4][5]. This matters if the certificate is delivered substantially online.
- **Teach-out / program discontinuance:** ACCJC required-documentation **item 2viii** requires policies ensuring enrolled students can complete in a timely way if a program is eliminated [6]. Given how fast AI tooling changes, build a **teach-out plan** into the Implementation section for any future course sunset.
- The specific substantive-change *process timelines* (ALO inquiry form; 15-day notification acknowledgment; 30/90/180-day administrative-approval windows) are largely confirmed, **but the committee-approval payment deadline is internally inconsistent in ACCJC's own manual** (Section 2 prose says "within 2 weeks," the flowchart says "at least 30 days") — flagged in §7 [5].

---

## 4. Labor Market Justification (California)

**Data sources & vintage.** Figures below come from **EDD's OEWS wage file** (California-Statewide; **May 2024 employment estimates with wages escalated to Q1 2025 dollars**) and **EDD's Long-Term Occupational Employment Projections 2024–2034**, cross-referenced with the **2025 California Jobs Market Report** [1][2][3]. All eight occupation figures were verified exactly against source [verdicts: *confirmed*].

**BLS-API / OEWS data caveat.** (1) The bulk EDD OEWS CSV used here is **one release cycle behind** the live EDD OEWS page, which now shows May 2025 employment / Q1 2026 wages — so employment counts differ slightly between the OEWS survey file and the projections file (different release vintages); both are legitimate official EDD numbers and are cited separately [9]. (2) There is **no standalone SOC code** for "MLOps Engineer" or "AI Engineer"; those roles are absorbed into 15-1252, 15-2051, and 15-1299, and any role-specific demand figures come from **private vendors (Lightcast), not government statistics** — treat as directional only [13]. (3) The statewide **8.8% baseline** is on the 2023–2033 cycle while occupation growth rates are 2024–2034 — a minor cross-cycle comparison [8].

### 4.1 Per-occupation table (California statewide)

| SOC | Occupation | Base employment (2024, projections file) | Median annual wage | Mean annual wage (OEWS) | Projected growth 2024–34 | Total openings 2024–34 |
|---|---|---|---|---|---|---|
| 15-2051 | **Data Scientists** | 40,400 | $145,554 (proj) / $140,518 (OEWS) | $159,675 | **+37.1%** (fastest) → 55,400 | 40,180 [1] |
| 15-1221 | **Computer & Information Research Scientists** | 8,800 | $163,554 (proj) / $160,538 (OEWS) | $168,344 | **+26.1%** (2nd fastest) → 11,100 | 7,690 [1] |
| 15-1252 | **Software Developers** | 290,800 | $179,292 (proj) / $175,555 (OEWS) | $190,798 | **+18.4%** → 344,400 | 207,260 [1][2] |
| 11-3021 | **Computer & Information Systems Managers** | 96,800 | $221,952 (proj) / $215,259 (OEWS) | $237,025 | **+16.5%** → 112,800 | 82,270 [1] |
| 15-1241 | **Computer Network Architects** | 15,300 | $163,317 (proj) / $142,110 (OEWS) | $154,087 | **+11.8%** → 17,100 | 9,510 [1] |
| 15-1299 | **Computer Occupations, All Other** (catch-all for many AI/ML/MLOps roles) | 84,700 | $138,203 (proj) / $132,249 (OEWS) | $140,015 | **+11.1%** → 94,100 | 59,320 [1] |
| 15-1211 | **Computer Systems Analysts** | 62,000 | $131,295 (proj) / $131,129 (OEWS) | $136,553 | **+9.7%** → 68,000 | 41,500 [1] |
| 15-1244 | **Network & Computer Systems Administrators** | 26,900 | $109,420 (proj) / $109,518 (OEWS) | $117,612 | **−4.5%** (only decliner) → 25,700 | 11,510 [1] |

### 4.2 Demand narrative

- **The AI/ML-adjacent occupations are the fastest-growing.** Data Scientists (+37.1%) and Computer & Information Research Scientists (+26.1%) far outpace the statewide **8.8% all-occupations baseline** (2023–2033, >21 million jobs) [8]. Seven of the eight target occupations exceed that baseline [8].
- **Software Developers is both the largest and a flagged high-demand occupation.** At 290,800 base employment and +18.4% growth, it is one of EDD's named high-demand careers and ranks **#2 among all bachelor's-level occupations** by projected openings (222,110, 2023–2033 cycle; $175,555 median; 9,838 online job ads June 12–Aug 10 2025 via Lightcast/CalJOBS) [2][3].
- **The one decliner reinforces the retraining thesis.** Network & Computer Systems Administrators is the only shrinking target occupation (−4.5%), consistent with cloud automation and managed services absorbing traditional on-prem sysadmin work — a direct argument for **retraining toward cloud/MLOps-adjacent skills** rather than legacy administration [1].
- **AI is simultaneously displacing and creating tech roles.** EDD's 2025 report attributes part of recent high-tech job losses (Professional & Business Services −179,100; Information −105,100) to "the rapid increase in the integration of artificial intelligence-related cost-saving measures," citing AI-driven layoffs shrinking entry-level jobs [3]. This supports training workers toward **higher-value AI-building/AI-operating roles** rather than commoditized ones.
- **Emerging roles corroborate direction (low confidence).** Vendor data (Lightcast) shows generative-AI unique job postings rising from ~55 (Jan 2021) to nearly 10,000 (May 2025), with California/Bay Area a top concentration — directional support for an AI-infrastructure credential, not a primary justification figure [13].

---

## 5. Curriculum Design and Alignment

### 5.1 Course-by-course alignment rationale

**Semester 1 — Foundations**

| Course | Alignment stance | Required emphasis | Current tools & techniques |
|---|---|---|---|
| **AIINFRA 100 — AI Systems & Development Environments** (merges old 100 + 101) | Foundational | Prototype-vs-production framing; AI governance/ethics primer; Python, Git, Linux, reproducible environments, and modern packaging | Inference-serving landscape; OWASP LLM Top 10 2025 [19]; NIST AI RMF [20] at survey level; `uv`/modern packaging; Git/Jupyter; MLflow preview to foreshadow LLMOps [12] |
| **AIINFRA 101 — Applied Infrastructure & Containerization** (merges old 102 + 200) | Deployment core | Docker → Kubernetes → cloud → IaC → CI/CD: optimized/secure images, registries, image scanning, GPU containers, Kubernetes deployment/scaling, cloud platforms, IAM, secrets, quotas, cost controls | Docker/Compose/Kubernetes; NVIDIA Container Toolkit; Trivy-style scanning; AWS/Azure/GCP; GitHub Actions; Terraform; managed endpoints and FinOps awareness [17][21][26] |

**Semester 2 — Serving & Adaptation**

| Course | Alignment stance | Required emphasis | Current tools & techniques |
|---|---|---|---|
| **AIINFRA 200 — Production Inference Serving & GPU Orchestration** (= old 201) | Production core | High-throughput inference serving, GPU-aware scheduling, observability, and operations evidence | vLLM, TGI, TensorRT-LLM, KServe/Ray Serve/Triton, NVIDIA Dynamo, GPU Operator, DRA, MIG [15][16][17] |
| **AIINFRA 201 — Model Adaptation: Fine-Tuning & Quantization** (= old 202) | Production core | LoRA/QLoRA, quantization, evaluation, model cards, and serving handoff | PEFT/LoRA/QLoRA, DPO/GRPO awareness, GGUF/AWQ/GPTQ/FP8, evaluation comparisons [14][18] |

**Semester 3 — Applied Production Systems**

| Course | Alignment stance | Required emphasis | Current tools & techniques |
|---|---|---|---|
| **AIINFRA 300 — Agentic AI & MCP** | Applied core | Provider APIs, code-first agent frameworks, MCP server-building, and tool security | OpenAI/Claude/Bedrock/Vertex/OpenRouter; LangGraph/CrewAI/OpenAI Agents SDK/Pydantic AI; MCP; AGENTS.md/A2A awareness [10][11] |
| **AIINFRA 301 — Production RAG + LLMOps Observability/Evals** | Applied core | Vector-DB selection, hybrid retrieval, reranking, RAG evaluation, traces, and dashboards | Qdrant/Milvus/Weaviate/pgvector; HNSW/IVF; dense+sparse search; RAGAS/DeepEval; Langfuse/Phoenix [10][12][25] |

**Semester 4 — Security, Governance & Capstone**

| Course | Alignment stance | Required emphasis | Current tools & techniques |
|---|---|---|---|
| **AIINFRA 302 — AI Security, Guardrails & Governance (+ GPU FinOps)** | Applied core | OWASP LLM risks, guardrails, governance, security review, accessibility, and GPU FinOps | OWASP LLM Top 10; NeMo Guardrails/Llama Guard; NIST AI RMF; ISO/IEC 42001; EU AI Act; cost-per-1,000-request analysis [19][20][26] |
| **AIINFRA 303 — Capstone** | Integration | Production-grade artifact instrumented with observability, evaluation, security evidence, and governance | Repository, CI/CD logs, deployment notes, security scan, architecture diagram, cost estimate, accessibility note, runbook, and recorded demo |

### 5.2 Strengthened modules and competencies

1. **Agentic AI & Agent Frameworks (code-first)** — LangGraph (graph-based), CrewAI (role-based), OpenAI Agents SDK (handoff-based, released March 2025), Pydantic AI (2025 breakout); agent state/graph control flow, tool-calling, handoffs, human-in-the-loop interrupts/approvals, multi-agent orchestration. Teach the cost/efficiency lesson (LangGraph fastest on latency; CrewAI ~3× token footprint on simple flows). Fills the gap left by N8N/Langflow/Flowise, which are visual workflow tools, not production agent frameworks [10].
2. **LLMOps: Observability, Tracing & Evaluation** — Langfuse (MIT, self-hostable), Arize Phoenix (50+ faithfulness/relevance/toxicity/hallucination metrics), LangSmith, OpenTelemetry/OpenLLMetry, MLflow tracing; the CLEAR evaluation framework (Cost, Latency, Efficacy, Assurance, Reliability). Currently entirely missing [12].
3. **High-Performance Inference Serving & GPU Orchestration** — vLLM/SGLang/TensorRT-LLM/TGI; Ray Serve, Triton, KServe; continuous batching, PagedAttention/KV-cache, tensor/pipeline parallelism; GPU Operator, DRA, **KAI Scheduler** (gang/topology-aware scheduling), MIG, Slurm-on-K8s (Slinky), SkyPilot; NVIDIA Dynamo disaggregated serving. The **biggest technical gap** for a course branded "Infrastructure and Architecture" [15][16][17].
4. **Model Adaptation: Fine-Tuning & Quantization** — LoRA/QLoRA/PEFT, DPO (has displaced classic RLHF), emerging GRPO; quantization formats **GGUF/AWQ/GPTQ/FP8**, KV-cache quantization; the heuristic "a larger model at lower precision usually beats a smaller model at higher precision." Single-GPU adaptation is accessible to this exact community-college audience [14][18].
5. **Production RAG: Rerankers, GraphRAG & Evals** — hybrid search (dense+BM25), query rewriting, **cross-encoder rerankers**, GraphRAG, agentic RAG; mandatory evaluation with **RAGAS** and **DeepEval** (CI/CD quality gates). Replaces naive embed-and-retrieve [10].
6. **AI Security & Guardrails** — OWASP **LLM Top 10 (2025)**; NeMo Guardrails, **Llama Guard 4** (12B multimodal, released Apr 30 2025), LLM Guard/Rebuff/Prompt Guard, Presidio (PII); direct vs. indirect prompt injection. Currently missing; essential given the agentic focus [19].
7. **AI Governance & Compliance** — **NIST AI RMF** (methodology), **ISO/IEC 42001** (auditable AMS), **EU AI Act** (binding law; prohibited practices + AI literacy applied Feb 2 2025, GPAI obligations Aug 2 2025, most high-risk requirements Aug 2 2026). Increasingly an employer/hiring requirement [20].
8. **GPU FinOps** — cost per 1,000 requests (not per GPU-hour); spot/preemptible for batch; quantization + KV-cache savings; right-sizing; fractional GPUs/MIG. Ties together serving, quantization, and orchestration [26] *(some FinOps case-study figures are vendor-sourced — see §7)*.

### 5.3 Proposed program map (108h × 4 = 432h)

At **54 contact hours per course** (the Chancellor's-Office-recommended 18×3 standard) the consolidated **8-course** sequence totals **432 contact hours** — a **24-unit** credit-equivalent, delivered **two courses per semester across four semesters** (108h per semester). The foundation tier was consolidated by **merging** the old intro and developer-environment courses into **AIINFRA 100 (AI Systems & Development Environments)** and the old container-lab and cloud/CI/CD courses into **AIINFRA 101 (Applied Infrastructure & Containerization)**, yielding a cleaner sequence that still runs **54 hours per course**. This removes the first-semester prerequisite conflict outright: deep container/Kubernetes/cloud work now lives in **AIINFRA 101**, and production serving with GPU orchestration in **AIINFRA 200**. The chain is strictly linear (100 → 101 → 200 → 201 → 300 → 301 → 302 → 303).

- **Semester 1 — Foundations (108h):** 100 AI Systems & Development Environments · 101 Applied Infrastructure & Containerization
- **Semester 2 — Serving & Adaptation (108h):** 200 Production Inference Serving & GPU Orchestration · 201 Model Adaptation: Fine-Tuning & Quantization
- **Semester 3 — Applied Production Systems (108h):** 300 Agentic AI & MCP · 301 Production RAG + LLMOps Observability/Evals
- **Semester 4 — Security, Governance & Capstone (108h):** 302 AI Security, Guardrails & Governance (+ GPU FinOps) · 303 Capstone

### 5.4 COR/Senate addendum layer

The curriculum cleanup should happen mainly in the COR/addendum layer so the consolidated 8-course pathway stays coherent while the Senate-facing evidence becomes clearer:

- **Prerequisite ladder:** the chain is strictly linear — AIINFRA 100 is open entry; 101 requires 100; 200 requires 101-level container/cloud deployment readiness; 201 requires 200; 300 requires 201; 301 requires 300; 302 requires 301; and 303 (capstone) requires 302 or equivalent skills.
- **Course-boundary language:** each COR should state how AIINFRA differs from adjacent CIS, data science, cloud, and cybersecurity offerings. AIINFRA's focus is operating, securing, observing, and governing AI infrastructure, not general programming, general analytics, or a vendor certification bootcamp.
- **DevSecOps evidence:** 101 should require local systems troubleshooting, secrets hygiene, image scanning, CI/CD, cloud/IaC/secrets controls, and deployment evidence; 302 should require governance and security review; 303 should require full pipeline evidence, including security findings and mitigations.
- **Vendor-specialization options:** the capstone path can allow AWS, Azure, or GCP specialization, but every required outcome must also have a local/no-cost fallback so student access does not depend on personal cloud billing.
- **Visible direct assessment:** every course should name the artifact that proves student learning, and each artifact should map to the program PLOs and shared rubric.
- **Employer-readable capstone:** 303 should require a public or reviewable repository, CI/CD logs, deployment notes, security scan report, architecture diagram, cost estimate, accessibility note, runbook, and recorded demo.

---

## 6. In-Demand Skills & Certifications Alignment

Employer demand for **AI Infrastructure Engineer / MLOps / ML Platform / AI/ML Engineer** roles in California converges on a consistent stack. Two live California postings verify the direction: **Scale AI** (Model Serving Platform) requires Python/Go/Rust/C++, Docker/Kubernetes, AWS/GCP + Terraform, and LLM-serving know-how with vLLM/SGLang/TensorRT-LLM as nice-to-haves [24] *(salary/URL specifics flagged in §7)*; **Hashlist** requires production GenAI experience, **MCP servers and agentic AI architectures**, and CI/CD-integrated AI tooling [24].

| Ranked employer-demanded skill/cert [21][24] | Where it lives in the revised curriculum |
|---|---|
| 1. Python (+ Go/Rust/C++ for infra) | 100 (dev environments) |
| 2. Docker + Kubernetes | 101 (Docker → Kubernetes/deployment) → 200 (GPU-aware production serving) |
| 3. Cloud platforms (AWS/GCP/Azure) | 101 |
| 4. Infrastructure-as-code (Terraform) | 101 |
| 5. CI/CD (Jenkins, GitHub Actions, GitLab CI) | 101 (CI/CD-for-ML) |
| 6. PyTorch / TensorFlow | 201 (fine-tuning) |
| 7. MLOps/data platform (Databricks, MLflow, Delta Lake, PySpark) | 301 (LLMOps/observability) |
| 8. LLM/GenAI (LangChain, RAG, prompt/agentic, vLLM/SGLang/TensorRT-LLM, MCP) | 200, 300, 301 |
| 9. Monitoring/observability (Prometheus, Grafana) | 301 |
| 10. Certifications (CKA/CKAD; AWS ML Engineer-Associate; Google Cloud PMLE; Azure AI Engineer; Databricks Data/ML Associate) | Align 101 → CKA/CKAD and cloud ML certs; 101 builds the Linux/Docker foundation those certs assume [21] |

**Certification strategy.** Following the **Coastline College** model (AI-for-Cybersecurity AS with NSA CAE-C validation and CompTIA alignment) [22-analog], the certificate can map explicitly to **vendor-neutral Kubernetes certs (CKA/CKAD)** and **cloud ML certs** as preferred qualifications. Reported salary premiums are directional (industry compensation analysis, not government wage data): **CKA ~18–25%, CKS ~25–35%** [24] *(see §7 for the specific ML-postings-share figure)*.

**Statewide positioning.** The CCC **Vision 2030 AI Workplan (July 2025)** funds shared infrastructure (a **$10M initial + $12M scaling** Common Cloud Data Platform) and workforce MOUs with **Nvidia, Google, OpenAI, Microsoft, IBM, Intel and others**, but **does not prescribe a technical AI-infrastructure curriculum** — so a college proposing a specific AI-infrastructure/MLOps non-credit certificate is **filling a real gap the system has not centrally defined**, while aligning with the state's named priorities [27].

---

## 7. Risks & Human-Verification List

**A. CCCCO items — now verified (2026-07-02), with residual procedural confirmations**

1. **§2 was re-researched against primary sources** after the automated pass failed, and is no longer an open gap: PCAH **8th Edition (Nov 2019)** [C1]; CDCP basis Ed Code §84760.5 / §84750.5 + Title 5 §55151, credit-parity funding per SB 860 [C3][C4]; Certificate-of-Achievement thresholds Title 5 §55070 as amended 2025 [C5][C5a]; Vision 2030 stackable/CPL support [C6]. *[resolved]*
2. **CDCP eligibility classification is correct but approval is procedural.** The Short-Term Vocational → Certificate of Completion mapping is right, but enhanced funding still requires **CCCCO approval of the certificate + its course sequence**; confirm the local submission path with your college Curriculum Committee / Articulation Officer before asserting funding in the proposal. *[procedural]*
3. **COCI and COR fields require local entry and signoff.** Internal templates can draft the fields, but the college must enter current COR data directly in COCI, attach DE/accessibility language, verify TOP/SAM/CIP choices, and route the package through curriculum committee and board approval. *[procedural]*
4. **Regional and advisory evidence must be current.** Attach advisory minutes, employer validation, regional consortium documentation where required, and a local LMI memo that includes regional evidence, not only statewide EDD or national BLS data. *[procedural]*
5. **Student-cost, security, and accessibility controls require named owners.** Before launch, confirm no required student-paid cloud/GPU/API costs; assign IT/security/accessibility signoff owners; document privacy, FERPA, data-retention, procurement, and alternative-access controls. *[procedural]*

**B. ACCJC nuances to verify**

6. **Committee-approval payment deadline is internally inconsistent in ACCJC's own manual** ("2 weeks" in prose vs. "30 days" in the flowchart). Do not cite a single figure without checking the current manual [5]. *[uncertain]*
7. **"Category F" label** for the substantive-change category was not verifiable from the retrieved primary source; the manual does not use lettered categories. Do not cite "category F." *[uncertain]*
8. **ER 9 / ER 11 are degree-framed;** applying them to a non-credit certificate is a reasonable inference, not explicit text. Present as best practice, not a naming citation [7]. *[uncertain]*
9. **RSI citation set** (34 CFR 600.2; Standards 1.4/2.1/2.2/2.6/2.9/3.9) comes from a DE-policy PDF not independently re-retrieved; the RSI requirement itself is well-established [4]. *[uncertain]*

**C. Labor-market / skills figures to hedge**

10. **MLOps/AI-Engineer demand numbers are vendor-sourced (Lightcast), not government data** — directional only [13]. *[confirmed as low-confidence]*
11. **Scale AI posting:** technical requirements confirmed, but the cited salary band ($180K–$225K) matches a non-senior listing while a near-duplicate "Senior" listing shows $216,200–$270,250, and the LinkedIn URL digit may be mistyped. Verify exact posting/title/URL before quoting [24]. *[refuted as cited — corrected]*
12. **California ML-postings share:** cited as ~29% but at least one source shows 32%. Verify against the actual CompTIA report table before quoting precisely [24]. *[uncertain]*
13. **Certification salary premiums** are industry compensation analysis, not government wage data — label directional [24]. *[uncertain]*

**D. Curriculum-claim figures to soften**

14. **"~80% of RAG failures are retrieval, not generation"** — **corrected to ~73%**; the 80% figure applies to overall RAG *project* failure rate, a different metric. Use 73% [10]. *[refuted — corrected]*
15. **"60% of new 2026 RAG deployments include eval from day one (up from <30%)"** — single aggregator source; treat as unverified [10]. *[uncertain]*
16. **GPU FinOps case study ($39K→$16K/month) and "55–80% of AI GPU spend is inference"** — single vendor/marketing source; present as illustrative [26]. *[uncertain]*
17. **"Token consumption grows ~20x by 2030"** — closest verified figure is Goldman Sachs' 24× (2026→2030); adjust base year/figure before citing precisely [14/26-adjacent]. *[confirmed-with-adjustment]*
18. **"LoRA/QLoRA cover ~95% of production fine-tuning"** and **vector-DB scale thresholds** (e.g., "Qdrant 500K–50M vectors") are soft rules-of-thumb, not hard statistics [14][25]. *[confirmed-as-illustrative]*
19. **KAI Scheduler "de facto reference"** is promotional framing (CNCF Sandbox project); accurate underlying facts, soften the superlative [17]. *[confirmed-with-nuance]*

**E. Comparative/precedent claims to re-confirm**

20. **De Anza** (222h figure), **Coastline** (NSA CAE-C through 2030), **Chaffey/Bakersfield**, **MiraCosta/Saddleback** precedents were medium/low confidence or not independently re-fetched [22][23]. Confirm before citing specific hours/structures. *[uncertain]*
21. **CCC AI Consortium (cccaic.org)** was unreachable; member list/curriculum templates unverified — confirm via ASCCC/BACCC [22-analog]. *[low confidence]*

---

## 8. Implementation Groundwork

**Capstone project standard.** The **303 Capstone** should require a *production-grade, instrumented* artifact rather than a prototype: an agentic or RAG system that (a) serves a quantized model via vLLM/TGI, (b) is instrumented with LLMOps tracing (Langfuse/Phoenix) and an automated eval harness (RAGAS/DeepEval), (c) enforces at least one guardrail (NeMo Guardrails / Llama Guard) mapped to an OWASP LLM Top 10 risk, and (d) reports a FinOps metric (cost per 1,000 requests) [12][15][19][26]. Implementation work should draft the capstone rubric, define SLO-linked assessment tied to ER 11 [7], specify facility/GPU-access needs (the CCC Common Cloud Data Platform and NVIDIA/cloud MOUs are potential resources [27]), and require employer-readable evidence: repository, CI/CD logs, deployment notes, security scan, architecture diagram, cost estimate, accessibility note, runbook, and recorded demo. The foundry or cloud access model should be institution-funded or centrally controlled so capstone completion does not depend on personal student billing.

**Interactive web presentation.** The public program proposal (Overview, Requirements, Core Curriculum, COR template, Implementation, Evaluation, Career Pathways, References) is a strong candidate for an **interactive web artifact**: a stackable-pathway visualizer (non-credit → credit), a labor-market dashboard driven by the §4 EDD table, a course-alignment matrix (KEEP/UPDATE/REPLACE), and a skills-to-curriculum crosswalk. Implementation groundwork: confirm the canonical section list, freeze the verified data tables, and resolve the §7 verification items so the interactive version ships only confirmed claims.

---

## 9. References

1. [California Long-Term Occupational Employment Projections 2024–2034 (EDD CSV, `lt-occ-emp-2024-2034.csv`)](https://data.ca.gov/dataset/715d1324-ac02-4b11-b922-86bafa6eb80f/resource/274e273c-d18c-4d84-b8df-49b4d13c14ce/download/lt-occ-emp-2024-2034.csv)
2. [California OEWS Wage Data (EDD, `oews-2009-2025_original.csv`)](https://data.ca.gov/dataset/6411456b-594b-4b73-af57-ce8dd401f2e2/resource/aef4c53a-7e17-418c-acc1-d189e39b6caa/download/oews-2009-2025_original.csv)
3. [2025 California Jobs Market Report (EDD, DE 864 Rev. 3 8-25)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/2025_california_jobs_market_report.pdf)
4. [ACCJC Policy on Distance Education and on Correspondence Education, June 2025](https://accjc.org/wp-content/uploads/Policy-on-Distance-and-on-Correspondence-Education.pdf)
5. [ACCJC Substantive Change Manual, May 2026 Edition](https://accjc.org/wp-content/uploads/Substantive-Change-Manual.pdf)
6. [ACCJC 2024 Accreditation Standards (June 2025 edition)](https://accjc.org/wp-content/uploads/ACCJC-2024-Accreditation-Standards.pdf)
7. [ACCJC Eligibility Requirements for Accreditation, January 2024](https://accjc.org/wp-content/uploads/Eligibility-Requirements-for-Accreditation.pdf)
8. [EDD Employment Projections page (confirms 2024–2034 vintage)](https://labormarketinfo.edd.ca.gov/data/employment-projections.html)
9. [EDD OEWS Employment and Wage Statistics page](https://labormarketinfo.edd.ca.gov/data/oes-employment-and-wages.html)
10. [RAG in Production 2026: GraphRAG, Hybrid Retrieval, and Evals](https://ailearningguides.com/rag-production-patterns-2026/) · [Top 5 Reranking Models (MachineLearningMastery)](https://machinelearningmastery.com/top-5-reranking-models-to-improve-rag-results/)
11. [Donating the Model Context Protocol and establishing the Agentic AI Foundation (Anthropic)](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) · [Linux Foundation press release](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)
12. [Best LLM Observability Tools (Firecrawl)](https://www.firecrawl.dev/blog/best-llm-observability-tools) · [Top 5 LLM and Agent Observability Tools (MLflow)](https://mlflow.org/top-5-agent-observability-tools/)
13. [Lightcast: The Generative AI Job Market: 2025 Data Insights](https://lightcast.io/resources/blog/the-generative-ai-job-market-2025-data-insights)
14. [LLM Fine-Tuning Guide: LoRA, QLoRA, DPO, GRPO, RLHF (Future AGI)](https://futureagi.com/blog/llm-fine-tuning-guide-2025/)
15. [Comparing the Top 6 Inference Runtimes for LLM Serving in 2025 (MarkTechPost)](https://www.marktechpost.com/2025/11/07/comparing-the-top-6-inference-runtimes-for-llm-serving-in-2025/)
16. [Introducing NVIDIA Dynamo (NVIDIA)](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/)
17. [Kubernetes GPU Scheduling: DRA, KAI, MIG (TechPlained)](https://www.techplained.com/kubernetes-gpu-scheduling) · [Slurm-on-Kubernetes (NVIDIA)](https://developer.nvidia.com/blog/running-large-scale-gpu-workloads-on-kubernetes-with-slurm/)
18. [Quantization Techniques for AI Inference 2026: GGUF, AWQ, GPTQ, FP8 (Sesame Disk)](https://sesamedisk.com/quantization-techniques-ai-inference-2026/)
19. [OWASP Top 10 for LLM Applications 2025 (official)](https://genai.owasp.org/llm-top-10/)
20. [EU AI Act Implementation Timeline (official)](https://artificialintelligenceact.eu/implementation-timeline/) · [EU AI Act vs NIST AI RMF vs ISO/IEC 42001 (EC-Council)](https://www.eccouncil.org/cybersecurity-exchange/responsible-ai-governance/eu-ai-act-nist-ai-rmf-and-iso-iec-42001-a-plain-english-comparison/)
21. [AWS Certified ML Engineer – Associate](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) · [Google Cloud Professional ML Engineer](https://cloud.google.com/learn/certification/machine-learning-engineer) · [Databricks ML Associate](https://www.databricks.com/learn/certification/machine-learning-associate)
22. [Grossmont College Applied AI AS/Certificate (catalog)](https://catalog.gcccd.edu/grossmont/associate-degree-programs-certificates/stem/artificial-intelligence-as-cert-achievement/) · [Grossmont launch news](https://www.gcccd.edu/news/articles/2025/2025-11-06-applied-ai-at-grossmont.php) · [Foothill College AI Certificate](https://catalog.foothill.edu/degrees-certificates/artificial-intelligence/) · [Coastline AI for Cybersecurity AS](https://catalog.cccd.edu/coastline/pathways/computer-cyber-sciences/cybersecurity/ai-cybersecurity-as/)
23. [De Anza College Applied AI degree](https://www.deanza.edu/news/2026/applied-artificial-intelligence-degree-fall-2026.html) · [GovTech coverage](https://www.govtech.com/education/higher-ed/de-anza-college-launches-associate-degree-in-applied-ai)
24. [AI Infrastructure Engineer, Model Serving Platform (Scale AI)](https://www.linkedin.com/jobs/view/ai-infrastructure-engineer-model-serving-platform-at-scale-ai-4196120822) *(URL/salary to verify — §7)* · [AI Infrastructure Engineer (Hashlist)](https://www.linkedin.com/jobs/view/ai-infrastructure-engineer-at-hashlist-4422814745) · [CompTIA State of the Tech Workforce 2026](https://www.comptia.org/en-us/resources/research/state-of-the-tech-workforce-2026/) · [LinkedIn Jobs on the Rise 2026](https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-roles-us-linkedin-news-dlb1c)
25. [Best Vector Databases 2026 (Firecrawl)](https://www.firecrawl.dev/blog/best-vector-databases) · [pgvector vs Pinecone vs Qdrant vs Weaviate (Kalvium)](https://www.kalviumlabs.ai/blog/vector-databases-compared-pgvector-pinecone-qdrant-weaviate/)
26. [AI Inference Cost Economics in 2026: GPU FinOps Playbook (Spheron)](https://www.spheron.network/blog/ai-inference-cost-economics-2026/) *(vendor source — treat figures as illustrative, §7)* · [FinOps for AI (Flexera)](https://www.flexera.com/blog/finops/finops-for-ai-governing-the-unique-economics-of-intelligent-workloads/)
27. [California Community Colleges Vision 2030 Artificial Intelligence Workplan, July 2025](https://www.cccco.edu/-/media/CCCCO-Website/docs/vision2030/artificial-intelligence-workplan.pdf) · [CCCCO AI initiative](https://ai.cccco.edu/)

### CCCCO Primary Sources — §2 (hand-verified 2026-07-02)

- **[C1]** Program and Course Approval Handbook (PCAH), **8th Edition (Nov 2019)** — current edition; credit + noncredit components. https://www.cccco.edu/-/media/CCCCO-Website/docs/curriculum/program-course-approval-handbook-8th-edition.pdf
- **[C2]** CCCCO Curriculum & Instruction Unit (approval authority for 116 colleges). https://www.cccco.edu/About-Us/Chancellors-Office/Divisions/Educational-Services-and-Support/What-we-do/Curriculum-and-Instruction-Unit
- **[C3]** CCCCO Noncredit Curriculum & Instructional Programs — CDCP categories; Certificate of Completion vs Certificate of Competency; enhanced-funding rules. https://www.cccco.edu/About-Us/Chancellors-Office/Divisions/Educational-Services-and-Support/What-we-do/Curriculum-and-Instruction-Unit/Curriculum/Noncredit-Curriculum-and-Instructional-Programs
- **[C4]** ASCCC Noncredit Instruction / Adult Education Basics — Ed Code §84750.5 / §84760.5, Title 5 §55151, SB 860 (2014) credit-parity funding. https://www.asccc.org/sites/default/files/Noncredit_Instruction_Adult_Education_Basics.pdf
- **[C5]** Title 5 §55070 Credit Certificates (Cornell LII). https://www.law.cornell.edu/regulations/california/5-CCR-55070
- **[C5a]** CCCCO Final Revisions to Title 5 §55070 re Credit Certificates of Achievement (adopted 2025). https://www.cccco.edu/-/media/CCCCO-Website/docs/regulatory-action/final-reg-text-certificate-of-achievement-final-v2-4-25-a11y-002.pdf
- **[C6]** CCCCO Vision 2030: A Roadmap for California Community Colleges — mirrored credit/noncredit pathways; Credit for Prior Learning via the MAP (Mapping Articulated Pathways) Initiative. https://www.cccco.edu/About-Us/Vision-2030 · https://vision2030.cccco.edu/

---

## Appendix: Compiled Reference List

### A. CCCCO / Title 5 / Ed Code

1. [CCCCO Artificial Intelligence Workplan, July 2025](https://www.cccco.edu/-/media/CCCCO-Website/docs/vision2030/artificial-intelligence-workplan.pdf)
2. [CCCCO AI initiative overview](https://ai.cccco.edu/)
3. [California Community Colleges AI Consortium](http://cccaic.org/)

### B. ACCJC

4. [ACCJC 2024 Accreditation Standards (June 2025 edition, PDF)](https://accjc.org/wp-content/uploads/ACCJC-2024-Accreditation-Standards.pdf)
5. [ACCJC Adopts 2024 Accreditation Standards](https://accjc.org/announcement/accjc-adopts-2024-accreditation-standards/)
6. [ACCJC Substantive Change Manual, May 2026 Edition (PDF)](https://accjc.org/wp-content/uploads/Substantive-Change-Manual.pdf)
7. [ACCJC Policy on Substantive Change, January 2026 (PDF)](https://accjc.org/wp-content/uploads/Policy-on-Substantive-Change.pdf)
8. [ACCJC Policy on Distance Education and on Correspondence Education, June 2025 (PDF)](https://accjc.org/wp-content/uploads/Policy-on-Distance-and-on-Correspondence-Education.pdf)
9. [ACCJC Eligibility Requirements for Accreditation, January 2024 (PDF)](https://accjc.org/wp-content/uploads/Eligibility-Requirements-for-Accreditation.pdf)

### C. EDD / LMI / BLS / Projections / COE

10. [California OEWS wage data CSV (EDD)](https://data.ca.gov/dataset/6411456b-594b-4b73-af57-ce8dd401f2e2/resource/aef4c53a-7e17-418c-acc1-d189e39b6caa/download/oews-2009-2025_original.csv)
11. [California Long-Term Occupational Employment Projections 2024-2034 (EDD CSV)](https://data.ca.gov/dataset/715d1324-ac02-4b11-b922-86bafa6eb80f/resource/274e273c-d18c-4d84-b8df-49b4d13c14ce/download/lt-occ-emp-2024-2034.csv)
12. [2025 California Jobs Market Report (EDD, DE 864 Rev. 3 8-25)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/2025_california_jobs_market_report.pdf)
13. [EDD Employment Projections page](https://labormarketinfo.edd.ca.gov/data/employment-projections.html)
14. [EDD OEWS Employment and Wage Statistics page](https://labormarketinfo.edd.ca.gov/data/oes-employment-and-wages.html)
15. [Employment Projections - Labor Market Information - CA.gov](https://labormarketinfo.edd.ca.gov/data/employment-projections.html)
16. [EDD Labor Market Information Division - Home Page](https://labormarketinfo.edd.ca.gov/)
17. [Centers of Excellence for Labor Market Research -- Collections](https://coeccc.net/collections/)

### D. Industry Tools & Techniques

18. [Lightcast: The Generative AI Job Market: 2025 Data Insights](https://lightcast.io/resources/blog/the-generative-ai-job-market-2025-data-insights)
19. [Lightcast: Beyond the Buzz -- AI Skills Command 28% Salary Premium](https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23)
20. [The best AI agent frameworks (LangChain)](https://www.langchain.com/resources/ai-agent-frameworks)
21. [Best AI Agent Frameworks 2025: LangGraph, CrewAI, OpenAI, LlamaIndex, AutoGen (Maxim AI)](https://www.getmaxim.ai/articles/top-5-ai-agent-frameworks-in-2025-a-practical-guide-for-ai-builders/)
22. [Best Multi-Agent Frameworks 2026: LangGraph, CrewAI, OpenAI SDK](https://uvik.net/blog/agentic-ai-frameworks/)
23. [Donating the Model Context Protocol and establishing the Agentic AI Foundation (Anthropic)](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
24. [Linux Foundation Announces the Formation of the Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)
25. [Best LLM Observability Tools (Firecrawl)](https://www.firecrawl.dev/blog/best-llm-observability-tools)
26. [Top 5 LLM and Agent Observability Tools (MLflow)](https://mlflow.org/top-5-agent-observability-tools/)
27. [Best AI Agent Observability Tools 2026 (Latitude)](https://latitude.so/blog/best-ai-agent-observability-tools-2026-comparison)
28. [Comparing the Top 6 Inference Runtimes for LLM Serving in 2025 (MarkTechPost)](https://www.marktechpost.com/2025/11/07/comparing-the-top-6-inference-runtimes-for-llm-serving-in-2025/)
29. [vLLM vs TensorRT-LLM vs HF TGI vs LMDeploy — Technical Comparison (MarkTechPost)](https://www.marktechpost.com/2025/11/19/vllm-vs-tensorrt-llm-vs-hf-tgi-vs-lmdeploy-a-deep-technical-comparison-for-production-llm-inference/)
30. [Introducing NVIDIA Dynamo, a Low-Latency Distributed Inference Framework (NVIDIA)](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/)
31. [Kubernetes GPU Scheduling: DRA, KAI, MIG (TechPlained)](https://www.techplained.com/kubernetes-gpu-scheduling)
32. [Running Large-Scale GPU Workloads on Kubernetes with Slurm (NVIDIA)](https://developer.nvidia.com/blog/running-large-scale-gpu-workloads-on-kubernetes-with-slurm/)
33. [SkyPilot (GitHub)](https://github.com/skypilot-org/skypilot)
34. [LLM Fine-Tuning Guide: LoRA, QLoRA, DPO, GRPO, RLHF (Future AGI)](https://futureagi.com/blog/llm-fine-tuning-guide-2025/)
35. [The ML Practitioner's Guide to Fine-Tuning Language Models (MachineLearningMastery)](https://machinelearningmastery.com/the-machine-learning-practitioners-guide-to-fine-tuning-language-models/)
36. [Quantization Techniques for AI Inference 2026: GGUF, AWQ, GPTQ, FP8 (Sesame Disk)](https://sesamedisk.com/quantization-techniques-ai-inference-2026/)
37. [LLM Quantization: GPTQ, AWQ, and GGUF for Efficient Deployment (Calmops)](https://calmops.com/algorithms/llm-quantization-gptq-awq-gguf/)
38. [RAG in Production 2026: GraphRAG, Hybrid Retrieval, and Evals](https://ailearningguides.com/rag-production-patterns-2026/)
39. [Top 5 Reranking Models to Improve RAG Results (MachineLearningMastery)](https://machinelearningmastery.com/top-5-reranking-models-to-improve-rag-results/)
40. [RAG Techniques Compared: Best Practices Guide (Starmorph)](https://blog.starmorph.com/blog/rag-techniques-compared-best-practices-guide)
41. [OWASP Top 10 for LLM Applications 2025 (official)](https://genai.owasp.org/llm-top-10/)
42. [LLM Guardrails: Production Safety Layers Reference 2026 (Digital Applied)](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-reference-2026)
43. [LLM Guardrails: Best Practices (Datadog)](https://www.datadoghq.com/blog/llm-guardrails-best-practices/)
44. [EU AI Act Implementation Timeline (official EU AI Act portal)](https://artificialintelligenceact.eu/implementation-timeline/)
45. [EU AI Act vs NIST AI RMF vs ISO/IEC 42001: A Plain English Comparison (EC-Council)](https://www.eccouncil.org/cybersecurity-exchange/responsible-ai-governance/eu-ai-act-nist-ai-rmf-and-iso-iec-42001-a-plain-english-comparison/)
46. [ISO/IEC 42001 and EU AI Act: A Practical Pairing (ISACA)](https://www.isaca.org/resources/news-and-trends/industry-news/2025/isoiec-42001-and-eu-ai-act-a-practical-pairing-for-ai-governance)
47. [Best Vector Databases 2026: A Complete Comparison Guide (Firecrawl)](https://www.firecrawl.dev/blog/best-vector-databases)
48. [pgvector vs Pinecone vs Qdrant vs Weaviate (2026): Which We Use in Production (Kalvium)](https://www.kalviumlabs.ai/blog/vector-databases-compared-pgvector-pinecone-qdrant-weaviate/)
49. [AI Inference Cost Economics in 2026: GPU FinOps Playbook (Spheron)](https://www.spheron.network/blog/ai-inference-cost-economics-2026/)
50. [FinOps for AI: Governing the Unique Economics of Intelligent Workloads (Flexera)](https://www.flexera.com/blog/finops/finops-for-ai-governing-the-unique-economics-of-intelligent-workloads/)

### E. Peer Programs & Job Market

51. [De Anza College Launches Silicon Valley's First Associate Degree in Applied Artificial Intelligence](https://www.deanza.edu/news/2026/applied-artificial-intelligence-degree-fall-2026.html)
52. [Silicon Valley to get its first two-year degree focused on AI – The Press Democrat](https://www.pressdemocrat.com/2026/05/22/silicon-valley-to-get-its-first-two-year-degree-focused-on-ai/)
53. [De Anza College Launches Associate Degree in Applied AI](https://www.govtech.com/education/higher-ed/de-anza-college-launches-associate-degree-in-applied-ai)
54. [Applied Artificial Intelligence Associate in Science and Certificate of Achievement | Grossmont-Cuyamaca CCD Catalog](https://catalog.gcccd.edu/grossmont/associate-degree-programs-certificates/stem/artificial-intelligence-as-cert-achievement/)
55. [Grossmont College launches first of its kind, Applied Artificial Intelligence Associate Science degree](https://www.gcccd.edu/news/articles/2025/2025-11-06-applied-ai-at-grossmont.php)
56. [Artificial Intelligence - Academic Catalog - Foothill College](https://catalog.foothill.edu/degrees-certificates/artificial-intelligence/)
57. [AI for Cybersecurity, Associate of Science Degree < Coastline College](https://catalog.cccd.edu/coastline/pathways/computer-cyber-sciences/cybersecurity/ai-cybersecurity-as/)
58. [Press Release: Coastline College's AI for Cybersecurity Program Earns NSA Validation Through 2030](https://blog.coastline.edu/2025/09/nsa-validates-cyber-ai-program.html)
59. [Chaffey College to Launch Four New Computer Technology Programs](https://www.prnewswire.com/news-releases/chaffey-college-to-launch-four-new-computer-technology-programs-302745244.html)
60. [BC Offering Free Media Literacy Certificate Program](https://www.kccd.edu/news/2024/0814-bc-offering-free-media-literacy-certificate-program.html)
61. [Associate in Science in Artificial Intelligence - Academic Map | MiraCosta](https://surf.miracosta.edu/psc/ps/EMPLOYEE/SA/c/MCC_CUSTOM.MZ_ACAD_MAP_SS.GBL?MAP_ID=1216)
62. [Artificial Intelligence and Machine Learning Suite | MiraCosta College in partnership with ed2go](https://www.ed2go.com/miracosta/online-courses/artificial-intelligence-machine-learning-suite/)
63. [Introduction to Artificial Intelligence | Saddleback College](https://www.ed2go.com/saddleback/online-courses/introduction-to-artificial-intelligence/)
64. [AI - Bay Area Community College Consortium](https://baccc.net/ai/)
65. [AIDA - Bay Area Community College Consortium](https://baccc.net/aida/)
66. [AI Infrastructure Engineer, Model Serving Platform | Scale AI](https://www.linkedin.com/jobs/view/ai-infrastructure-engineer-model-serving-platform-at-scale-ai-4196120822)
67. [AI Infrastructure Engineer at Hashlist (San Francisco, CA)](https://www.linkedin.com/jobs/view/ai-infrastructure-engineer-at-hashlist-4422814745)
68. [State of the Tech Workforce 2026 | CompTIA Research](https://www.comptia.org/en-us/resources/research/state-of-the-tech-workforce-2026/)
69. [Key employment metrics, market insights and the impact of AI revealed in CompTIA State of Tech Workforce 2026 report](https://www.comptia.org/en-us/about-us/news/press-releases/key-employment-metrics-market-insights-and-the-impact-of-ai-revealed-in-comptia-state-of-tech-workforce-2026-report/)
70. [LinkedIn Jobs on the Rise 2026: The 25 fastest-growing roles in the U.S.](https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-roles-us-linkedin-news-dlb1c)
71. [AWS Certified Machine Learning Engineer – Associate](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/)
72. [Professional ML Engineer Certification | Google Cloud](https://cloud.google.com/learn/certification/machine-learning-engineer)
73. [Databricks Certified Machine Learning Associate](https://www.databricks.com/learn/certification/machine-learning-associate)
