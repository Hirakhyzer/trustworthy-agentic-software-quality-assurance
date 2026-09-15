# Research Framework

## Purpose

This document defines the conceptual and experimental framework for the project. The detailed PhD positioning, research gaps, refined research questions, falsifiable hypotheses, and expected contributions are maintained in [`research-gap.md`](research-gap.md).

## Conceptual model

The framework treats software quality assurance as an evidence-mediated decision process rather than a free-form language-model task.

```text
Software change
    ↓
Observable quality evidence
    ↓
Specialized agent findings
    ↓
Evidence aggregation
    ↓
Risk + confidence + disagreement
    ↓
Oversight policy
    ↓
Human approval / autonomous recommendation
    ↓
Assurance decision
    ↓
Evaluation + audit record
```

The central design principle is that **analysis and authority are separate**. An agent can identify a quality concern without automatically receiving authority to approve or block a release.

## Core PhD research question

> **How can agentic AI be designed and empirically evaluated to improve continuous software quality assurance while preserving evidence traceability, calibrated uncertainty, decision reliability, and meaningful human control?**

## Refined research questions

| ID | Research question |
|---|---|
| RQ1 | To what extent does specialized multi-agent SQA improve detection and prioritization of software-quality risks compared with rule-based and single-agent baselines? |
| RQ2 | Does requiring explicit evidence for every agent finding reduce unsupported quality claims and improve traceability? |
| RQ3 | How stable are agentic SQA findings and release recommendations across repeated runs and controlled configuration changes? |
| RQ4 | Which human-oversight policy best reduces incorrect high-impact recommendations without creating unnecessary review workload? |
| RQ5 | Does explicit confidence representation improve agent calibration and human reliance? |
| RQ6 | When does specialization improve SQA, and when does coordination overhead or disagreement reduce performance? |
| RQ7 | How do model, prompt, policy, and orchestration changes affect assurance reproducibility over time? |

See [`research-gap.md`](research-gap.md) for operational definitions and outcome measures for each RQ.

## Design principles

### 1. Evidence before judgement

Every important finding should be linked to an observable input, such as a failed test, coverage change, complexity change, requirement property, defect record, or traceability gap.

### 2. Specialized roles

Agents should have narrow quality responsibilities. This supports experiments on division of labor, disagreement, specialization, and agent ablation.

### 3. Risk and confidence are distinct

Software risk describes the potential quality impact of the change. Confidence describes how strongly the available evidence supports the agent's judgement. These signals should be represented and evaluated separately.

### 4. Disagreement is observable

Inter-agent disagreement should not be silently hidden by aggregation. It can be measured as a possible signal for uncertainty, coordination failure, or escalation.

### 5. Human control

High-impact recommendations should pass through an explicit approval or review gate. Human oversight is treated as an experimentally testable design variable rather than a purely normative requirement.

### 6. Repeated-run reliability

Point accuracy is not enough for assurance. Equivalent inputs should be evaluated across repeated runs so that variance and decision stability can be measured.

### 7. Reproducibility

Scenario inputs, agent configuration, evidence, findings, confidence, recommendations, human decisions, and outcomes should be persistable for repeated experiments.

### 8. Evolution must be auditable

Changes to models, prompts, tools, thresholds, or orchestration policies can change assurance behavior. Longitudinal experiments should therefore treat agent-system evolution as a potential source of assurance drift.

## Experimental conditions

The core experimental programme compares four conditions:

| Condition | Description |
|---|---|
| Rule-based baseline | Conventional deterministic quality checks and explicit thresholds. |
| Single-agent baseline | One AI reasoning component receives the complete scenario. |
| Multi-agent SQA | Specialized agents coordinate through the proposed orchestrator. |
| Multi-agent + human oversight | The same architecture with explicit reviewer approval and override. |

Additional experiments may compare evidence-constrained and free-form outputs, risk-only and risk-plus-confidence escalation, or alternative oversight policies.

## Independent variables

Candidate independent variables include:

- SQA architecture;
- defect density;
- requirement ambiguity;
- test coverage gap;
- change complexity;
- number of modified components;
- conflicting evidence;
- evidence-grounding policy;
- confidence threshold;
- human approval policy;
- number and type of specialized agents;
- agent disagreement level;
- model, prompt, or orchestration configuration.

## Dependent variables

Candidate outcomes include:

### Software-quality performance

- precision;
- recall;
- F1 score;
- false-positive rate;
- false-negative rate;
- release recommendation accuracy;
- quality-risk ranking agreement.

### Trustworthiness performance

- unsupported finding rate;
- evidence completeness;
- evidence-to-finding traceability;
- calibration error;
- repeated-run agreement;
- finding-set similarity;
- inter-agent disagreement;
- decision drift.

### Human-centered performance

- human escalation precision and recall;
- human override rate;
- prevented incorrect approvals;
- review time;
- reviewer workload;
- appropriate reliance;
- perceived transparency and usefulness.

## Refined hypotheses

The detailed hypotheses, null hypotheses, and measurement mapping are defined in [`research-gap.md`](research-gap.md). The primary hypothesis set is:

- **H1:** Specialized multi-agent SQA will achieve higher recall for heterogeneous software-quality risks than a single-agent baseline while maintaining comparable precision.
- **H2:** Structured evidence requirements will reduce unsupported quality findings compared with free-form agent reasoning.
- **H3:** Risk- and confidence-triggered human approval gates will reduce incorrect autonomous release approvals in high-impact scenarios.
- **H4:** Separating confidence from software-risk classification will improve escalation quality compared with risk-only escalation.
- **H5:** Reviewers shown explicit evidence and calibrated confidence will demonstrate more appropriate reliance on agentic SQA recommendations.
- **H6:** Evidence-constrained agentic SQA will produce higher repeated-run decision agreement than unconstrained free-form agentic SQA.
- **H7:** Removing specialized agents through ablation will reduce detection performance in the quality-risk categories primarily assigned to those agents.
- **H8:** Higher inter-agent disagreement will be associated with recommendation error or cases requiring human override.
- **H9:** Selective approval policies based on risk and confidence will provide a better safety/workload trade-off than mandatory review of every case.
- **H10:** Model, prompt, or orchestration changes will cause measurable assurance drift that can be detected using regression benchmarks.

## Expected contribution structure

The PhD contribution is expected to span eight layers:

1. **Conceptual** — an evidence-mediated model of agentic SQA that separates evidence, judgement, uncertainty, and authority.
2. **Architectural** — a reference architecture for specialized trustworthy QA agents and human approval gates.
3. **Measurement** — metrics for evidence completeness, unsupported claims, calibration, disagreement, stability, escalation, and drift.
4. **Benchmark** — reproducible controlled scenarios with known software-quality ground truth.
5. **Empirical** — comparison of rule-based, single-agent, multi-agent, and human-supervised conditions.
6. **Human-centered** — evidence on where intervention improves quality decisions without excessive workload.
7. **Reproducibility** — a protocol for recording configurations, evidence, decisions, approvals, and repeated runs.
8. **Assurance drift** — a method for evaluating whether agentic QA behavior changes unexpectedly as the AI system evolves.

## Novelty boundary

The project should not claim novelty simply from using multiple AI agents. The intended research contribution must be validated around the combination of continuous SQA, evidence-first decisions, explicit risk/confidence separation, measurable disagreement, selective human authority, repeated-run reliability, assurance-drift analysis, and reproducible baseline comparison.

A systematic literature review should validate which parts of this positioning are genuinely novel, partially explored, or already established.

## Scientific stance

The framework is designed to remain informative even when the hypotheses are rejected. For example, a finding that rule-based SQA outperforms an agentic system for particular classes of quality checks would still provide useful evidence about where agentic AI should not be used.