"""
Execution Step domain model.
"""

from enum import Enum

from pydantic import BaseModel


class StepType(str, Enum):
    """
    Execution step types.
    """

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