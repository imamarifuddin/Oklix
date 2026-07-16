from core.recommendation_builder import RecommendationBuilder
from domain import DecisionResponse, TaskRequest


def test_response_is_decision_response_v2():
    """The core response model is recommendation-only and fully structured."""

    response = RecommendationBuilder().build(TaskRequest(task="chat"), "response-id")

    assert isinstance(response, DecisionResponse)
    assert response.recommendation.model
    assert response.execution_plan.type == "recommendation_only"
    assert response.execution_plan.steps[0].provider == response.recommendation.provider
