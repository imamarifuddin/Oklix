"""
Runtime layer for Oklix.
"""

from domain import ExecutionContext
from domain import ExecutionPlan


class Runtime:
    """
    Runtime environment shared during execution.
    """

    def create_context(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionContext:
        """
        Create a runtime context from an execution plan.
        """

        context = ExecutionContext()

        context.metadata["strategy"] = plan.strategy

        context.logs.append(
            f"Runtime created ({plan.strategy})"
        )

        context.plan = plan

        return context