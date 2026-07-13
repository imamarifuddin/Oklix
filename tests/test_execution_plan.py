from domain import ExecutionPlan
from domain import ExecutionStep
from domain.execution_step import StepType


def test_execution_plan():

    plan = ExecutionPlan(
        strategy="direct_execution",
        steps=[
            ExecutionStep(
                order=1,
                type=StepType.EXECUTE,
                description="Execute model",
            )
        ],
        estimated_cost=0.25,
        estimated_latency_ms=1800,
        confidence=0.92,
    )

    assert plan.strategy == "direct_execution"

    assert len(plan.steps) == 1

    assert plan.estimated_cost > 0

    assert plan.estimated_latency_ms > 0

    assert plan.confidence > 0