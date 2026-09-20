from __future__ import annotations

import json
from pathlib import Path

from trustworthy_agentic_sqa import AgenticSQAOrchestrator, Recommendation, SoftwareChange
from trustworthy_agentic_sqa.evaluation import agent_risk_disagreement
from trustworthy_agentic_sqa.quality_agents import (
    CodeQualityAgent,
    DefectAnalysisAgent,
    ReleaseAssuranceAgent,
    RequirementsQAAgent,
    TestStrategyAgent,
)


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


def full_agent_set():
    return [
        RequirementsQAAgent(),
        CodeQualityAgent(),
        TestStrategyAgent(),
        DefectAnalysisAgent(),
        ReleaseAssuranceAgent(),
    ]


def main() -> None:
    scenarios = load_scenarios()
    configurations: dict[str, list] = {"full": full_agent_set()}

    for removed_index, removed_agent in enumerate(full_agent_set()):
        configurations[f"without-{removed_agent.name}"] = [
            agent for index, agent in enumerate(full_agent_set()) if index != removed_index
        ]

    print("configuration\taccuracy\tundercalls\tmean_disagreement")

    for name, agents in configurations.items():
        orchestrator = AgenticSQAOrchestrator(agents=agents)
        correct = 0
        undercalls = 0
        disagreements: list[float] = []

        for raw in scenarios:
            decision = orchestrator.assess(to_change(raw))
            expected = Recommendation(raw["expected_recommendation"])
            correct += int(decision.recommendation == expected)
            undercalls += int(
                decision.recommendation.value == "approve"
                and expected.value in {"review", "block"}
                or decision.recommendation.value == "review"
                and expected.value == "block"
            )
            disagreements.append(agent_risk_disagreement(decision))

        total = len(scenarios)
        mean_disagreement = sum(disagreements) / total
        print(
            f"{name}\t{correct / total:.3f}\t"
            f"{undercalls / total:.3f}\t{mean_disagreement:.3f}"
        )


if __name__ == "__main__":
    main()
