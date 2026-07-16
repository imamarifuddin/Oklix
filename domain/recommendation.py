from pydantic import BaseModel, Field

from .ranking import RankedModel


class Recommendation(BaseModel):
    """
    Recommendation produced by the optimizer.
    """

    # Decision Engine recommendation
    strategy: str

    provider: str

    recommended_model: str

    estimated_cost: float

    estimated_latency_ms: int

    confidence: float

    reason: str = ""

    ranking: list[RankedModel] = Field(default_factory=list)
