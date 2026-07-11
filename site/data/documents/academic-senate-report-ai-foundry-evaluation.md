## Curriculum Status Note

The hosted chatbot/voice-agent project and custom adapter/fine-tuning project are proposed curriculum projects, not pre-existing assignments. The current curriculum already contains adjacent capstone and infrastructure topics where these projects fit; this report recommends adding the project specifications explicitly and marking them as foundry-required options.

## Approval-Readiness Note

The AI Foundry recommendation incorporates internal approval-evidence work while keeping public rationale focused on the governance, access, and assessment requirements reviewers need. The foundry is not proposed as a standalone technology purchase; it is proposed as shared instructional infrastructure governed by faculty workload commitments, accessibility and security signoff, student-cost controls, capstone assessment evidence, and employer/advisory validation. The curriculum should remain vendor-neutral, while procurement may compare named vendors against those public academic requirements.

## Executive Summary

The AIINFRA certificate already teaches the core technical skills needed for modern AI infrastructure: containers, GPU-aware orchestration, cloud platforms, production inference, model adaptation, agentic systems, RAG, LLMOps, security, governance, and capstone deployment. The remaining gap is not curricular relevance. The gap is shared, reliable, instructional AI infrastructure that lets whole classes build the same kind of systems they are studying.

An AI foundry should be understood as a teaching and production sandbox where faculty can provision GPU compute, shared workspaces, model-serving endpoints, fine-tuning jobs, RAG/vector services, notebooks, dashboards, and course-ready project environments without requiring each student to manage separate cloud accounts, credit cards, quota requests, or fragile local GPUs.

The strongest education-specific value proposition in the current vendor set is a flat-fee or predictable-capacity model with unlimited users. That model aligns better with community college instruction than per-token, per-seat, or per-hour pricing because faculty can design authentic labs without every assignment becoming a cost-management exercise. Metered hyperscaler AI services remain important for literacy and comparison, but they do not replace shared compute for hands-on infrastructure courses.

The Senate-facing condition is that the foundry must be implemented as an equitable instructional resource: no required student-paid cloud/GPU/API spend, clear alternative-access paths, signed security and accessibility review, faculty training time, quota controls, incident response, and capstone artifacts that can be reviewed by faculty and employers.

Recommendation: pilot an education-focused AI foundry for AIINFRA 200, 201, 301, 302, and 303, with a vendor-neutral curriculum abstraction called "AI Foundry". The curriculum should avoid requiring named products, but the procurement report can compare named vendors and platforms.

## What Counts As An AI Foundry

For this program, an AI foundry is not simply a chatbot API. It should provide:

- Shared GPU compute available to classes, cohorts, and project teams.
- Browser-accessible development environments such as notebooks, IDEs, remote desktops, or proxied web applications.
- Model-serving infrastructure for open-weight or institution-approved models.
- Fine-tuning or adapter-training workflows for supervised fine-tuning, LoRA/QLoRA, quantization, and evaluation.
- RAG infrastructure such as document ingestion, embedding, vector storage, and retrieval evaluation.
- Agent and tool integration support, including secure app endpoints and observability.
- Faculty/admin controls for users, workshops, resource quotas, dashboards, and cost visibility.
- Governance controls for FERPA, privacy, access boundaries, logs, and responsible AI review.
- Centralized quota, billing, and access controls so required assignments do not depend on personal student-paid cloud accounts.
- Accessibility documentation, VPAT or equivalent review evidence, and alternative-access workflows for students who cannot use a specific interface.
- Exportable learning evidence: repositories, CI/CD logs, deployment notes, security scan reports, architecture diagrams, runbooks, and recorded demos.

## Vendor Landscape

### Heidi AI

Heidi positions itself as an on-demand cloud supercomputer for education, research labs, and enterprises. Its public site describes multi-cloud infrastructure deployment, browser-accessible GPU computing, built-in frameworks, education/training support, analytics, team collaboration, remote desktop access, and enterprise security. Its course catalog currently presents a small public course surface, but the platform positioning is explicitly education-friendly.

The supplied IBM GPU reference sheet is important because it shows annual, unlimited-user configurations from 1x A100 80GB through 163x A100 80GB, with a head node plus compute nodes, workshops, content/library features, an adaptive software stack, and ParaTools/E4S components. For classroom planning, the exact vendor SKU matters less than the capacity model: one institutional platform can serve many learners without each learner incurring separate GPU bills.

Best fit for AIINFRA: classroom-scale access to notebooks, shared clusters, remote desktops, hosted project VMs, and a flat-fee procurement story.

Risks and checks before acquisition: confirm current SSO/LMS integration, data-use terms, audit logs, user provisioning, quota controls, public endpoint policy, uptime/SLA, content library ownership, exportability, accessibility of the learner interface, and whether training jobs and long-running services can be isolated per course/team.

### NVIDIA AI Enterprise / Enterprise AI Factory

NVIDIA AI Enterprise is a production AI software platform around supported microservices, frameworks, libraries, GPU orchestration, optimized model deployment, and enterprise support. NVIDIA's Enterprise AI Factory guidance emphasizes that AI factories require dense accelerators, high-speed networking, scale-out storage, power/cooling, dynamic capacity, and software such as NIM, NeMo, and Run:ai for inference, model lifecycle, and workload orchestration.

Best fit for AIINFRA: strong technical alignment with production inference, GPU orchestration, model serving, fine-tuning, and enterprise private AI patterns. Strong fit for AIINFRA 200, 201, 302, and 303 from an industry-reference perspective.

Limitations for education: it is more of a software/hardware architecture and enterprise platform than a turnkey classroom subscription. It generally assumes available GPU infrastructure, enterprise licensing, and IT operators.

### HPE Private Cloud AI / HPE AI Factory Solutions

HPE Private Cloud AI is positioned as a turnkey private AI stack for enterprise AI agents with unified control, governance, observability, data/model/tool integration, and lower-latency private operation. HPE describes use cases around governed data access, model/tool freedom, audit/compliance, private inference, RAG, and agentic workflows.

Best fit for AIINFRA: a strong example of private/sovereign AI infrastructure, especially for regulated data, predictable private capacity, and enterprise operations.

Limitations for education: likely heavier procurement and operations footprint than a classroom-first foundry. Best viewed as an enterprise private AI reference pattern unless the district wants a managed private cloud strategy.

### Microsoft Azure AI Foundry

Azure AI Foundry is positioned as a unified platform for building, grounding, governing, observing, and scaling AI apps and agents. The official page highlights a large model catalog, model customization, real-time routing, agents, MCP-style tool connections, observability, security, and governance.

Best fit for AIINFRA: strong model-catalog and enterprise-governance teaching value; useful for demonstrating managed agents, model routing, prompt/agent lifecycle, and identity-integrated governance.

Limitations for education: usage is typically metered through cloud consumption. Students can learn the platform, but course-scale GPU experiments can become quota- and budget-sensitive unless centrally controlled.

### Amazon Bedrock

Amazon Bedrock provides model access, agents, guardrails, customization, knowledge bases, monitoring/logging, and responsible AI controls without direct infrastructure management. It is strong for model API access, agent and guardrail labs, managed RAG, and AWS-integrated production apps.

Best fit for AIINFRA: managed foundation-model API literacy, agent and guardrail labs, cloud-native application integration, and comparison against self-hosted inference.

Limitations for education: it is not primarily a flat-fee shared GPU foundry. It is excellent for managed AI platform literacy, but less ideal as the only infrastructure for courses that need students to operate model servers, GPUs, and training jobs.

### Google Vertex AI / Gemini Enterprise Agent Platform

Google's current Vertex AI surface is presented through Gemini Enterprise Agent Platform, a developer platform for building, scaling, governing, and optimizing enterprise-grade agents. The page highlights Model Garden, custom training, model testing/customization/deployment, secure agent development, and fine-tuning/customization workflows.

Best fit for AIINFRA: strong for model garden discovery, custom training, agent development, and managed ML lifecycle.

Limitations for education: like the other hyperscalers, it is powerful but consumption-based. It is best taught as a managed AI platform category, not treated as the sole student compute substrate.

## Comparison Against Education Requirements

1. Predictable cost for cohorts: education-focused flat-fee/shared compute is strongest. Hyperscalers are strongest for elasticity but can be difficult to budget for authentic student experimentation.
2. Unlimited or broad user access: Heidi's referenced model is most aligned because the reference sheet and public marketplace language emphasize unlimited users. Enterprise private cloud options can support many users, but procurement is usually contract/capacity based rather than classroom-simple.
3. Hands-on GPU operations: private AI factory and education foundry options are strongest. API-only managed services abstract away too much of the infrastructure that AIINFRA students need to learn.
4. Fine-tuning/model adaptation: NVIDIA/HPE/private stacks and education foundries are strong when GPUs are available; hyperscalers are strong when the assignment is managed training rather than infrastructure operations.
5. Hosted services and voice/chatbot projects: foundry VM or cluster access is the clearest fit because students need persistent services, ports, TLS/reverse proxies, vector databases, model servers, and observability.
6. Governance and security: hyperscalers and enterprise private AI stacks have mature identity, compliance, and logging surfaces. Any education-focused foundry must be checked carefully for auditability, FERPA boundaries, SSO, and export controls.
7. Faculty usability: education foundry and turnkey private cloud are strongest if they provide course/workshop management. Raw cloud platforms require more faculty support labor.
8. Accessibility and instructional continuity: any selected platform must support documented accessibility review, accessible alternatives, exportable student work, and a plan for students who need asynchronous or lower-bandwidth access.
9. Assessment evidence: the platform should make it easy for students to produce reviewable artifacts, including logs, model cards, architecture diagrams, security findings, cost estimates, and reproducibility notes.

## Curriculum Fit And Required Foundry Assignments

The following existing assignments already justify shared foundry infrastructure:

- AIINFRA 200 final capstone: production inference serving system with GPU-backed model server, containerization, Kubernetes/GPU orchestration, monitoring, and cost/capacity plan.
- AIINFRA 201 final capstone: LoRA/QLoRA adapter training, evaluation, quantization, and serving. A shared GPU foundry lets students move beyond toy notebooks into realistic adapter training and comparison.
- AIINFRA 301 final capstone: production RAG/LLMOps system with vector database, tracing, golden dataset evaluation, dashboards, and incident-response thinking.
- AIINFRA 302 Week 13: GPU FinOps. A flat-fee-vs-metered compute analysis directly maps to procurement and operating-cost literacy.
- AIINFRA 303 Week 09 and Week 16: model-layer and full certificate capstone integration, including served models, adaptation, RAG, agents/MCP, observability, security, and FinOps.

New or strengthened foundry assignments added to the curriculum:

- Hosted inference service on shared GPU VM or cluster.
- Hosted RAG chatbot with optional realtime voice agent.
- Custom LoRA adapter training and deployment track.
- Flat-fee vs metered compute procurement memo.
- Capstone foundry evidence appendix documenting compute profile, logs, cost model, security boundaries, and reproducibility.

Foundry assignments should also produce portfolio evidence needed for Senate and employer review: public or reviewable repository, CI/CD logs, deployment notes, security scan report, architecture diagram, cost estimate, accessibility note, runbook, and recorded demo. These artifacts make the capstone legible to faculty reviewers, advisory members, and hiring managers without changing the core course sequence.

## Example Projects That Justify Acquisition

1. Fully hosted campus/domain chatbot with optional voice agent. Students deploy an end-to-end stack on a foundry VM: web app/API, model server, vector database, realtime voice service, speech-to-text/text-to-speech, observability, and public or authenticated routing. The prior Heidi handoff (an internal proof-of-concept campus chatbot deployment, documented separately and available to reviewers on request) demonstrates a realistic reference architecture using a VM, local LLM serving, Qdrant, Neo4j, LiveKit, STT/TTS, and campus-specific routing.
2. Custom model or LoRA adapter training. Students fine-tune a small or medium open model for structured outputs, document accessibility remediation, helpdesk routing, or domain-specific tone/format. The remedy-server work (an internal document-remediation adapter-training project, documented separately and available to reviewers on request) is a concrete alignment point: Qwen3-VL adapters, task-specific routing, and vLLM/PEFT serving patterns map directly to AIINFRA 201 and 303.
3. Multimodal document remediation assistant. Students build an accessibility assistant that audits PDFs or Office documents, generates alt text, detects reading-order problems, and routes tasks to specialized adapters.
4. Secure agentic workflow. Students host an agent with tools, retrieval, logs, guardrails, and human approval boundaries, then red-team it in AIINFRA 302.
5. GPU FinOps benchmark and procurement memo. Students compare a flat annual shared-compute profile to metered cloud/token/API pricing using measured throughput, latency, concurrency, and class-size assumptions.

## Interdisciplinary STEM + CS/CIS Collaboration Model

A second academic value proposition is cross-department collaboration. AIINFRA can serve as the infrastructure partner for STEM research projects: CS/CIS students design, deploy, monitor, secure, and document the compute environment, while STEM students and faculty define the scientific question, dataset, validation criteria, and research interpretation.

This model fits especially well with public scientific simulation datasets such as The Well, a large collection of spatiotemporal physics simulation datasets used for machine learning and computational science research. The Well is not just a sample dataset; it is large enough and domain-specific enough to require real infrastructure decisions around storage, data movement, GPU scheduling, benchmarking, reproducibility, and model evaluation.

Recommended interdisciplinary project pattern:

- STEM partner provides a research question, dataset context, expected scientific behavior, and validation constraints.
- CS/CIS AIINFRA team provides the foundry workspace, data pipeline, training or inference environment, experiment tracking, benchmark harness, cost/right-sizing analysis, security boundary, and reproducibility package.
- Both teams co-present results: STEM students explain scientific meaning and limitations; CS/CIS students explain infrastructure, compute, reliability, and deployment decisions.

Example projects:

- Physics simulation surrogate modeling using a subset of a public scientific simulation dataset.
- Climate, fluid dynamics, acoustic scattering, or biological-system benchmark pipeline using institution-managed GPU time.
- Research data portal or dashboard that lets STEM students inspect model predictions, errors, and uncertainty.
- Reproducible computational-science benchmark comparing local CPU, shared GPU, and managed cloud execution.
- Scientific RAG assistant over papers, lab notes, dataset documentation, and benchmark results.

This strengthens the academic case for an AI Foundry because the platform becomes shared research infrastructure, not only an instructional tool. It also creates portfolio-quality collaboration artifacts: research questions, data cards, benchmark results, model cards, runbooks, and reproducible containers.

## Recommended Pilot

Pilot a foundry with AIINFRA 200, 201, 301, 302, and 303 rather than the entire certificate at once.

Minimum pilot capacity should support:

- One always-on shared project VM or small cluster for hosted chatbot/RAG/voice services.
- Scheduled GPU windows for LoRA/QLoRA training labs.
- Faculty/admin controls for course cohorts and team workspaces.
- Student-accessible notebook or browser IDE workflows.
- Monitoring dashboards for GPU utilization, job status, cost/capacity, and usage by course/team.
- Exportable artifacts: repositories, adapters, logs, model cards, architecture diagrams, and runbooks.

Success measures:

- At least 80% of student teams can complete a hosted foundry project without personal cloud billing.
- At least two courses use foundry-dependent assignments in the first pilot term.
- Faculty can provision and reset student/team environments without vendor support for routine tasks.
- The platform can produce utilization and access logs sufficient for academic and IT review.
- Students produce portfolio artifacts that demonstrate real infrastructure operations, not only API consumption.

Launch gates before the pilot becomes a standing instructional requirement:

- Instructional costs are institution-funded or centrally controlled; optional paid services are clearly labeled and never required.
- IT/security, accessibility, and procurement owners sign off on privacy, FERPA, data-retention, public endpoint, incident-response, and vendor terms.
- Faculty receive paid upskilling time, release time or stipend support where needed, and documented bench-strength coverage so the pilot is not dependent on one instructor.
- Each required AWS, Azure, or GCP activity has a local/no-cost fallback that still meets the learning outcome.
- Advisory members review the capstone evidence standard and confirm that the artifacts read as credible workforce evidence.

## Decision Position

The AIINFRA curriculum can remain platform-agnostic while still requiring an AI foundry. The curriculum should describe capabilities, constraints, and deliverables without naming vendors. Procurement and senate review can compare named platforms.

A flat-fee unlimited-user foundry is especially attractive for education because it converts unpredictable student experimentation into a planned instructional resource. The academic case is strongest when the acquisition is tied to specific assignments that cannot be taught authentically with local laptops or one-off free tiers: hosted voice/RAG chatbots, GPU model serving, adapter training, fine-tuning evaluation, security red-teaming, and GPU FinOps.

Recommended Senate position: approve the foundry as a conditional instructional pilot tied to documented workload, accessibility, security, student-cost, assessment, maintenance, and employer-validation evidence, not as an unconditional procurement commitment.

## Sources

- [Heidi AI homepage](https://heidiai.io/)
- [Heidi course catalog](https://heidiai.io/courses)
- Heidi documentation: [quick-start guide](https://heidiai.io/docs/getting-started/quick-start) and [cluster CLI reference](https://heidiai.io/docs/cli/clusters)
- Reference sheet supplied for review: IBM-GPU-heidi-ai-pricelist_20260518.pdf, dated May 18, 2026.
- Internal reference: prior Heidi handoff package (campus chatbot proof-of-concept deployment notes; available to reviewers on request).
- Internal reference: remedy-server adapter-training project notes (document-remediation fine-tuning and serving; available to reviewers on request).
- [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/)
- [NVIDIA Enterprise AI Factory design guide](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-factory-white-paper/latest/ai-factory-overview.html)
- [HPE Private Cloud AI](https://www.hpe.com/us/en/private-cloud-ai.html)
- [HPE Private Cloud AI QuickSpecs](https://www.hpe.com/us/en/collaterals/collateral.a50009216enw.html)
- [Microsoft Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Google Gemini Enterprise Agent Platform / Vertex AI](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- [The Well documentation](https://polymathic-ai.org/the_well/)
- [The Well repository](https://github.com/polymathicai/the_well)
- [The Well paper](https://arxiv.org/abs/2412.00568)
