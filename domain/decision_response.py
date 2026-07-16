"""Decision-only response models for Oklix consumers."""

from typing import Literal

from pydantic import BaseModel, Field

from .ranking import RankedModel
from .decision_metrics import CostEstimate, LatencyEstimate, RecommendationExplanation, TradeoffRecommendation


class RecommendedAction(BaseModel):
    """A non-executable action recommended to the caller agent."""

    type: str

    provider: str | None = None

    model: str | None = None


class RecommendationPlan(BaseModel):
    """A non-executable plan that the caller may use to perform a task."""

    type: Literal["recommendation_only"] = "recommendation_only"

    steps: list[RecommendedAction] = Field(default_factory=list)


class RecommendationSummary(BaseModel):
    """The selected strategy and model recommendation."""

    strategy: str
    provider: str
    model: str
    estimated_cost: float
    estimated_latency_ms: int
    confidence: float
    reason: str


class DecisionResponse(BaseModel):
    """Complete Decision Intelligence response returned to caller agents."""

    recommendation_id: str

    recommendation: RecommendationSummary

    ranking: list[RankedModel] = Field(default_factory=list)

    alternatives: list[TradeoffRecommendation] = Field(default_factory=list)

    estimated_cost_detail: CostEstimate

    estimated_latency: LatencyEstimate

    confidence: float

    tradeoffs: list[TradeoffRecommendation] = Field(default_factory=list)

    explanation: RecommendationExplanation

    execution_plan: RecommendationPlan
