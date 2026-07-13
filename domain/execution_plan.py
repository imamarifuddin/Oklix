"""
Execution Plan domain model.
"""

from pydantic import BaseModel, Field

from .execution_step import ExecutionStep


class ExecutionPlan(BaseModel):
    """
    Complete execution plan produced by the planner.
    """

    strategy: str

    steps: list[ExecutionStep] = Field(
        default_factory=list,
    )

    estimated_cost: float = 0.0

    estimated_latency_ms: int = 0

    confidence: float = 0.0