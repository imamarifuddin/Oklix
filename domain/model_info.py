"""
Metadata describing an AI model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ModelInfo:
    """
    Immutable metadata for an AI model.
    """

    provider: str

    model: str

    context_window: int

    estimated_cost: float

    estimated_latency_ms: int

    confidence: float

    supports_tools: bool

    supports_images: bool

    supports_reasoning: bool

    max_output_tokens: int