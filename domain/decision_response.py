"""Decision-only response models for Oklix consumers."""

from pydantic import BaseModel, Field

from .ranking import RankedModel
from .decision_metrics import CostEstimate, LatencyEstimate, RecommendationExplanation, TradeoffRecommendation


class RecommendedAction(BaseModel):
    """A non-executable action recommended to the caller agent."""

    type: str

    provider: str | None = None

    model: str | None = None

    tool_name: str | None = None


class DecisionResponse(BaseModel):
    """Complete Decision Intelligence response returned to caller agents."""

    strategy: str

    recommended_provider: str

    recommended_model: str

    estimated_cost: float

    estimated_latency_ms: int

    confidence: float

    reason: str

    ranking: list[RankedModel] = Field(default_factory=list)

    execution_plan: list[RecommendedAction] = Field(default_factory=list)

    recommendation: dict = Field(default_factory=dict)

    alternatives: list[TradeoffRecommendation] = Field(default_factory=list)

    explanation: RecommendationExplanation | None = None

    estimated_cost_detail: CostEstimate | None = None

    estimated_latency: LatencyEstimate | None = None

    tradeoffs: list[TradeoffRecommendation] = Field(default_factory=list)
