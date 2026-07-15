from core.asp.response import ASPResponse


def test_response_exists():

    response = ASPResponse(
        strategy="balanced",
        recommended_provider="openai",
        recommended_model="gpt-4.1-mini",
        execution_provider="qwen",
        execution_model="qwen-plus",
        estimated_cost=0.001,
        estimated_latency_ms=900,
        confidence=0.95,
        reason="test",
    )

    assert response is not None


def test_model():

    response = ASPResponse(
        strategy="balanced",
        recommended_provider="openai",
        recommended_model="gpt-4.1-mini",
        execution_provider="qwen",
        execution_model="qwen-plus",
        estimated_cost=0.001,
        estimated_latency_ms=900,
        confidence=0.95,
        reason="test",
    )

    assert response.recommended_model == "gpt-4.1-mini"