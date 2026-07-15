from core.asp.response import ASPResponse
from core.asp.response_builder import ResponseBuilder

from domain import Recommendation


def test_builder_exists():

    builder = ResponseBuilder()

    assert builder is not None


def test_build():

    builder = ResponseBuilder()

    recommendation = Recommendation(
        strategy="balanced",
        provider="openai",
        recommended_model="gpt-4.1-mini",
        execution_provider="qwen",
        execution_model="qwen-plus",
        estimated_cost=0.001,
        estimated_latency_ms=900,
        confidence=0.95,
        reason="test",
    )

    response = builder.build(
        recommendation,
    )

    assert isinstance(
        response,
        ASPResponse,
    )


def test_model():

    builder = ResponseBuilder()

    recommendation = Recommendation(
        strategy="balanced",
        provider="openai",
        recommended_model="gpt-4.1-mini",
        execution_provider="qwen",
        execution_model="qwen-plus",
        estimated_cost=0.001,
        estimated_latency_ms=900,
        confidence=0.95,
        reason="test",
    )

    response = builder.build(
        recommendation,
    )

    assert response.recommended_model == "gpt-4.1-mini"