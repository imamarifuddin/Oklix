from core.recommendation_builder import RecommendationBuilder

from domain import DecisionResponse, TaskRequest


def test_builder_exists():

    builder = RecommendationBuilder()

    assert builder is not None


def test_build():

    builder = RecommendationBuilder()

    response = builder.build(
        TaskRequest(
            task="chat",
        ),
        "recommendation-test-id",
    )

    assert isinstance(response, DecisionResponse)
    assert response.recommendation_id == "recommendation-test-id"
    assert response.recommendation.provider
    assert response.ranking
    assert response.tradeoffs
    assert response.explanation.reasons
    assert response.estimated_cost_detail.total_cost >= 0
    assert response.estimated_latency.lower_bound_ms > 0
    assert response.execution_plan.type == "recommendation_only"
