from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIO_PATH = ROOT / "data" / "scenarios.json"


REQUIRED_FIELDS = {
    "scenario_id",
    "family",
    "title",
    "requirements",
    "changed_modules",
    "tests_changed",
    "known_failures",
    "complexity_delta",
    "coverage_delta",
    "expected_recommendation",
    "expected_human_gate",
    "ground_truth_basis",
}

VALID_RECOMMENDATIONS = {"approve", "review", "block"}


def load_scenarios() -> list[dict]:
    return json.loads(SCENARIO_PATH.read_text(encoding="utf-8"))


def test_benchmark_has_multiple_quality_families() -> None:
    scenarios = load_scenarios()
    families = {scenario["family"] for scenario in scenarios}

    assert len(scenarios) >= 15
    assert len(families) >= 8


def test_scenario_ids_are_unique() -> None:
    scenarios = load_scenarios()
    ids = [scenario["scenario_id"] for scenario in scenarios]

    assert len(ids) == len(set(ids))


def test_all_scenarios_have_required_ground_truth_fields() -> None:
    for scenario in load_scenarios():
        assert REQUIRED_FIELDS.issubset(scenario)
        assert scenario["expected_recommendation"] in VALID_RECOMMENDATIONS
        assert isinstance(scenario["expected_human_gate"], bool)
        assert scenario["ground_truth_basis"].strip()


def test_suite_contains_positive_negative_and_blocking_cases() -> None:
    recommendations = {
        scenario["expected_recommendation"] for scenario in load_scenarios()
    }

    assert recommendations == VALID_RECOMMENDATIONS


def test_suite_contains_conflicting_and_boundary_cases() -> None:
    families = {scenario["family"] for scenario in load_scenarios()}

    assert "conflicting-evidence" in families
    assert "boundary-case" in families
    assert "safe-change" in families
