from __future__ import annotations

from .quality_agents import (
    CodeQualityAgent,
    DefectAnalysisAgent,
    QualityAgent,
    ReleaseAssuranceAgent,
    RequirementsQAAgent,
    TestStrategyAgent,
)
from .risk_engine import aggregate_risk as calculate_aggregate_risk
from .risk_engine import recommend, requires_human_approval
from .schema import AssuranceDecision, SoftwareChange


class AgenticSQAOrchestrator:
    """Coordinates specialized quality agents and preserves human oversight.

    A custom agent list can be supplied for controlled ablation studies. The
    default configuration preserves the full five-agent research architecture.
    """

    def __init__(self, agents: list[QualityAgent] | None = None) -> None:
        self.agents = agents if agents is not None else [
            RequirementsQAAgent(),
            CodeQualityAgent(),
            TestStrategyAgent(),
            DefectAnalysisAgent(),
            ReleaseAssuranceAgent(),
        ]
        if not self.agents:
            raise ValueError("AgenticSQAOrchestrator requires at least one quality agent")

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
