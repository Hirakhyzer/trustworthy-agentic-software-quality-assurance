# Benchmark Design

This directory is reserved for reproducible software-quality benchmark definitions and results.

## Benchmark principles

Each benchmark should:

1. define the software-quality condition before evaluation;
2. separate observable evidence from expected judgement;
3. include both positive and negative cases;
4. avoid leaking the expected decision into the evaluated agent prompt;
5. support deterministic baseline evaluation;
6. record repeated-run results for stochastic systems.

## Initial benchmark families

| Family | Controlled variable | Example outcome |
|---|---|---|
| Requirements quality | ambiguity and verifiability | ambiguous requirement detected or missed |
| Maintainability | complexity change | elevated review risk |
| Test adequacy | coverage and test-change evidence | review recommendation |
| Defect evidence | known failing checks | block recommendation |
| Conflicting evidence | mixed positive/negative signals | calibrated escalation |
| Oversight | risk/confidence thresholds | human gate triggered or bypassed |

## Result schema

Recommended CSV/JSON fields:

```text
scenario_id
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
correct
```

Future work can add real open-source defect datasets after dataset licenses, provenance, and reproducibility requirements are documented.
