from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from trustworthy_agentic_sqa import AgenticSQAOrchestrator, SoftwareChange
from trustworthy_agentic_sqa.baselines import rule_based_baseline


ROOT = Path(__file__).resolve().parents[1]


def load_scenarios() -> list[dict]:
    return json.loads((ROOT / "data" / "scenarios.json").read_text(encoding="utf-8"))


def to_change(raw: dict) -> SoftwareChange:
    return SoftwareChange(
        change_id=raw["scenario_id"],
        requirements=raw["requirements"],
        changed_modules=raw["changed_modules"],
        tests_changed=raw["tests_changed"],
        known_failures=raw["known_failures"],
        complexity_delta=raw["complexity_delta"],
        coverage_delta=raw["coverage_delta"],
    )


def main() -> None:
    scenarios = load_scenarios()
    orchestrator = AgenticSQAOrchestrator()

    correct_agentic = 0
    correct_baseline = 0
    correct_human_gate = 0
    family_counts: dict[str, dict[str, int]] = defaultdict(
        lambda: {"total": 0, "baseline": 0, "agentic": 0, "gate": 0}
    )

    print(
        "scenario\tfamily\texpected\tbaseline\tagentic\t"
        "expected_gate\tactual_gate\tagent_confidence\taggregate_risk"
    )

    for raw in scenarios:
        change = to_change(raw)
        expected = raw["expected_recommendation"]
        expected_gate = raw["expected_human_gate"]
        family = raw["family"]

        baseline = rule_based_baseline(change).value
        decision = orchestrator.assess(change)
        agentic = decision.recommendation.value

        baseline_correct = baseline == expected
        agentic_correct = agentic == expected
        gate_correct = decision.requires_human_approval == expected_gate

        correct_baseline += int(baseline_correct)
        correct_agentic += int(agentic_correct)
        correct_human_gate += int(gate_correct)

        family_counts[family]["total"] += 1
        family_counts[family]["baseline"] += int(baseline_correct)
        family_counts[family]["agentic"] += int(agentic_correct)
        family_counts[family]["gate"] += int(gate_correct)

        print(
            f"{raw['scenario_id']}\t{family}\t{expected}\t{baseline}\t{agentic}\t"
            f"{expected_gate}\t{decision.requires_human_approval}\t"
            f"{decision.confidence:.3f}\t{decision.aggregate_risk.value}"
        )

    total = len(scenarios)
    print("\nOverall summary")
    print(f"Scenarios:                {total}")
    print(f"Rule baseline accuracy:   {correct_baseline}/{total} ({correct_baseline / total:.1%})")
    print(f"Agentic SQA accuracy:     {correct_agentic}/{total} ({correct_agentic / total:.1%})")
    print(f"Human-gate agreement:     {correct_human_gate}/{total} ({correct_human_gate / total:.1%})")

    print("\nFamily-level summary")
    print("family\tn\tbaseline_accuracy\tagentic_accuracy\tgate_agreement")
    for family in sorted(family_counts):
        values = family_counts[family]
        n = values["total"]
        print(
            f"{family}\t{n}\t"
            f"{values['baseline'] / n:.1%}\t"
            f"{values['agentic'] / n:.1%}\t"
            f"{values['gate'] / n:.1%}"
        )


if __name__ == "__main__":
    main()
