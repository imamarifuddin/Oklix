"""
Execution context shared across the pipeline.
"""

from pydantic import BaseModel
from pydantic import Field

from domain import Recommendation
from domain import TaskProfile
from domain import ExecutionPlan

class ExecutionContext(BaseModel):
    """
    Shared runtime context.
    """

    #
    # New pipeline
    #

    profile: TaskProfile | None = None

    recommendation: Recommendation | None = None

    prompt: str = ""

    plan: ExecutionPlan | None = None

    execution_provider: str | None = None

    execution_model: str | None = None

    #
    # Runtime state
    #

    metadata: dict = Field(default_factory=dict)

    logs: list[str] = Field(default_factory=list)