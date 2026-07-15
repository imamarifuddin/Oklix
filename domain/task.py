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
    Incoming task request.
    """

    task: str

    estimated_input_tokens: int = 0

    estimated_output_tokens: int = 0

    budget: BudgetLevel = BudgetLevel.MEDIUM
    quality: QualityLevel = QualityLevel.MEDIUM
    latency: LatencyLevel = LatencyLevel.NORMAL
