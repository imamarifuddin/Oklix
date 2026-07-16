from core.experience_engine import ExperienceEngine
from core.asp.request import ASPRequest
from core.asp.request_parser import RequestParser
from core.asp.response import ASPResponse
from core.asp.response_builder import ResponseBuilder
from core.provider_health import ProviderHealthRegistry
from core.recommendation_builder import RecommendationBuilder
from core.recommendation_history import HistoryItem, RecommendationHistory
from uuid import uuid4


class ASPService:
    """
    Application service for Decision Intelligence requests.
    """

    def __init__(self) -> None:

        self.request_parser = RequestParser()

        self.recommendation_builder = RecommendationBuilder()
        self.provider_health = ProviderHealthRegistry()
        self.experience = ExperienceEngine()
        self.history = RecommendationHistory()
        self.recommendation_builder.scoring_engine.health_registry = self.provider_health
        self.recommendation_builder.scoring_engine.experience_engine = self.experience

        self.response_builder = ResponseBuilder()

    def optimize(
        self,
        request: ASPRequest,
    ) -> ASPResponse:
        """
        Build the complete Decision Intelligence response.
        """

        task = self.request_parser.parse(
            request,
        )

        recommendation, profile, scores = self.recommendation_builder.build_with_details(task)

        response = self.response_builder.build(
            recommendation,
            profile,
            scores,
        )
        recommendation_id = str(uuid4())
        response.recommendation["recommendation_id"] = recommendation_id
        self.history.add(
            HistoryItem(
                recommendation_id,
                recommendation.provider,
                recommendation.recommended_model,
                recommendation.confidence,
                recommendation.estimated_cost,
                recommendation.estimated_latency_ms,
            )
        )
        return response

    def feedback(
        self,
        recommendation_id: str,
        success: bool,
        latency: int | None = None,
        actual_cost: float | None = None,
        error: str | None = None,
    ) -> bool:
        """Apply caller-reported outcome feedback to adaptive local state."""
        item = self.history.get(recommendation_id)
        if item is None: return False
        item.success = success
        self.provider_health.record(item.provider, success, latency)
        self.experience.record(item.model, success, latency, actual_cost)
        return True
