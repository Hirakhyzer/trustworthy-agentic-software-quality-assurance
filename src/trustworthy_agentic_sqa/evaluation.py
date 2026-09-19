from __future__ import annotations

from dataclasses import dataclass
from statistics import mean

from .schema import AssuranceDecision, Recommendation


_RECOMMENDATION_ORDER = {
    Recommendation.APPROVE: 0,
    Recommendation.REVIEW: 1,
    Recommendation.BLOCK: 2,
}


@dataclass(frozen=True)
class EvaluationResult:
    expected: Recommendation
    predicted: Recommendation
    correct: bool
    human_gate_triggered: bool


@dataclass(frozen=True)
class BenchmarkMetrics:
    """Aggregate metrics for controlled agentic-SQA experiments."""

    recommendation_accuracy: float
    mean_ordinal_error: float
    undercall_rate: float
    gate_precision: float
    gate_recall: float
    gate_f1: float
    mean_confidence: float
    evidence_coverage: float


def evaluate_decision(decision: AssuranceDecision, expected: Recommendation) -> EvaluationResult:
    return EvaluationResult(
        expected=expected,
        predicted=decision.recommendation,
        correct=decision.recommendation == expected,
        human_gate_triggered=decision.requires_human_approval,
    )


def decision_consistency(decisions: list[AssuranceDecision]) -> float:
    """Return the proportion of decisions matching the first recommendation."""
    if not decisions:
        return 0.0
    first = decisions[0].recommendation
    matches = sum(d.recommendation == first for d in decisions)
    return matches / len(decisions)


def ordinal_recommendation_error(
    predicted: Recommendation,
    expected: Recommendation,
) -> int:
    """Distance between approve, review, and block on an ordinal scale."""
    return abs(_RECOMMENDATION_ORDER[predicted] - _RECOMMENDATION_ORDER[expected])


def is_undercall(predicted: Recommendation, expected: Recommendation) -> bool:
    """Return True when a prediction is less conservative than ground truth."""
    return _RECOMMENDATION_ORDER[predicted] < _RECOMMENDATION_ORDER[expected]


def finding_evidence_coverage(decision: AssuranceDecision) -> float:
    """Fraction of findings that cite at least one structured evidence item."""
    if not decision.findings:
        return 0.0
    supported = sum(bool(finding.evidence) for finding in decision.findings)
    return supported / len(decision.findings)


def _binary_precision_recall_f1(
    expected: list[bool],
    predicted: list[bool],
) -> tuple[float, float, float]:
    true_positive = sum(e and p for e, p in zip(expected, predicted))
    false_positive = sum((not e) and p for e, p in zip(expected, predicted))
    false_negative = sum(e and (not p) for e, p in zip(expected, predicted))

    precision = (
        true_positive / (true_positive + false_positive)
        if true_positive + false_positive
        else 0.0
    )
    recall = (
        true_positive / (true_positive + false_negative)
        if true_positive + false_negative
        else 0.0
    )
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return precision, recall, f1


def summarize_benchmark(
    decisions: list[AssuranceDecision],
    expected_recommendations: list[Recommendation],
    expected_human_gates: list[bool],
) -> BenchmarkMetrics:
    """Summarize effectiveness, safety, oversight, and evidence metrics.

    The three lists must be aligned by scenario. This function deliberately
    reports ordinal error and under-calls separately from raw accuracy because
    approving a case that should be blocked is more important to surface than
    a generic incorrect-decision count.
    """
    if not decisions:
        raise ValueError("at least one decision is required")
    if not (
        len(decisions)
        == len(expected_recommendations)
        == len(expected_human_gates)
    ):
        raise ValueError("decisions and expected labels must have equal length")

    predicted_recommendations = [decision.recommendation for decision in decisions]
    predicted_gates = [decision.requires_human_approval for decision in decisions]

    correct = sum(
        predicted == expected
        for predicted, expected in zip(predicted_recommendations, expected_recommendations)
    )
    ordinal_errors = [
        ordinal_recommendation_error(predicted, expected)
        for predicted, expected in zip(predicted_recommendations, expected_recommendations)
    ]
    undercalls = sum(
        is_undercall(predicted, expected)
        for predicted, expected in zip(predicted_recommendations, expected_recommendations)
    )
    gate_precision, gate_recall, gate_f1 = _binary_precision_recall_f1(
        expected_human_gates,
        predicted_gates,
    )

    return BenchmarkMetrics(
        recommendation_accuracy=correct / len(decisions),
        mean_ordinal_error=mean(ordinal_errors),
        undercall_rate=undercalls / len(decisions),
        gate_precision=gate_precision,
        gate_recall=gate_recall,
        gate_f1=gate_f1,
        mean_confidence=mean(decision.confidence for decision in decisions),
        evidence_coverage=mean(finding_evidence_coverage(decision) for decision in decisions),
    )
