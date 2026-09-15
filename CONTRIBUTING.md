# Contributing

Contributions that improve reproducibility, software-quality evaluation, documentation, tests, or research methodology are welcome.

## Good contribution areas

- new controlled SQA benchmark scenarios;
- deterministic baselines;
- evaluation metrics;
- unit tests;
- documentation and research-method improvements;
- human-oversight experiments;
- evidence-traceability features.

## Research contribution requirements

Please document:

1. the research question or engineering problem;
2. assumptions and expected behavior;
3. new dependencies, if any;
4. tests or evaluation evidence;
5. limitations and threats to validity.

## Development

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -e ".[dev]"
pytest
```

Keep production-impact claims conservative. This repository is a research prototype, and contributions should not imply that agent-generated release recommendations are a substitute for accountable software-quality review.
