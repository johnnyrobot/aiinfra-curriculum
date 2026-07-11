This addendum defines the platform-agnostic AI Foundry layer used across AIINFRA. It should be used in course materials without naming any vendor.

## Definition For Students

An AI Foundry is a shared instructional platform where students can build, train, serve, evaluate, monitor, and secure AI systems using institution-managed compute. It may include GPU VMs, notebooks, remote desktops, model-serving endpoints, vector databases, experiment tracking, dashboards, user/workshop management, and secure app hosting.

The foundry is not a single model API. It is the infrastructure environment around the model.

## Vendor-Neutral Compute Profiles

Use these generic profiles in assignments instead of vendor SKU names:

- Profile A - single 80GB data-center GPU, one head/compute node, suitable for small hosted services, single-model inference, and scheduled adapter training.
- Profile B - two 80GB data-center GPUs across head/compute resources, suitable for concurrent classes, heavier inference, or parallel project teams.
- Profile C - four 80GB data-center GPUs, suitable for multiple capstone teams, larger open models, and higher concurrency testing.
- Profile D - eight or more 80GB data-center GPUs, suitable for program-scale scheduling, multi-course pilots, and advanced distributed labs.

Students should justify the profile they request using workload evidence: model size, VRAM need, expected concurrency, latency SLA, storage requirement, and whether the task is training, inference, RAG, or voice/agent hosting.

## Required Student Evidence When Using A Foundry

Any foundry-backed assignment should require:

- Compute profile selected and why.
- Reproducible setup steps or infrastructure-as-code.
- Running endpoint, notebook, training job, or service log evidence.
- Resource-use evidence such as GPU memory, GPU utilization, job duration, throughput, or latency.
- Cost model comparing flat shared capacity to metered alternatives.
- Security boundary: user access, data source, secrets handling, and what is not exposed.
- Exportable artifact: repo, notebook, adapter, model card, runbook, dashboard screenshot, or eval report.

## Assignments That Require Or Strongly Benefit From A Foundry

- Hosted inference service: deploy an open model or model server on a shared GPU VM or cluster and expose an authenticated API.
- Hosted RAG chatbot: run a web app/API, vector database, embedding service, retrieval pipeline, and tracing dashboard in a persistent environment.
- Voice-enabled AI assistant: add realtime voice transport plus speech-to-text/text-to-speech services to a hosted chatbot.
- LoRA/QLoRA adapter training: train a task-specific adapter on institution-managed GPU time, evaluate it, and serve or package it.
- GPU FinOps benchmark: measure throughput, latency, and utilization, then compare flat-fee shared capacity against metered GPU or token pricing.
- Secure agentic workflow: host an agent with tools, retrieval, logs, guardrails, and human approval controls, then red-team it.
- Capstone deployment: submit a foundry evidence appendix with architecture, compute profile, logs, cost model, security controls, and reproducibility notes.

## Faculty Notes

Keep student-facing language platform agnostic. Say "AI Foundry," "shared GPU VM," "managed model-serving endpoint," "institution-hosted notebook," "vector database," "remote app," and "foundry dashboard" instead of naming products.

Named vendors may be discussed in procurement reports, instructor notes, or comparison appendices, but the graded curriculum should assess capability and reasoning, not familiarity with one vendor console.

## Suggested Rubric Addition

Foundry Infrastructure Evidence, 10 pts:

- 3 pts: correct compute profile and workload justification.
- 2 pts: reproducible setup or deployment steps.
- 2 pts: runtime evidence such as logs, endpoint output, utilization, latency, or training metrics.
- 2 pts: cost and right-sizing explanation.
- 1 pt: security/access boundary documented.

## Flagship Curriculum Projects To Add

These are new project specifications for the curriculum. They are not assumed to already exist in the current course pages.

1. Hosted chatbot with optional voice agent. Students deploy a persistent service on a shared AI Foundry VM or cluster. The stack should include a web app or API, model-serving endpoint, retrieval or vector storage layer, monitoring/log evidence, secure access boundaries, and an optional realtime voice path using speech-to-text and text-to-speech services.
2. Custom model adaptation or LoRA/QLoRA adapter. Students train or fine-tune a task-specific adapter using scheduled foundry GPU time, evaluate base-model versus adapted-model behavior, package the adapter or model artifact, and document the compute profile, training logs, model card, and deployment path.

Both projects should be treated as foundry-required because they depend on persistent services, GPU availability, shared cohort access, and evidence that cannot be produced reliably on student laptops alone.

## STEM Research Infrastructure Studio Track

This track adds an interdisciplinary collaboration model to the AI Foundry curriculum. CS/CIS students act as the AI infrastructure team for STEM students or faculty who bring a scientific question, dataset, and validation context.

**Student-facing framing:** Build the infrastructure that lets a research team use AI responsibly and reproducibly on scientific data.

**Role split:**

- STEM partner: research question, domain background, dataset meaning, scientific success criteria, and interpretation of results.
- CS/CIS AIINFRA team: compute profile, data pipeline, model or benchmark environment, storage, experiment tracking, monitoring, security boundary, cost model, and reproducible deployment.

**Suitable dataset sources:** public scientific simulation datasets, open lab datasets, campus-approved research data, or benchmark collections. The Well can be used as a reference example because it contains large spatiotemporal physics simulation datasets and exposes a PyTorch-oriented workflow.

**Foundry requirements:**

- Shared storage or dataset cache.
- Scheduled GPU access for benchmark or training runs.
- Reproducible Python environment and container image.
- Experiment tracking and evaluation outputs.
- Cost/right-sizing evidence.
- Research handoff package that a STEM collaborator can understand.

**Suggested deliverables:**

- Joint project charter with STEM and CS/CIS responsibilities.
- Data card covering source, license, size, fields, privacy, and scientific meaning.
- Baseline benchmark or model run.
- Infrastructure runbook and reproducibility package.
- Research-facing result summary written for non-infrastructure readers.
- Technical appendix covering compute, logs, performance, cost, and limitations.

This track should be optional at first, then expanded into a formal cross-listed or partner-project pathway if STEM faculty identify recurring datasets or research questions.
