"""
Ranking models.
"""

from pydantic import BaseModel


class RankedModel(BaseModel):
    """Single ranked model."""

    rank: int

    model: str

    provider: str

    score: float

    estimated_cost: float

    estimated_latency_ms: int

    strength: str