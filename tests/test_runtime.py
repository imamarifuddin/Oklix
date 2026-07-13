from core.runtime import Runtime

from domain import (
    ExecutionPlan,
)


def test_runtime():

    runtime = Runtime()

    context = runtime.create_context(

        ExecutionPlan(
            strategy="direct_execution",
            steps=[],
        )

    )

    assert context.metadata["strategy"] == "direct_execution"

    assert len(context.logs) == 1