from __future__ import annotations

from .quality_agents import (
    CodeQualityAgent,
    DefectAnalysisAgent,
    ReleaseAssuranceAgent,
    RequirementsQAAgent,
    TestStrategyAgent,
)
from .risk_engine import aggregate_risk as calculate_aggregate_risk
from .risk_engine import recommend, requires_human_approval
from .schema import AssuranceDecision, SoftwareChange


class AgenticSQAOrchestrator:
    """Coordinates specialized quality agents and preserves human oversight."""

    def __init__(self) -> None:
        self.agents = [
            RequirementsQAAgent(),
            CodeQualityAgent(),
            TestStrategyAgent(),
            DefectAnalysisAgent(),
            ReleaseAssuranceAgent(),
        ]

    def assess(self, change: SoftwareChange) -> AssuranceDecision:
        findings = [agent.analyze(change) for agent in self.agents]
        aggregate_risk, risk_score = calculate_aggregate_risk(findings)
        confidence = sum(f.confidence for f in findings) / len(findings)
        decision = recommend(aggregate_risk, confidence)
        human_gate = requires_human_approval(aggregate_risk, confidence)

        explanation = (
            f"Assessed {len(findings)} quality dimensions. "
            f"Aggregate risk score={risk_score:.2f}; confidence={confidence:.2f}; "
            f"recommendation={decision.value}."
        )

        return AssuranceDecision(
            change_id=change.change_id,
            recommendation=decision,
            aggregate_risk=aggregate_risk,
            confidence=confidence,
            requires_human_approval=human_gate,
            findings=findings,
            explanation=explanation,
        )
