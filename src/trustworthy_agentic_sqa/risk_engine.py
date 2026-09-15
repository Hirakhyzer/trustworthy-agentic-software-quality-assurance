from __future__ import annotations

from .schema import QualityFinding, Recommendation, RiskLevel


_RISK_WEIGHT = {
    RiskLevel.LOW: 0.2,
    RiskLevel.MEDIUM: 0.6,
    RiskLevel.HIGH: 1.0,
}


def aggregate_risk(findings: list[QualityFinding]) -> tuple[RiskLevel, float]:
    if not findings:
        return RiskLevel.LOW, 0.0

    weighted = sum(_RISK_WEIGHT[f.risk] * max(0.0, min(1.0, f.confidence)) for f in findings)
    total_confidence = sum(max(0.0, min(1.0, f.confidence)) for f in findings)
    score = weighted / total_confidence if total_confidence else 0.0

    if score >= 0.70:
        return RiskLevel.HIGH, score
    if score >= 0.40:
        return RiskLevel.MEDIUM, score
    return RiskLevel.LOW, score


def recommend(risk: RiskLevel, confidence: float) -> Recommendation:
    if risk == RiskLevel.HIGH:
        return Recommendation.BLOCK
    if risk == RiskLevel.MEDIUM or confidence < 0.70:
        return Recommendation.REVIEW
    return Recommendation.APPROVE


def requires_human_approval(risk: RiskLevel, confidence: float) -> bool:
    return risk != RiskLevel.LOW or confidence < 0.80
