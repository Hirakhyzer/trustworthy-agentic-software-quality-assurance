# Benchmark Design

This directory contains reproducible software-quality benchmark definitions and evaluation utilities for the **Trustworthy Agentic Software Quality Assurance** research project.

## Benchmark principles

Each benchmark should:

1. define the software-quality condition before evaluation;
2. separate observable evidence from expected judgement;
3. include both positive and negative cases;
4. avoid leaking the expected decision into the evaluated agent prompt;
5. support deterministic baseline evaluation;
6. record repeated-run results for stochastic systems;
7. preserve the rationale used to establish synthetic ground truth;
8. include boundary and conflicting-evidence cases rather than only obvious failures.

## Current benchmark suite

The initial suite now contains **15 controlled scenarios** spanning eight benchmark families.

| Family | Controlled condition | Research purpose |
|---|---|---|
| Safe change | healthy test and change evidence | measure false positives and unnecessary escalation |
| Requirements quality | ambiguity and non-verifiable language | test whether requirement risk is detected even when implementation evidence is clean |
| Test adequacy | coverage regression | measure sensitivity to verification weakness |
| Test traceability | production changes without test changes | evaluate change-to-test evidence gaps |
| Maintainability | controlled complexity growth | study maintainability-risk detection |
| Defect evidence | known failing verification checks | test whether explicit failure evidence dominates release decisions |
| Conflicting evidence | positive and negative signals together | evaluate evidence prioritization and escalation |
| Boundary case | exact threshold values | expose brittle threshold behavior and calibration issues |
| Compound risk | multiple simultaneous quality signals | test aggregation and interaction effects |

The source scenarios are stored in [`../data/scenarios.json`](../data/scenarios.json).

## Scenario schema

Each synthetic benchmark case records:

```text
scenario_id
family
title
requirements
changed_modules
tests_changed
known_failures
complexity_delta
coverage_delta
expected_recommendation
expected_human_gate
ground_truth_basis
```

`ground_truth_basis` documents why the expected label was assigned. It is metadata for benchmark construction and reporting; it should not be provided to an evaluated AI system as input.

## Ground-truth policy

The current suite uses **controlled synthetic ground truth**. Expected recommendations are assigned from the scenario design before the evaluated system runs.

The labels intentionally do not mirror the implementation thresholds exactly. This is important: a benchmark should be able to expose weaknesses in both the deterministic baseline and the agentic system rather than reward either system for reproducing its own rules.

Three recommendation labels are used:

- `approve` — no elevated quality signal requires intervention;
- `review` — evidence warrants explicit quality review before release;
- `block` — a known unresolved failure or compound critical condition should prevent release in the synthetic study.

The separate `expected_human_gate` field allows oversight-policy evaluation even when the final recommendation is not `block`.

## Running the benchmark

From the repository root:

```bash
python -m pip install -e ".[dev]"
python benchmarks/run_benchmark.py
```

The runner reports:

- scenario-level expected, baseline, and agentic decisions;
- expected versus actual human-approval gates;
- agent confidence and aggregate risk;
- overall decision accuracy;
- human-gate agreement;
- family-level baseline and agentic accuracy.

Family-level reporting is important because aggregate accuracy can hide systematic weaknesses in requirements quality, maintainability, test adequacy, or conflicting-evidence cases.

## Result schema for future repeated-run experiments

Recommended CSV/JSON fields:

```text
scenario_id
family
condition
run_id
agent
finding
risk
confidence
evidence_count
recommendation
human_gate
expected_recommendation
expected_human_gate
correct
gate_correct
model_or_policy_version
seed
```

## Benchmark evolution plan

The synthetic suite should grow in stages:

1. increase scenario count within each family;
2. add paired counterfactual scenarios that differ in exactly one quality signal;
3. add repeated-run experiments for stochastic agents;
4. add controlled defect injection into miniature software repositories;
5. introduce open-source defect datasets only after license, provenance, leakage, and reproducibility requirements are documented;
6. freeze benchmark versions used in papers so later scenario changes do not alter previously reported results.

## Research caution

This benchmark is an experimental instrument, not a production release policy. Thresholds and expected decisions are intentionally simplified so that hypotheses about evidence, confidence, specialization, escalation, and reliability can be tested transparently.
