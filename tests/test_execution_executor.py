from core.execution_executor import ExecutionExecutor

from domain import (
    ExecutionPlan,
    ExecutionStep,
)
from domain.execution_step import StepType


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

    result = executor.execute(
        plan,
    )

    assert result.success is True

    assert result.executed_steps == 2

    assert result.output != ""