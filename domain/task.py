"""
Domain model representing an optimization request.
"""

from enum import Enum

from pydantic import BaseModel, Field


class BudgetLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class QualityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class LatencyLevel(str, Enum):
    FAST = "fast"
    NORMAL = "normal"
    SLOW = "slow"


class TaskRequest(BaseModel):
    """
    Request accepted by the optimizer.
    """

    task: str = Field(..., description="Task name")

    estimated_input_tokens: int = Field(
        ...,
        ge=0,
    )

    estimated_output_tokens: int = Field(
        ...,
        ge=0,
    )

    budget: BudgetLevel = BudgetLevel.MEDIUM
    quality: QualityLevel = QualityLevel.MEDIUM
    latency: LatencyLevel = LatencyLevel.NORMAL
