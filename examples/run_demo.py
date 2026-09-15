from trustworthy_agentic_sqa import AgenticSQAOrchestrator, SoftwareChange


def main() -> None:
    change = SoftwareChange(
        change_id="demo-001",
        requirements=[
            "The service should be fast and user friendly.",
            "Failed requests must return a traceable error identifier.",
        ],
        changed_modules=["service.py", "validation.py"],
        tests_changed=[],
        known_failures=["integration test intermittently fails on invalid payload"],
        complexity_delta=6.5,
        coverage_delta=-7.0,
    )

    decision = AgenticSQAOrchestrator().assess(change)

    print(f"Change: {decision.change_id}")
    print(f"Recommendation: {decision.recommendation.value}")
    print(f"Aggregate risk: {decision.aggregate_risk.value}")
    print(f"Confidence: {decision.confidence:.2f}")
    print(f"Human approval required: {decision.requires_human_approval}")
    print(decision.explanation)

    print("\nFindings")
    for finding in decision.findings:
        print(f"- {finding.agent}: {finding.risk.value} | {finding.title}")
        for evidence in finding.evidence:
            print(f"    evidence: {evidence.observation}")


if __name__ == "__main__":
    main()
