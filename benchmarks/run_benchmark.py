from __future__ import annotations

import json
from pathlib import Path

from trustworthy_agentic_sqa import AgenticSQAOrchestrator, SoftwareChange
from trustworthy_agentic_sqa.baselines import rule_based_baseline


ROOT = Path(__file__).resolve().parents[1]


def load_scenarios() -> list[dict]:
    return json.loads((ROOT / "data" / "scenarios.json").read_text(encoding="utf-8"))


def main() -> None:
    orchestrator = AgenticSQAOrchestrator()
    correct_agentic = 0
    correct_baseline = 0

    print("scenario\texpected\tbaseline\tagentic\thuman_gate")

    for raw in load_scenarios():
        change = SoftwareChange(
            change_id=raw["scenario_id"],
            requirements=raw["requirements"],
            changed_modules=raw["changed_modules"],
            tests_changed=raw["tests_changed"],
            known_failures=raw["known_failures"],
            complexity_delta=raw["complexity_delta"],
            coverage_delta=raw["coverage_delta"],
        )
        expected = raw["expected_recommendation"]
        baseline = rule_based_baseline(change).value
        decision = orchestrator.assess(change)
        agentic = decision.recommendation.value

        correct_baseline += baseline == expected
        correct_agentic += agentic == expected

        print(
            f"{raw['scenario_id']}\t{expected}\t{baseline}\t{agentic}\t"
            f"{decision.requires_human_approval}"
        )

    total = len(load_scenarios())
    print("\nSummary")
    print(f"Rule baseline accuracy: {correct_baseline}/{total}")
    print(f"Agentic SQA accuracy:   {correct_agentic}/{total}")


if __name__ == "__main__":
    main()
