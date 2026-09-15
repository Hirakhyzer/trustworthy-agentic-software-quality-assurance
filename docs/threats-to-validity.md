# Threats to Validity

## Construct validity

Synthetic indicators such as complexity delta or coverage change are proxies for software quality, not quality itself. Experiments should avoid claiming that one metric fully represents maintainability, reliability, or release readiness.

## Internal validity

Results may be influenced by scenario design, thresholds, prompt construction, agent ordering, aggregation rules, or researcher expectations. Controlled ablations and preregistered evaluation criteria can reduce these effects.

## External validity

Synthetic repositories may not represent large industrial systems, legacy codebases, regulated software, complex socio-technical workflows, or organization-specific release practices. Claims should therefore be scoped to evaluated settings.

## Conclusion validity

Small scenario sets can produce unstable estimates. Repeated runs, confidence intervals, effect sizes, and transparent negative results are preferable to conclusions based only on point estimates.

## AI-specific validity threats

When external AI models are introduced, results may depend on:

- model version;
- provider updates;
- inference temperature;
- prompt wording;
- context ordering;
- hidden system behavior;
- nondeterminism.

Experiments should record these variables wherever possible.

## Human-study threats

Participant expertise, familiarity with AI tools, software-engineering background, and risk tolerance may affect trust and override behavior. Human-subject studies should document recruitment, experience levels, training, and study tasks.

## Mitigation strategy

Use multiple scenario classes, deterministic baselines, repeated runs, clear ground truth, blinded scoring when feasible, and complete experiment logs. Findings should distinguish prototype performance from broader claims about autonomous software engineering.
