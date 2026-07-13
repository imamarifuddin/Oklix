"""
Internal task profile produced by the Analyzer.
"""

from enum import Enum

from pydantic import BaseModel

from domain.task import (
    BudgetLevel,
    LatencyLevel,
    QualityLevel,
)


class TaskSize(str, Enum):
    """Estimated task size based on total tokens."""

    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class TaskComplexity(str, Enum):
    """Estimated task complexity."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskProfile(BaseModel):
    """
    Internal normalized representation of a task.

    This object is produced by the Analyzer and consumed by
    the Optimizer and Decision Engine.
    """

    task: str

    total_tokens: int

    size: TaskSize

    complexity: TaskComplexity

    budget: BudgetLevel

    quality: QualityLevel

    latency: LatencyLevel