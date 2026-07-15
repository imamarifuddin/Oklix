"""
ASP Response.
"""

from pydantic import BaseModel


class ASPResponse(BaseModel):
    """
    Response returned by the ASP layer.
    """

    strategy: str

    recommended_provider: str

    recommended_model: str

    execution_provider: str

    execution_model: str

    estimated_cost: float

    estimated_latency_ms: int

    confidence: float

    reason: str