"""
ASP Request.
"""

from pydantic import BaseModel, Field


class ASPRequest(BaseModel):
    """
    Request sent to the Oklix Decision Intelligence engine.
    """

    task: str = Field(
        ...,
        description="Task that should be optimized.",
        examples=["summarize_pdf"],
    )

    budget: str = Field(
        default="medium",
        description="Budget preference.",
        examples=["low"],
    )

    quality: str = Field(
        default="medium",
        description="Desired response quality.",
        examples=["high"],
    )

    latency: str = Field(
        default="normal",
        description="Latency preference.",
        examples=["fast"],
    )

    estimated_input_tokens: int = Field(
        default=0,
        description="Estimated input tokens.",
        examples=[5000],
    )

    estimated_output_tokens: int = Field(
        default=0,
        description="Estimated output tokens.",
        examples=[1000],
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "task": "summarize_pdf",
                "budget": "low",
                "quality": "high",
                "latency": "fast",
                "estimated_input_tokens": 5000,
                "estimated_output_tokens": 1000,
            }
        }
    }