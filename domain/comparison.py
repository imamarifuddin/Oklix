"""
Comparison result.
"""

from pydantic import BaseModel

from domain.ranking import RankedModel


class ModelComparison(BaseModel):
    """Comparison between candidate models."""

    decision_profile: str

    recommended_model: str

    ranking: list[RankedModel]