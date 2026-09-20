# Agent Ablation and Disagreement Study

## Purpose

This study investigates whether each specialized quality agent contributes unique value to the overall assurance decision and whether disagreement among agents can act as a measurable uncertainty signal.

The study directly supports two PhD hypotheses:

- **H7:** Removing specialized agents through ablation will reduce detection performance in the quality-risk categories primarily assigned to those agents.
- **H8:** Higher inter-agent disagreement will be associated with recommendation error or cases requiring human override.

## Why ablation matters

A multi-agent architecture should not be assumed to be better simply because it contains more agents. If removing an agent has no measurable effect, that role may be redundant. If removing an agent improves performance, the role may be introducing noise, duplicated evidence, or coordination error.

Ablation therefore tests whether specialization is empirically justified.

## Configurations

The benchmark runner compares the full five-agent system with one-agent-removed variants:

| Configuration | Removed role |
|---|---|
| full | none |
| without-requirements-qa | Requirements QA Agent |
| without-code-quality | Code Quality Agent |
| without-test-strategy | Test Strategy Agent |
| without-defect-analysis | Defect Analysis Agent |
| without-release-assurance | Release Assurance Agent |

The script is available at:

```text
benchmarks/run_ablation_study.py
```

Run it with:

```bash
python benchmarks/run_ablation_study.py
```

## Primary measures

### Recommendation accuracy

Exact agreement with benchmark ground truth.

### Undercall rate

The fraction of cases where the system is less conservative than the benchmark label, such as approving a case that should be reviewed or blocked.

### Mean inter-agent risk disagreement

For each decision, every pair of agent findings is compared. The disagreement score is:

```text
number of agent pairs with different risk labels
------------------------------------------------
total number of agent pairs
```

A score of `0.0` means unanimous agent risk labels. A higher score means more disagreement.

## Research questions

### AQ1

Does removing a specialized agent reduce overall recommendation accuracy?

### AQ2

Does removing a specialized agent increase the undercall rate?

### AQ3

Which agent removals produce the largest change in disagreement?

### AQ4

Are scenarios with higher disagreement more likely to produce incorrect recommendations?

### AQ5

Are scenarios with higher disagreement more likely to trigger, or benefit from, human review?

## Interpretation rules

Ablation results must not be interpreted only from overall accuracy.

For example:

- unchanged accuracy with a higher undercall rate may indicate a safety regression;
- lower disagreement after removing an agent is not necessarily beneficial if the removed agent was correctly identifying a distinct risk;
- higher disagreement can indicate useful diversity rather than poor coordination;
- the Release Assurance Agent may overlap with evidence already reviewed by specialized agents, so its ablation should be examined for redundancy carefully.

## Planned analysis

For each configuration, report:

- overall accuracy;
- undercall rate;
- mean disagreement;
- per-family accuracy;
- per-family undercall rate;
- human-gate behavior;
- cases where the recommendation changes relative to the full configuration.

For disagreement analysis, compare disagreement distributions across:

1. correct vs incorrect decisions;
2. human-gated vs non-gated decisions;
3. approve, review, and block cases;
4. quality-risk families.

## Statistical plan

When the benchmark grows sufficiently large, use paired analysis because every configuration is evaluated on the same scenarios.

Candidate methods include:

- McNemar-style paired comparison for recommendation correctness;
- paired bootstrap confidence intervals for metric differences;
- non-parametric paired tests for disagreement scores;
- effect sizes in addition to p-values.

Statistical testing should only be applied once scenario counts are large enough to make the analysis meaningful.

## Threats to validity

The current synthetic benchmark is small and partly constructed from the same quality assumptions used by the prototype agents. This can inflate apparent performance and should not be treated as evidence of real-world generalization.

The next validation stage should introduce independent open-source defect datasets, externally defined quality cases, or blinded scenario construction.

## Expected contribution

This study turns multi-agent architecture design into an empirical question. Rather than claiming that specialization is inherently useful, the project measures which agent roles contribute distinct assurance value, which are redundant, and whether disagreement itself can help identify uncertain or high-risk release decisions.
