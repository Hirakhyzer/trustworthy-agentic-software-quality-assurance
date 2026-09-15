from __future__ import annotations

from .schema import Recommendation, SoftwareChange


def rule_based_baseline(change: SoftwareChange) -> Recommendation:
    """Simple deterministic comparator for controlled experiments."""
    if change.known_failures:
        return Recommendation.BLOCK
    if change.coverage_delta <= -5 or change.complexity_delta >= 10:
        return Recommendation.REVIEW
    if change.changed_modules and not change.tests_changed:
        return Recommendation.REVIEW
    return Recommendation.APPROVE
