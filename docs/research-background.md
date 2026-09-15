# Research Background

Software quality assurance increasingly operates in continuous-delivery environments where requirements, code, tests, dependencies, and operational evidence change rapidly. Traditional quality gates remain useful, but they can struggle with the volume and heterogeneity of evidence available during modern release cycles.

Agentic AI introduces a different research opportunity: instead of using a single model to produce one quality judgement, multiple specialized agents can coordinate around requirements quality, maintainability, test adequacy, defect evidence, and release readiness. This creates opportunities for richer analysis, but also introduces new assurance challenges.

## Research problem

An agentic QA system can fail even when individual agents appear capable. Important failure modes include:

- unsupported or hallucinated quality findings;
- inconsistent recommendations across repeated runs;
- overconfident risk assessments;
- weak traceability between evidence and conclusions;
- disagreement between agents without a principled resolution method;
- automation bias in human reviewers;
- unclear responsibility for release decisions;
- hidden quality regressions caused by agent configuration or model drift.

The research question is therefore not only whether AI can detect defects. The stronger question is whether agentic AI can participate in software quality assurance in a way that is measurable, explainable, auditable, and appropriately controlled.

## PhD research direction

This repository supports a research programme around four themes:

1. **Quality intelligence** — how specialized agents detect and prioritize software-quality concerns.
2. **Trustworthy orchestration** — how evidence, confidence, disagreement, and escalation should be managed across agents.
3. **Human oversight** — when humans should approve, override, or investigate agent recommendations.
4. **Empirical evaluation** — how agentic QA compares with conventional automation and single-agent baselines.

## Candidate empirical studies

- Controlled defect-injection experiments across synthetic repositories.
- Requirements ambiguity and traceability experiments.
- Test recommendation experiments using controlled coverage gaps.
- Release-readiness studies comparing rule-based, single-agent, and multi-agent approaches.
- Human-subject studies on trust calibration and explanation quality.
- Longitudinal experiments on decision stability under configuration or model changes.

## Intended contribution

The project aims to produce a reusable experimental framework, not a claim that autonomous agents should replace software-quality professionals. Its value lies in making agentic QA decisions observable enough to study scientifically.
