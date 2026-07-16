"""
ASP Response Builder.

Convert a Recommendation into an ASPResponse.
"""

from core.asp.response import ASPResponse
from core.cost_engine import CostEngine
from core.explanation_engine import RecommendationExplanationEngine
from core.latency_engine import LatencyEngine
from core.registry import ModelRegistry
from core.tradeoff_engine import TradeoffEngine

from domain import RecommendedAction, Recommendation


class ResponseBuilder:
    """
    Build an ASP response from a Recommendation.
    """

    def build(
        self,
        recommendation: Recommendation,
        profile=None,
        scores: list | None = None,
    ) -> ASPResponse:
        """
        Convert a Recommendation into an ASPResponse.
        """

        capability = ModelRegistry().get(recommendation.recommended_model)
        score = next(
            (item for item in scores or [] if item.name == recommendation.recommended_model),
            None,
        )
        cost_detail = CostEngine().estimate_detailed(profile, capability) if profile else None
        latency = LatencyEngine().estimate(profile, capability) if profile else None
        explanation = (
            RecommendationExplanationEngine().explain(
                recommendation.ranking[0], score,
            )
            if recommendation.ranking and score is not None
            else None
        )
        tradeoffs = TradeoffEngine().build(recommendation.ranking)

        return ASPResponse(
            strategy=recommendation.strategy,
            recommended_provider=recommendation.provider,
            recommended_model=recommendation.recommended_model,
            estimated_cost=recommendation.estimated_cost,
            estimated_latency_ms=recommendation.estimated_latency_ms,
            confidence=recommendation.confidence,
            reason=recommendation.reason,
            ranking=recommendation.ranking,
            execution_plan=[
                RecommendedAction(
                    type="provider",
                    provider=recommendation.provider,
                    model=recommendation.recommended_model,
                )
            ],
            recommendation={
                "provider": recommendation.provider,
                "model": recommendation.recommended_model,
                "strategy": recommendation.strategy,
            },
            alternatives=tradeoffs,
            explanation=explanation,
            estimated_cost_detail=cost_detail,
            estimated_latency=latency,
            tradeoffs=tradeoffs,
        )
