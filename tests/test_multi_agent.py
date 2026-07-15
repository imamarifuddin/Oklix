from core.multi_agent import MultiAgent

from domain import (
    ExecutionContext,
    Recommendation,
    TaskProfile,
    TaskSize,
    TaskComplexity,
    BudgetLevel,
    QualityLevel,
    LatencyLevel,
)


class DummyAgent:

    def execute(
        self,
        context,
    ):
        return "done"


def test_multi_agent():

    profile = TaskProfile(
        task="hello",
        total_tokens=10,
        size=TaskSize.SMALL,
        complexity=TaskComplexity.LOW,
        budget=BudgetLevel.MEDIUM,
        quality=QualityLevel.MEDIUM,
        latency=LatencyLevel.NORMAL,
    )

    recommendation = Recommendation(
        strategy="direct_execution",
        provider="qwen",
        recommended_model="qwen-plus",
        execution_provider="qwen",
        execution_model="qwen-plus",
        estimated_cost=0.0,
        estimated_latency_ms=100,
        confidence=1.0,
    )

    context = ExecutionContext(
        profile=profile,
        recommendation=recommendation,
        prompt="hello",
    )

    orchestrator = MultiAgent()

    orchestrator.register(
        "executor",
        DummyAgent(),
    )

    result = orchestrator.execute(
        "executor",
        context,
    )

    assert result == "done"