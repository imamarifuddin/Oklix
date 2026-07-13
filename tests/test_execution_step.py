from domain import ExecutionStep
from domain.execution_step import StepType


def test_execution_step():

    step = ExecutionStep(
        order=1,
        type=StepType.EXECUTE,
        description="Execute model",
    )

    assert step.order == 1

    assert step.type == StepType.EXECUTE

    assert step.description != ""