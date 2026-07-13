from pydantic import BaseModel, Field

from domain.ranking import RankedModel


class Recommendation(BaseModel):
    strategy: str

    recommended_model: str

    provider: str

    estimated_cost: float

    estimated_latency_ms: int

    confidence: float

    reason: str

    ranking: list[RankedModel] = Field(default_factory=list)