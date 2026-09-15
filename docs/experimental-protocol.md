# Experimental Protocol

## Objective

Provide a reproducible procedure for evaluating the agentic SQA framework across controlled software-quality scenarios.

## Procedure

1. Select a benchmark scenario and record its version.
2. Load the scenario without exposing its expected decision to the evaluated system.
3. Run the rule-based baseline.
4. Run the single-agent baseline, if included in the study.
5. Run the multi-agent SQA condition.
6. Record each finding, evidence item, confidence value, risk label, and final recommendation.
7. Apply the human oversight condition where required.
8. Compare outputs with scenario ground truth.
9. Repeat stochastic conditions using a predefined number of runs.
10. Aggregate detection, decision, consistency, calibration, and oversight metrics.

## Minimum run record

```text
experiment_id:
scenario_id:
scenario_version:
condition:
run_number:
agent_configuration:
quality_findings:
evidence_items:
confidence_values:
aggregate_risk:
recommendation:
human_gate_triggered:
human_decision:
expected_recommendation:
notes:
```

## Suggested experiment families

### Experiment A — Defect detection
Vary known failure evidence and observe defect-finding accuracy.

### Experiment B — Test adequacy
Vary coverage delta and test-change traceability.

### Experiment C — Requirements quality
Inject ambiguous or unverifiable requirements and compare detection performance.

### Experiment D — Conflicting evidence
Combine strong positive and negative signals to test aggregation behavior.

### Experiment E — Human oversight
Measure when human reviewers accept, override, or investigate agent recommendations.

### Experiment F — Stability
Repeat identical scenarios to measure recommendation and confidence consistency.

## Pre-registration recommendation

For publication-oriented experiments, define hypotheses, metrics, thresholds, exclusions, and statistical analyses before collecting final results. This reduces researcher degrees of freedom and makes negative findings more credible.
