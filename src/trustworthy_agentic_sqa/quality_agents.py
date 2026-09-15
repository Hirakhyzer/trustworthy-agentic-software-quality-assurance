from __future__ import annotations

from abc import ABC, abstractmethod

from .evidence import collect_change_evidence
from .schema import QualityFinding, RiskLevel, SoftwareChange


_RISK_ORDER = {RiskLevel.LOW: 0, RiskLevel.MEDIUM: 1, RiskLevel.HIGH: 2}


class QualityAgent(ABC):
    name: str

    @abstractmethod
    def analyze(self, change: SoftwareChange) -> QualityFinding:
        raise NotImplementedError


class RequirementsQAAgent(QualityAgent):
    name = "requirements-qa"

    def analyze(self, change: SoftwareChange) -> QualityFinding:
        vague_terms = ("fast", "easy", "robust", "user friendly", "as needed", "etc.")
        ambiguous = [r for r in change.requirements if any(term in r.lower() for term in vague_terms)]
        risk = RiskLevel.MEDIUM if ambiguous else RiskLevel.LOW
        confidence = 0.84 if ambiguous else 0.72
        rationale = (
            f"Detected {len(ambiguous)} potentially ambiguous requirement(s)."
            if ambiguous
            else "No simple ambiguity heuristic was triggered in the supplied requirements."
        )
        return QualityFinding(self.name, "Requirements quality", rationale, [], confidence, risk)


class CodeQualityAgent(QualityAgent):
    name = "code-quality"

    def analyze(self, change: SoftwareChange) -> QualityFinding:
        evidence = [e for e in collect_change_evidence(change) if e.source == "complexity_delta"]
        risk = max((e.severity for e in evidence), default=RiskLevel.LOW, key=_RISK_ORDER.get)
        rationale = "Complexity evidence reviewed for maintainability risk."
        return QualityFinding(self.name, "Code maintainability", rationale, evidence, 0.88 if evidence else 0.70, risk)


class TestStrategyAgent(QualityAgent):
    name = "test-strategy"

    def analyze(self, change: SoftwareChange) -> QualityFinding:
        evidence = [
            e
            for e in collect_change_evidence(change)
            if e.source in {"coverage_delta", "test_change_trace"}
        ]
        risk = max((e.severity for e in evidence), default=RiskLevel.LOW, key=_RISK_ORDER.get)
        rationale = "Test-change and coverage evidence reviewed for verification adequacy."
        return QualityFinding(self.name, "Test adequacy", rationale, evidence, 0.90 if evidence else 0.72, risk)


class DefectAnalysisAgent(QualityAgent):
    name = "defect-analysis"

    def analyze(self, change: SoftwareChange) -> QualityFinding:
        evidence = [e for e in collect_change_evidence(change) if e.source == "known_failures"]
        risk = RiskLevel.HIGH if evidence else RiskLevel.LOW
        rationale = "Known failure evidence reviewed for unresolved defect risk."
        return QualityFinding(self.name, "Defect evidence", rationale, evidence, 0.97 if evidence else 0.75, risk)


class ReleaseAssuranceAgent(QualityAgent):
    name = "release-assurance"

    def analyze(self, change: SoftwareChange) -> QualityFinding:
        evidence = collect_change_evidence(change)
        risk = max((e.severity for e in evidence), key=_RISK_ORDER.get)
        confidence = sum(e.confidence for e in evidence) / len(evidence)
        return QualityFinding(
            self.name,
            "Release evidence summary",
            "Aggregated observable evidence for release-readiness review.",
            evidence,
            confidence,
            risk,
        )
