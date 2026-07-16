"""API response compatibility model for Decision Intelligence results."""

from domain import DecisionResponse


class ASPResponse(DecisionResponse):
    """Deprecated name for the decision-only API response model."""

    model_config = {
        "json_schema_extra": {
            "example": {
                "strategy": "single_model",
                "recommended_provider": "OpenAI",
                "recommended_model": "gpt-5-mini",
                "estimated_cost": 0.0031,
                "estimated_latency_ms": 720,
                "confidence": 0.96,
                "reason": "Best balance between quality, latency, and cost.",
                "ranking": [],
                "execution_plan": [
                    {
                        "type": "provider",
                        "provider": "OpenAI",
                        "model": "gpt-5-mini",
                    }
                ],
            }
        }
    }
