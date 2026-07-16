"""Structured decision metrics returned by Decision Intelligence engines."""

from pydantic import BaseModel, Field


class CostEstimate(BaseModel):
    """Explainable estimate of the cost recommended to a caller agent."""

    input_tokens: int
    output_tokens: int
    cached_tokens: int
    input_cost: float
    output_cost: float
    cached_cost: float
    total_cost: float
    calculation: str


class LatencyEstimate(BaseModel):
    """Latency estimate with a confidence interval for a recommendation."""

    expected_ms: int
    lower_bound_ms: int
    upper_bound_ms: int
    confidence: float
    factors: dict[str, float] = Field(default_factory=dict)


class RecommendationExplanation(BaseModel):
    """Machine-readable justification for a selected recommendation."""

    summary: str
    reasons: list[str] = Field(default_factory=list)
    confidence: float
    factors: dict[str, float] = Field(default_factory=dict)


class TradeoffRecommendation(BaseModel):
    """Alternative recommendation optimized for a named preference."""

    category: str
    provider: str
    model: str
    justification: str
    score: float
