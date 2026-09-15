from __future__ import annotations

from .schema import QualityEvidence, RiskLevel, SoftwareChange


def collect_change_evidence(change: SoftwareChange) -> list[QualityEvidence]:
    evidence: list[QualityEvidence] = []

    if change.known_failures:
        evidence.append(
            QualityEvidence(
                source="known_failures",
                observation=f"{len(change.known_failures)} known failure(s) are associated with the change.",
                severity=RiskLevel.HIGH,
                confidence=0.98,
            )
        )

    if change.coverage_delta < -5:
        evidence.append(
            QualityEvidence(
                source="coverage_delta",
                observation=f"Test coverage decreased by {abs(change.coverage_delta):.1f} percentage points.",
                severity=RiskLevel.HIGH,
                confidence=0.95,
            )
        )
    elif change.coverage_delta < 0:
        evidence.append(
            QualityEvidence(
                source="coverage_delta",
                observation=f"Test coverage decreased by {abs(change.coverage_delta):.1f} percentage points.",
                severity=RiskLevel.MEDIUM,
                confidence=0.90,
            )
        )

    if change.complexity_delta > 10:
        evidence.append(
            QualityEvidence(
                source="complexity_delta",
                observation=f"Complexity increased by {change.complexity_delta:.1f} points.",
                severity=RiskLevel.HIGH,
                confidence=0.90,
            )
        )
    elif change.complexity_delta > 3:
        evidence.append(
            QualityEvidence(
                source="complexity_delta",
                observation=f"Complexity increased by {change.complexity_delta:.1f} points.",
                severity=RiskLevel.MEDIUM,
                confidence=0.85,
            )
        )

    if not change.tests_changed and change.changed_modules:
        evidence.append(
            QualityEvidence(
                source="test_change_trace",
                observation="Production modules changed without corresponding test changes.",
                severity=RiskLevel.MEDIUM,
                confidence=0.80,
            )
        )

    if not evidence:
        evidence.append(
            QualityEvidence(
                source="change_summary",
                observation="No elevated synthetic quality-risk signal was observed.",
                severity=RiskLevel.LOW,
                confidence=0.75,
            )
        )

    return evidence
