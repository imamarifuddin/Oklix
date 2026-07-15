"""
Execution Executor.
"""

from core.provider_router import ProviderRouter
from core.providers import ProviderRegistry

from domain import (
    ExecutionContext,
    ExecutionPlan,
    ExecutionResult,
    StepType,
)


class ExecutionExecutor:
    """
    Execute an execution plan.
    """

    def __init__(self) -> None:

        registry = ProviderRegistry()

        self.router = ProviderRouter(registry)

    def execute(
        self,
        plan: ExecutionPlan,
        context: ExecutionContext,
    ) -> ExecutionResult:
        """
        Execute executable steps.
        """

        provider = self.router.resolve(
            context.recommendation,
        )

        output = ""

        executed_steps = 0

        for step in plan.steps:

            executed_steps += 1

            if step.type not in (
                StepType.EXECUTE,
                StepType.PARALLEL,
            ):
                continue

            if not step.prompt:

                output = step.description

                continue

            output = provider.chat(
                prompt=step.prompt,
                system_prompt=step.system_prompt,
                model=context.execution_model,
            )

        return ExecutionResult(
            success=True,
            executed_steps=executed_steps,
            output=output or "Execution completed.",
        )
    
    def execute_context(
        self,
        context,
    ):
        """
        Execute from ExecutionContext.
        """

        if context.plan is None:
            raise ValueError(
               "ExecutionContext has no execution plan."
            )

        return self.execute(
            context.plan,
            context,
        )