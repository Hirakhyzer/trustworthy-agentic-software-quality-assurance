# Metrics Specification

## Purpose

This document defines the primary quantitative metrics for evaluating trustworthy agentic software quality assurance. The goal is to avoid relying on a single accuracy number and instead measure effectiveness, safety, oversight quality, evidence traceability, and repeated-run reliability separately.

## Why raw accuracy is insufficient

Release recommendations are ordinal:

```text
approve < review < block
```

An incorrect `review` prediction for a case that should be `block` is not equivalent to an incorrect `approve` prediction for that same case. For assurance research, less-conservative errors are especially important because they can allow risky changes to proceed.

The evaluation module therefore reports both conventional correctness and safety-oriented error measures.

## Core metrics

### 1. Recommendation accuracy

The proportion of benchmark scenarios where the predicted recommendation exactly matches ground truth.

```text
accuracy = correct recommendations / total recommendations
```

This is useful for overall comparison but should never be reported alone.

### 2. Mean ordinal recommendation error

Recommendations are mapped to an ordinal scale:

```text
approve = 0
review  = 1
block   = 2
```

The absolute distance between predicted and expected recommendations is calculated for every scenario and then averaged.

A prediction of `approve` when `block` is expected therefore has an error of 2, while `review` instead of `block` has an error of 1.

### 3. Undercall rate

The proportion of scenarios where the predicted recommendation is less conservative than the expected recommendation.

Examples:

- predicted `approve`, expected `review` -> undercall;
- predicted `approve`, expected `block` -> undercall;
- predicted `review`, expected `block` -> undercall;
- predicted `block`, expected `review` -> not an undercall.

This metric is intended to expose potentially unsafe recommendation errors that could be hidden by aggregate accuracy.

### 4. Human-gate precision

Among all scenarios where the system requested human approval, the proportion that truly required human review according to benchmark ground truth.

High precision means the oversight mechanism does not create excessive unnecessary escalations.

### 5. Human-gate recall

Among all scenarios that should have required human approval, the proportion correctly escalated by the system.

High recall means risky or uncertain cases are rarely allowed to bypass human oversight.

### 6. Human-gate F1

The harmonic mean of gate precision and gate recall. This provides one summary measure for comparing alternative oversight policies while preserving the tension between excessive review burden and missed escalation.

### 7. Mean decision confidence

The average confidence reported across assurance decisions.

This is descriptive rather than inherently good or bad. It should be interpreted together with calibration analysis. High confidence is only desirable when it corresponds to high correctness.

### 8. Evidence coverage

For each assurance decision, evidence coverage is the fraction of agent findings that contain at least one structured `QualityEvidence` item. Benchmark-level evidence coverage is the mean across decisions.

This metric operationalizes the project's evidence-first principle by distinguishing traceable findings from unsupported narrative judgements.

### 9. Repeated-run decision consistency

For repeated evaluations of an equivalent scenario, consistency is measured as the proportion of recommendations matching the first run.

For stochastic model experiments, this should be complemented with pairwise agreement, variance, and confidence intervals.

## Reporting requirements

Every experiment should report at minimum:

| Dimension | Required metric |
|---|---|
| Effectiveness | recommendation accuracy |
| Error severity | mean ordinal error |
| Safety | undercall rate |
| Human oversight | gate precision, recall, and F1 |
| Uncertainty | mean confidence plus calibration analysis when possible |
| Traceability | evidence coverage |
| Reliability | repeated-run consistency for stochastic conditions |

## Interpretation guidance

No single metric establishes that an agentic SQA system is trustworthy.

For example:

- higher accuracy with a higher undercall rate may be unacceptable for high-impact release decisions;
- perfect gate recall with very low precision may create excessive reviewer workload;
- high evidence coverage does not prove that cited evidence is correct or relevant;
- high repeated-run consistency can indicate stable behavior even when the behavior is consistently wrong;
- high confidence without calibration can increase automation bias.

The metrics should therefore be interpreted jointly and compared across rule-based, single-agent, multi-agent, and human-supervised experimental conditions.

## Planned extensions

Future evaluation work should add:

- calibration error and reliability diagrams;
- per-quality-family precision and recall;
- confusion matrices for approve/review/block;
- inter-agent disagreement measures;
- evidence relevance and correctness scoring;
- reviewer workload and time-to-decision;
- human override effectiveness;
- longitudinal assurance-drift metrics;
- bootstrap confidence intervals and statistical significance testing where appropriate.

## Reproducibility note

Metric definitions must remain versioned with experimental results. If a threshold, ground-truth label, aggregation rule, or metric definition changes, the experiment version should change as well so that results remain reproducible and comparable.
