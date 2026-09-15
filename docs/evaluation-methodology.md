# Evaluation Methodology

## Goal

Evaluate whether trustworthy agentic AI can improve continuous software quality assurance while preserving evidence traceability, calibrated uncertainty, and human control.

## Baselines

The recommended experimental design compares:

1. **Rule-based SQA** — deterministic thresholds and scripted checks.
2. **Single-agent AI SQA** — one general-purpose agent receives the full scenario.
3. **Multi-agent SQA** — specialized agents coordinated by the proposed architecture.
4. **Multi-agent + human oversight** — high-risk or low-confidence decisions require reviewer approval.

## Scenario classes

Synthetic scenarios should vary along controlled dimensions:

- requirement ambiguity;
- missing acceptance criteria;
- code complexity growth;
- test coverage loss;
- changed production code without changed tests;
- known failing tests;
- conflicting quality evidence;
- apparently safe changes with no injected defect.

## Ground truth

Each benchmark scenario should define an expected quality state and release recommendation before the agent system is run. Ground truth can be constructed from controlled defect injection and deterministic scenario metadata.

## Metrics

### Detection performance

- precision;
- recall;
- F1 score;
- false-positive rate;
- false-negative rate.

### Decision performance

- release recommendation accuracy;
- risk classification accuracy;
- human escalation precision;
- human escalation recall.

### Trustworthiness performance

- unsupported finding rate;
- evidence completeness;
- repeated-run consistency;
- confidence calibration;
- inter-agent agreement;
- human override rate.

### Human-centered outcomes

For participant studies:

- perceived usefulness;
- perceived transparency;
- trust calibration;
- review workload;
- time to decision;
- willingness to rely on the system in low- versus high-risk cases.

## Ablation studies

Useful ablations include:

- remove the requirements agent;
- remove confidence information;
- remove human approval gates;
- remove evidence references;
- use one general agent instead of specialized agents;
- change aggregation thresholds.

## Repeated-run evaluation

Where stochastic AI models are introduced, run each scenario multiple times and report mean, variance, and decision agreement. This prevents one successful run from being treated as representative performance.

## Reporting

Every experiment should publish:

- software and model configuration;
- scenario version;
- seeds where applicable;
- baseline definitions;
- raw decision outputs;
- metric definitions;
- confidence intervals where appropriate;
- failures and negative results.
