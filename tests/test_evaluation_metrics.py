from trustworthy_agentic_sqa.evaluation import (
    decision_consistency,
    finding_evidence_coverage,
    is_undercall,
    ordinal_recommendation_error,
    summarize_benchmark,
)
from trustworthy_agentic_sqa.schema import (
    AssuranceDecision,
    QualityEvidence,
    QualityFinding,
    Recommendation,
    RiskLevel,
)


def make_decision(
    recommendation: Recommendation,
    *,
    confidence: float = 0.8,
    human_gate: bool = False,
    supported_findings: int = 1,
    total_findings: int = 1,
) -> AssuranceDecision:
    findings = []
    for index in range(total_findings):
        evidence = []
        if index < supported_findings:
            evidence = [
                QualityEvidence(
                    source="synthetic-test",
                    observation="controlled evidence",
                    severity=RiskLevel.MEDIUM,
                    confidence=0.9,
                )
            ]
        findings.append(
            QualityFinding(
                agent=f"agent-{index}",
                title="Synthetic finding",
                rationale="Used for evaluation tests.",
                evidence=evidence,
                confidence=confidence,
                risk=RiskLevel.MEDIUM,
            )
        )

    return AssuranceDecision(
        change_id="synthetic",
        recommendation=recommendation,
        aggregate_risk=RiskLevel.MEDIUM,
        confidence=confidence,
        requires_human_approval=human_gate,
        findings=findings,
        explanation="synthetic decision",
    )


def test_ordinal_error_distinguishes_adjacent_and_two_step_misses() -> None:
    assert ordinal_recommendation_error(Recommendation.REVIEW, Recommendation.BLOCK) == 1
    assert ordinal_recommendation_error(Recommendation.APPROVE, Recommendation.BLOCK) == 2
    assert ordinal_recommendation_error(Recommendation.BLOCK, Recommendation.BLOCK) == 0


def test_undercall_flags_less_conservative_predictions() -> None:
    assert is_undercall(Recommendation.APPROVE, Recommendation.REVIEW) is True
    assert is_undercall(Recommendation.APPROVE, Recommendation.BLOCK) is True
    assert is_undercall(Recommendation.BLOCK, Recommendation.REVIEW) is False


def test_finding_evidence_coverage_is_fraction_supported() -> None:
    decision = make_decision(
        Recommendation.REVIEW,
        supported_findings=2,
        total_findings=4,
    )
    assert finding_evidence_coverage(decision) == 0.5


def test_summary_reports_accuracy_safety_and_gate_metrics() -> None:
    decisions = [
        make_decision(Recommendation.APPROVE, confidence=0.9, human_gate=False),
        make_decision(Recommendation.REVIEW, confidence=0.8, human_gate=True),
        make_decision(Recommendation.APPROVE, confidence=0.7, human_gate=False),
        make_decision(Recommendation.BLOCK, confidence=0.6, human_gate=True),
    ]
    expected = [
        Recommendation.APPROVE,
        Recommendation.REVIEW,
        Recommendation.BLOCK,
        Recommendation.BLOCK,
    ]
    expected_gates = [False, True, True, True]

    metrics = summarize_benchmark(decisions, expected, expected_gates)

    assert metrics.recommendation_accuracy == 0.75
    assert metrics.mean_ordinal_error == 0.5
    assert metrics.undercall_rate == 0.25
    assert metrics.gate_precision == 1.0
    assert metrics.gate_recall == 2 / 3
    assert metrics.gate_f1 == 0.8
    assert metrics.mean_confidence == 0.75
    assert metrics.evidence_coverage == 1.0


def test_decision_consistency_measures_repeated_run_agreement() -> None:
    decisions = [
        make_decision(Recommendation.REVIEW),
        make_decision(Recommendation.REVIEW),
        make_decision(Recommendation.BLOCK),
    ]
    assert decision_consistency(decisions) == 2 / 3
