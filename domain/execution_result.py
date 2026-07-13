"""
Execution Result domain model.
"""

from pydantic import BaseModel, Field


class ExecutionResult(BaseModel):
    """
    Result produced after executing an execution plan.
    """

    success: bool

    executed_steps: int

    output: str = ""

    metadata: dict[str, str] = Field(
        default_factory=dict,
    )