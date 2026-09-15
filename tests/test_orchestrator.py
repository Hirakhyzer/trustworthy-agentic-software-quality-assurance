from trustworthy_agentic_sqa import AgenticSQAOrchestrator, Recommendation, RiskLevel, SoftwareChange


def test_high_risk_change_is_blocked_and_escalated() -> None:
    change = SoftwareChange(
        change_id="risk-001",
        requirements=["The system must return a deterministic validation result."],
        changed_modules=["core.py"],
        tests_changed=[],
        known_failures=["regression test fails"],
        complexity_delta=12.0,
        coverage_delta=-8.0,
    )

    decision = AgenticSQAOrchestrator().assess(change)

    assert decision.aggregate_risk == RiskLevel.HIGH
    assert decision.recommendation == Recommendation.BLOCK
    assert decision.requires_human_approval is True


def test_low_risk_change_can_be_approved() -> None:
    change = SoftwareChange(
        change_id="risk-002",
        requirements=["The API must return HTTP 200 for valid requests."],
        changed_modules=["api.py"],
        tests_changed=["test_api.py"],
        known_failures=[],
        complexity_delta=0.5,
        coverage_delta=2.0,
    )

    decision = AgenticSQAOrchestrator().assess(change)

    assert decision.aggregate_risk == RiskLevel.LOW
    assert decision.recommendation == Recommendation.APPROVE


def test_orchestrator_produces_all_agent_findings() -> None:
    change = SoftwareChange(
        change_id="risk-003",
        requirements=["A trace identifier must be stored for each failed request."],
        changed_modules=["logging.py"],
        tests_changed=["test_logging.py"],
        known_failures=[],
    )

    decision = AgenticSQAOrchestrator().assess(change)

    assert len(decision.findings) == 5
    assert {f.agent for f in decision.findings} == {
        "requirements-qa",
        "code-quality",
        "test-strategy",
        "defect-analysis",
        "release-assurance",
    }
