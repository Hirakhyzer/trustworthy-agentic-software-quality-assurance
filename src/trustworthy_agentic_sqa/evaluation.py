from __future__ import annotations

from dataclasses import dataclass

from .schema import AssuranceDecision, Recommendation


@dataclass(frozen=True)
class EvaluationResult:
    expected: Recommendation
    predicted: Recommendation
    correct: bool
    human_gate_triggered: bool


def evaluate_decision(decision: AssuranceDecision, expected: Recommendation) -> EvaluationResult:
    return EvaluationResult(
        expected=expected,
        predicted=decision.recommendation,
        correct=decision.recommendation == expected,
        human_gate_triggered=decision.requires_human_approval,
    )


def decision_consistency(decisions: list[AssuranceDecision]) -> float:
    if not decisions:
        return 0.0
    first = decisions[0].recommendation
    matches = sum(d.recommendation == first for d in decisions)
    return matches / len(decisions)
