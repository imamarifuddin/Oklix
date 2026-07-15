from core.asp.response import ASPResponse


def test_response():

    response = ASPResponse(
        strategy="direct_execution",

        recommended_provider="openai",
        recommended_model="gpt-4.1-mini",

        execution_provider="qwen",
        execution_model="qwen-plus",

        estimated_cost=0.1,
        estimated_latency_ms=500,
        confidence=0.9,

        reason="lowest cost",
    )

    assert response.recommended_provider == "openai"

    assert response.recommended_model == "gpt-4.1-mini"

    assert response.execution_provider == "qwen"

    assert response.execution_model == "qwen-plus"