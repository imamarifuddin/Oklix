from pydantic import BaseModel, Field


class FeedbackRequest(BaseModel):
    """Caller-reported recommendation outcome used for adaptation."""
    recommendation_id: str = Field(..., description="Identifier returned with the recommendation")
    executed: bool = Field(True, description="Whether the caller acted on the recommendation")
    success: bool = Field(..., description="Whether the caller-reported execution succeeded")
    latency: int | None = Field(None, ge=0, description="Observed latency in milliseconds")
    actual_cost: float | None = Field(None, ge=0, description="Observed cost in the caller's currency unit")
    error: str | None = Field(None, description="Caller-reported error summary")
