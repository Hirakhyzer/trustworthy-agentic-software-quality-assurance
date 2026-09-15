from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Recommendation(str, Enum):
    APPROVE = "approve"
    REVIEW = "review"
    BLOCK = "block"


@dataclass(frozen=True)
class QualityEvidence:
    source: str
    observation: str
    severity: RiskLevel
    confidence: float


@dataclass
class QualityFinding:
    agent: str
    title: str
    rationale: str
    evidence: List[QualityEvidence] = field(default_factory=list)
    confidence: float = 0.0
    risk: RiskLevel = RiskLevel.LOW


@dataclass
class SoftwareChange:
    change_id: str
    requirements: List[str]
    changed_modules: List[str]
    tests_changed: List[str]
    known_failures: List[str]
    complexity_delta: float = 0.0
    coverage_delta: float = 0.0


@dataclass
class AssuranceDecision:
    change_id: str
    recommendation: Recommendation
    aggregate_risk: RiskLevel
    confidence: float
    requires_human_approval: bool
    findings: List[QualityFinding]
    explanation: str
