"""
Execution Runtime.
"""

from domain import (
    ExecutionContext,
    ExecutionPlan,
)


class Runtime:
    """
    Runtime responsible for executing plans.
    """

    def create_context(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionContext:

        context = ExecutionContext()

        context.metadata["strategy"] = plan.strategy

        context.log(
            f"Runtime created for strategy '{plan.strategy}'"
        )

        return context