# Research Framework

## Conceptual model

The framework treats software quality assurance as an evidence-mediated decision process rather than a free-form language-model task.

```text
Software change
    ↓
Observable quality evidence
    ↓
Specialized agent findings
    ↓
Evidence aggregation and confidence
    ↓
Risk classification
    ↓
Human oversight gate
    ↓
Assurance decision
```

## Design principles

### 1. Evidence before judgement
Every important finding should be linked to an observable input, such as a failed test, coverage change, complexity change, requirement property, defect record, or traceability gap.

### 2. Specialized roles
Agents should have narrow quality responsibilities. This allows experiments on division of labor, disagreement, and specialization.

### 3. Explicit uncertainty
Confidence is represented separately from risk. A high-risk finding with weak confidence should be investigated differently from a high-risk finding with strong evidence.

### 4. Human control
High-impact recommendations should pass through an explicit approval or review gate. The prototype therefore distinguishes analysis from authority.

### 5. Reproducibility
Scenario inputs, findings, confidence, recommendations, and evaluation outcomes should be persistable for repeated experiments.

## Experimental conditions

A useful PhD evaluation can compare at least three conditions:

| Condition | Description |
|---|---|
| Rule-based baseline | Conventional deterministic quality checks and thresholds. |
| Single-agent baseline | One AI reasoning component receives the complete scenario. |
| Multi-agent SQA | Specialized agents coordinate through the proposed orchestrator. |

Optional fourth condition:

| Condition | Description |
|---|---|
| Multi-agent + human oversight | Same agentic architecture with explicit reviewer approval and override. |

## Independent variables

Candidate independent variables include:

- defect density;
- requirement ambiguity;
- test coverage gap;
- change complexity;
- number of modified components;
- conflicting evidence;
- agent confidence threshold;
- human approval policy;
- number of specialized agents.

## Dependent variables

Candidate outcomes include:

- precision and recall of quality findings;
- false positive and false negative rates;
- release recommendation accuracy;
- calibration error;
- repeated-run consistency;
- explanation/evidence completeness;
- human override rate;
- review time;
- perceived trust and usefulness.

## Research hypothesis examples

- **H1:** Multi-agent SQA detects a broader range of controlled quality risks than a single-agent baseline.
- **H2:** Evidence-grounded findings reduce unsupported quality claims.
- **H3:** Human approval gates reduce incorrect autonomous release recommendations for high-risk scenarios.
- **H4:** Explicit confidence information improves human trust calibration.
- **H5:** Specialized agents increase traceability but may introduce coordination inconsistency, which can be measured and mitigated.
