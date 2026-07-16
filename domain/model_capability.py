"""
Model Capability domain model.
"""

from pydantic import BaseModel, Field


class ModelCapability(BaseModel):
    """
    AI model capability description.
    """

    name: str

    provider: str

    quality: str

    speed: str

    latency_ms: int

    cost_per_100k_tokens: float

    context_window: int

    max_output_tokens: int

    supports: dict[str, bool] = Field(default_factory=dict)

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    capabilities: dict[str, float] = Field(default_factory=dict)

    input_cost_per_1m_tokens: float | None = None

    output_cost_per_1m_tokens: float | None = None

    cached_cost_per_1m_tokens: float | None = None
