"""
ASP Response Builder.

Convert a Recommendation into an ASPResponse.
"""

from core.asp.response import ASPResponse

from domain import Recommendation


class ResponseBuilder:
    """
    Build an ASP response from a Recommendation.
    """

    def build(
        self,
        recommendation: Recommendation,
    ) -> ASPResponse:
        """
        Convert a Recommendation into an ASPResponse.
        """

        return ASPResponse(
            strategy=recommendation.strategy,
            recommended_provider=recommendation.provider,
            recommended_model=recommendation.recommended_model,
            execution_provider=recommendation.execution_provider,
            execution_model=recommendation.execution_model,
            estimated_cost=recommendation.estimated_cost,
            estimated_latency_ms=recommendation.estimated_latency_ms,
            confidence=recommendation.confidence,
            reason=recommendation.reason,
        )