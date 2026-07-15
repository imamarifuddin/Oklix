"""
Execution Step domain model.
"""

from enum import Enum

from pydantic import BaseModel


class StepType(str, Enum):

    CHUNK = "chunk"

    EXECUTE = "execute"

    PARALLEL = "parallel"

    MERGE = "merge"

    VALIDATE = "validate"

    RETURN = "return"


class ExecutionStep(BaseModel):
    """
    A single execution step.
    """

    order: int

    type: StepType

    description: str

    provider: str | None = None

    model: str | None = None

    prompt: str = ""

    system_prompt: str = ""