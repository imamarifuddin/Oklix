from core.recommendation_builder import RecommendationBuilder

from domain import TaskRequest


def test_builder_exists():

    builder = RecommendationBuilder()

    assert builder is not None


def test_build():

    builder = RecommendationBuilder()

    recommendation = builder.build(
        TaskRequest(
            task="chat",
        )
    )

    assert recommendation.provider != ""
    assert recommendation.recommended_model != ""
    assert recommendation.reason
