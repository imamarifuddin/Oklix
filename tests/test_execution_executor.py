from core.execution_executor import ExecutionExecutor

from domain import (
    BudgetLevel,
    ExecutionContext,
    ExecutionPlan,
    ExecutionStep,
    Recommendation,
    StepType,
    TaskComplexity,
    TaskProfile,
    TaskSize,
    QualityLevel,
    LatencyLevel,
)


def test_execute_plan():

    executor = ExecutionExecutor()

    plan = ExecutionPlan(
        strategy="direct_execution",
        steps=[
            ExecutionStep(
                order=1,
                type=StepType.EXECUTE,
                description="Execute model",
            ),
            ExecutionStep(
                order=2,
                type=StepType.RETURN,
                description="Return result",
            ),
        ],
    )

    profile = TaskProfile(
        task="Hello",
        total_tokens=100,
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
        estimated_cost=0.01,
        estimated_latency_ms=500,
        confidence=0.95,
    )

    context = ExecutionContext(
        profile=profile,
        recommendation=recommendation,
        prompt="Hello",
        execution_provider="qwen",
        execution_model="qwen-plus",
    )

    result = executor.execute(
        plan,
        context,
    )

    assert result.success

    assert result.executed_steps == 2