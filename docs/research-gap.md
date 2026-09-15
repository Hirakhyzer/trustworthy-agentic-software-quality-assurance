# Research Gap and PhD Positioning

## Purpose

This document defines the current PhD-level research gap, research questions, testable hypotheses, and expected contributions for **Trustworthy Agentic Software Quality Assurance**.

It should be treated as a **working research-positioning document**. The gap statements are intentionally formulated so they can be validated, refined, or rejected through a systematic literature review rather than assumed to be universally established facts.

---

## Research Context

Software quality assurance (SQA) is increasingly performed in continuous-delivery settings where requirements, code, tests, dependencies, defects, and operational evidence change rapidly. Existing automation is strong at deterministic checks such as test execution, linting, static analysis, coverage measurement, and policy enforcement.

Recent AI-assisted software engineering introduces a different class of systems: autonomous or semi-autonomous agents that can inspect heterogeneous evidence, reason across multiple quality concerns, coordinate tasks, recommend actions, and potentially influence release decisions.

The research challenge is therefore no longer only:

> Can AI detect software-quality problems?

A stronger question is:

> **Can agentic AI participate in continuous software quality assurance in a way that is empirically effective, evidence-grounded, reproducible, calibrated, auditable, and appropriately governed by humans?**

This project studies that stronger question.

---

## Working Research Gap

### Gap G1 — Quality evaluation is often task-local rather than assurance-system-level

Many AI-for-software-engineering evaluations focus on isolated tasks such as code generation, defect prediction, test generation, bug localization, or code review. These tasks are valuable, but continuous SQA requires evidence to be combined across requirements, implementation, testing, defect history, and release context.

**Research opportunity:** evaluate agentic AI as a coordinated assurance system rather than as a collection of independent software-engineering tasks.

### Gap G2 — Agent autonomy is rarely evaluated together with release authority

An agent may generate useful findings while still being unsafe to trust with a high-impact quality decision. Detection capability and decision authority are different properties.

**Research opportunity:** experimentally separate analysis, recommendation, escalation, and approval authority, and measure when human approval gates improve outcomes.

### Gap G3 — Evidence traceability is weaker than recommendation evaluation

A correct recommendation is not sufficient for trustworthy SQA if reviewers cannot determine which observations support it. Agent outputs may mix factual evidence, inference, uncertainty, and recommendation in one narrative.

**Research opportunity:** require structured links between findings and observable quality evidence, then measure evidence completeness and unsupported-claim rates.

### Gap G4 — Confidence and software risk are often conflated

A high-risk software change can be assessed with high or low confidence. Similarly, a low-risk change can still be evaluated with weak evidence. Risk and epistemic confidence should not be treated as the same signal.

**Research opportunity:** model risk and confidence separately and study whether this separation improves escalation decisions and human trust calibration.

### Gap G5 — Multi-agent disagreement is under-specified as a quality signal

Specialized agents may disagree because they observe different evidence, use different criteria, or fail inconsistently. Treating disagreement only as an orchestration problem may discard useful uncertainty information.

**Research opportunity:** study inter-agent disagreement as a measurable signal for uncertainty, escalation, and quality-risk review.

### Gap G6 — Repeated-run reliability receives less attention than point accuracy

A stochastic agentic system can give a correct answer once and still be unsuitable for assurance if its recommendations vary materially across equivalent runs.

**Research opportunity:** treat decision stability, variance, and repeated-run agreement as first-class SQA metrics alongside precision, recall, and recommendation accuracy.

### Gap G7 — Human oversight is often described normatively rather than evaluated empirically

Human-in-the-loop designs are frequently recommended for trustworthy AI, but the placement, timing, and effectiveness of intervention points need empirical study.

**Research opportunity:** compare no-oversight, recommendation-only, risk-triggered approval, and confidence-triggered approval conditions using quality outcomes, reviewer workload, and override behavior.

### Gap G8 — Agent evolution introduces a new form of assurance drift

Model changes, prompts, tool configurations, thresholds, and orchestration policies can alter QA behavior even when the software under review is unchanged.

**Research opportunity:** evaluate assurance drift longitudinally and study whether agentic QA decisions remain reproducible across controlled system changes.

---

## Core PhD Research Question

> **How can agentic AI be designed and empirically evaluated to improve continuous software quality assurance while preserving evidence traceability, calibrated uncertainty, decision reliability, and meaningful human control?**

---

## Refined Research Questions

### RQ1 — Effectiveness

**To what extent does specialized multi-agent SQA improve detection and prioritization of software-quality risks compared with rule-based and single-agent baselines?**

Primary outcomes:

- precision;
- recall;
- F1 score;
- release recommendation accuracy;
- quality-risk ranking agreement.

### RQ2 — Evidence grounding

**Does requiring explicit evidence for every agent finding reduce unsupported quality claims and improve traceability of assurance decisions?**

Primary outcomes:

- unsupported finding rate;
- evidence completeness;
- evidence-to-finding traceability;
- reviewer verification success.

### RQ3 — Reliability and consistency

**How stable are agentic SQA findings and release recommendations across repeated runs, equivalent software changes, and controlled configuration changes?**

Primary outcomes:

- repeated-run agreement;
- recommendation variance;
- finding-set similarity;
- confidence variance;
- drift over time.

### RQ4 — Human oversight

**Which human-oversight policy best reduces harmful or incorrect high-impact recommendations without creating unnecessary review workload?**

Candidate conditions:

- no mandatory approval;
- approval for high-risk cases;
- approval for low-confidence cases;
- approval for either high risk or low confidence;
- human review of all release recommendations.

Primary outcomes:

- prevented incorrect approvals;
- escalation precision and recall;
- human override rate;
- review time;
- reviewer workload.

### RQ5 — Confidence calibration

**Does explicit confidence representation improve the calibration of both agent decisions and human reliance on those decisions?**

Primary outcomes:

- calibration error;
- confidence/accuracy alignment;
- appropriate reliance;
- over-reliance and under-reliance rates.

### RQ6 — Multi-agent coordination

**When does specialization improve software-quality assurance, and when does coordination overhead or disagreement reduce performance?**

Primary outcomes:

- inter-agent agreement;
- marginal contribution of each agent;
- ablation performance;
- coordination failure rate;
- decision latency.

### RQ7 — Assurance drift

**How do model, prompt, policy, and orchestration changes affect the reproducibility and trustworthiness of agentic SQA decisions over time?**

Primary outcomes:

- decision drift;
- evidence drift;
- confidence drift;
- regression frequency;
- rollback effectiveness.

---

## Testable Hypotheses

These hypotheses are deliberately falsifiable and should be tested against controlled benchmark scenarios and, where appropriate, human-subject studies.

### H1 — Multi-agent detection effectiveness

**H1:** Specialized multi-agent SQA will achieve higher recall for heterogeneous software-quality risks than a single-agent baseline while maintaining comparable precision.

**Null:** There is no meaningful improvement in recall, or the gain is offset by substantially lower precision.

### H2 — Evidence grounding

**H2:** Requiring structured evidence references for every quality finding will reduce the unsupported finding rate compared with free-form agent reasoning.

**Null:** Structured evidence requirements do not materially reduce unsupported findings.

### H3 — Human approval gates

**H3:** Risk- and confidence-triggered human approval gates will reduce incorrect autonomous release approvals in high-impact scenarios compared with an agent-only condition.

**Null:** Approval gates do not materially reduce incorrect release approvals.

### H4 — Confidence calibration

**H4:** Separating confidence from software-risk classification will improve escalation quality compared with a policy that uses risk score alone.

**Null:** Separate confidence representation provides no measurable escalation benefit.

### H5 — Trust calibration

**H5:** Reviewers shown explicit evidence and calibrated confidence will demonstrate more appropriate reliance on agentic SQA recommendations than reviewers shown recommendations without those signals.

**Null:** Evidence and confidence presentation do not improve appropriate reliance.

### H6 — Decision stability

**H6:** Evidence-constrained agentic SQA will produce higher repeated-run decision agreement than unconstrained free-form agentic SQA.

**Null:** Evidence constraints do not improve repeated-run stability.

### H7 — Value of specialization

**H7:** Removing specialized agents through ablation will produce measurable losses in the quality-risk categories primarily assigned to those agents.

**Null:** Specialized agents provide no distinct measurable contribution relative to a simpler architecture.

### H8 — Disagreement as uncertainty signal

**H8:** Higher inter-agent disagreement will be positively associated with incorrect recommendations or cases requiring human override.

**Null:** Inter-agent disagreement has no useful relationship with recommendation error or human intervention.

### H9 — Oversight cost trade-off

**H9:** Selective approval policies based on risk and confidence will achieve a better safety/workload trade-off than mandatory human review of every case.

**Null:** Selective oversight provides no advantage over full manual review or no mandatory review.

### H10 — Assurance drift

**H10:** Controlled changes to model, prompt, or orchestration configuration will cause measurable changes in recommendation stability, and explicit regression benchmarks will detect a substantial proportion of those changes.

**Null:** Configuration evolution produces no measurable assurance drift, or the proposed benchmark is unable to detect it.

---

## Hypothesis-to-Evidence Mapping

| Hypothesis | Independent variable | Key dependent variables | Suggested comparison |
|---|---|---|---|
| H1 | QA architecture | Precision, recall, F1 | Multi-agent vs single-agent |
| H2 | Evidence constraint | Unsupported finding rate, traceability | Structured vs free-form findings |
| H3 | Approval policy | Incorrect approvals, overrides | Agent-only vs human-gated |
| H4 | Confidence-aware escalation | Escalation precision/recall | Risk-only vs risk + confidence |
| H5 | Reviewer information | Appropriate reliance, workload | Recommendation-only vs evidence + confidence |
| H6 | Evidence constraint | Repeated-run agreement | Constrained vs unconstrained agentic SQA |
| H7 | Agent composition | Category-specific detection | Full model vs agent ablations |
| H8 | Inter-agent disagreement | Error/override probability | Agreement level analysis |
| H9 | Oversight policy | Prevented errors, review cost | Selective vs full review |
| H10 | Agent-system configuration | Decision/evidence drift | Baseline vs changed configurations |

---

## Expected PhD Contributions

### C1 — Conceptual contribution

A model of **agentic software quality assurance as an evidence-mediated decision system**, explicitly separating:

- observable software-quality evidence;
- agent findings;
- risk;
- confidence;
- disagreement;
- recommendation;
- human authority.

### C2 — Architectural contribution

A reference architecture for trustworthy agentic SQA with:

- specialized QA agents;
- transparent orchestration;
- evidence aggregation;
- uncertainty representation;
- escalation rules;
- human approval gates;
- auditable assurance decisions.

### C3 — Measurement contribution

A metric suite extending conventional detection metrics with agentic-assurance measures such as:

- unsupported finding rate;
- evidence completeness;
- repeated-run agreement;
- inter-agent disagreement;
- confidence calibration;
- human escalation precision/recall;
- human override rate;
- assurance drift.

### C4 — Benchmark contribution

A reproducible benchmark containing controlled software-quality scenarios with known ground truth across:

- requirement ambiguity;
- traceability gaps;
- complexity growth;
- test inadequacy;
- known defects;
- conflicting evidence;
- apparently safe changes;
- high-risk release situations.

### C5 — Empirical contribution

A comparative evaluation of:

1. deterministic rule-based SQA;
2. single-agent AI SQA;
3. specialized multi-agent SQA;
4. multi-agent SQA with human oversight.

The contribution is not merely identifying the best-performing condition, but explaining the circumstances under which each condition succeeds or fails.

### C6 — Human-centered contribution

Empirical evidence on where human intervention should occur in agentic QA workflows, including the trade-off between:

- risk reduction;
- review effort;
- automation bias;
- trust calibration;
- reviewer autonomy.

### C7 — Reproducibility contribution

A protocol for recording agent configurations, scenario versions, evidence, decisions, confidence, approvals, and repeated-run results so that agentic QA experiments can be audited and replicated.

### C8 — Assurance-drift contribution

A longitudinal evaluation method for detecting whether changes to models, prompts, policies, thresholds, or agent composition alter quality-assurance behavior unexpectedly.

---

## Claimed Novelty Boundary

The project should **not** claim novelty merely because it uses multiple AI agents for software engineering. Multi-agent software-engineering systems already form a broad research area.

The intended novelty should instead be tested around the combination of:

1. continuous SQA rather than isolated generation tasks;
2. evidence-first assurance decisions;
3. explicit separation of risk and confidence;
4. measurable inter-agent disagreement;
5. selective human authority over high-impact decisions;
6. repeated-run reliability as an assurance property;
7. longitudinal assurance-drift evaluation;
8. reproducible comparison against conventional and single-agent baselines.

A systematic literature review should determine which of these elements are genuinely novel, partially explored, or already well established.

---

## Research Program

A practical thesis progression could be organized as follows.

### Study 1 — Benchmark and baseline establishment

Build controlled software-quality scenarios and compare deterministic SQA with the initial agentic architecture.

### Study 2 — Evidence-grounded agentic QA

Test whether explicit evidence constraints improve correctness, traceability, and repeated-run stability.

### Study 3 — Multi-agent specialization and disagreement

Evaluate specialization, ablations, coordination failures, and disagreement as an uncertainty signal.

### Study 4 — Human oversight and trust calibration

Evaluate approval policies and reviewer behavior using controlled human-subject experiments where appropriate and ethically approved.

### Study 5 — Longitudinal assurance drift

Measure how agentic QA behavior changes under model, prompt, orchestration, or policy evolution.

---

## Falsifiability and Negative Results

A strong PhD project must remain valuable even if agentic AI does **not** outperform simpler SQA methods.

Important publishable negative findings could include:

- multi-agent coordination adds complexity without accuracy gains;
- specialized agents increase false positives;
- explicit confidence is poorly calibrated;
- human approval gates create excessive workload;
- evidence constraints improve traceability but reduce detection coverage;
- repeated-run instability makes some agentic configurations unsuitable for assurance;
- deterministic rules outperform agentic methods for specific classes of quality checks.

Such outcomes would still provide useful design guidance about where agentic AI should and should not be used in software quality assurance.

---

## Immediate Validation Tasks

Before treating these gap statements as thesis claims:

1. conduct a systematic or structured literature review;
2. define inclusion/exclusion criteria for agentic AI and SQA literature;
3. map existing studies against G1–G8;
4. identify prior work measuring evidence traceability, confidence, consistency, human oversight, and drift;
5. refine RQs and hypotheses based on the resulting evidence map;
6. pre-register experimental hypotheses where suitable;
7. avoid novelty claims unsupported by the literature review.

---

## Positioning Statement

The intended thesis contribution is not an autonomous replacement for software-quality engineers. It is a **scientific framework for determining when, how, and under what controls agentic AI can be trusted to participate in continuous software quality assurance**.