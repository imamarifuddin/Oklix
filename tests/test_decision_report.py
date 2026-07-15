from core.decision_report import DecisionReport

from domain import (
    BudgetLevel,
    ExecutionContext,
    LatencyLevel,
    QualityLevel,
    Recommendation,
    TaskComplexity,
    TaskProfile,
    TaskRequest,
    TaskSize,
)


def test_decision_report():

    request = TaskRequest(
        task="Hello",
        estimated_input_tokens=10,
        estimated_output_tokens=100,
    )

    profile = TaskProfile(
        task=request.task,
        total_tokens=110,
        size=TaskSize.SMALL,
        complexity=TaskComplexity.MEDIUM,
        budget=BudgetLevel.MEDIUM,
        quality=QualityLevel.MEDIUM,
        latency=LatencyLevel.NORMAL,
    )

    recommendation = Recommendation(
        strategy="direct_execution",
        provider="openrouter",
        recommended_model="gpt-4.1-mini",
        execution_provider="qwen",
        execution_model="qwen-plus",
        estimated_cost=0.0036,
        estimated_latency_ms=2500,
        confidence=0.90,
        reason="Selected by optimizer.",
        ranking=[],
    )

    context = ExecutionContext(
        profile=profile,
        recommendation=recommendation,
        prompt=request.task,
        execution_provider="qwen",
        execution_model="qwen-plus",
    )

    report = DecisionReport.build(
        request=request,
        profile=profile,
        recommendation=recommendation,
        context=context,
    )

    assert "OKLIX DECISION REPORT" in report
    assert "Hello" in report
    assert "direct_execution" in report
    assert "openrouter" in report
    assert "gpt-4.1-mini" in report
    assert "qwen-plus" in report
    assert "2500 ms" in report
    assert "$0.0036" in report