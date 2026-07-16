from core.asp.response_builder import ResponseBuilder
from core.recommendation_builder import RecommendationBuilder
from domain import DecisionResponse, TaskRequest


def test_builder_exists():

    builder = ResponseBuilder()

    assert builder is not None


def test_build():

    builder = ResponseBuilder()

    response = builder.build(
        RecommendationBuilder().build(TaskRequest(task="chat"), "builder-test-id")
    )

    assert isinstance(response, DecisionResponse)


def test_model():

    builder = ResponseBuilder()

    response = builder.build(
        RecommendationBuilder().build(TaskRequest(task="chat"), "model-test-id")
    )

    assert response.recommendation.model
    assert response.recommendation_id == "model-test-id"
