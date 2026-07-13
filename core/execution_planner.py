"""
Execution Planner.
"""

from domain import (
    ExecutionPlan,
    ExecutionStep,
    Recommendation,
    StepType,
    TaskProfile,
)
from domain.profile import TaskSize


class ExecutionPlanner:
    """
    Build an execution plan from the optimizer recommendation.
    """

    def build(
        self,
        profile: TaskProfile,
        recommendation: Recommendation,
    ) -> ExecutionPlan:

        steps: list[ExecutionStep] = []

        if profile.size == TaskSize.LARGE:

            steps.extend(
                [
                    ExecutionStep(
                        order=1,
                        type=StepType.CHUNK,
                        description="Split task into chunks.",
                    ),
                    ExecutionStep(
                        order=2,
                        type=StepType.PARALLEL,
                        description="Execute chunks in parallel.",
                    ),
                    ExecutionStep(
                        order=3,
                        type=StepType.MERGE,
                        description="Merge partial results.",
                    ),
                    ExecutionStep(
                        order=4,
                        type=StepType.VALIDATE,
                        description="Validate merged output.",
                    ),
                    ExecutionStep(
                        order=5,
                        type=StepType.RETURN,
                        description="Return final response.",
                    ),
                ]
            )

        else:

            steps.extend(
                [
                    ExecutionStep(
                        order=1,
                        type=StepType.EXECUTE,
                        description="Execute selected model.",
                    ),
                    ExecutionStep(
                        order=2,
                        type=StepType.RETURN,
                        description="Return response.",
                    ),
                ]
            )

        return ExecutionPlan(
            strategy=recommendation.strategy,
            steps=steps,
            estimated_cost=recommendation.estimated_cost,
            estimated_latency_ms=recommendation.estimated_latency_ms,
            confidence=recommendation.confidence,
        )