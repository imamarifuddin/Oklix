from core.asp.response import ASPResponse


def test_response_contains_recommendations_only():

    response = ASPResponse(
        strategy="direct_execution",
        recommended_provider="openai",
        recommended_model="gpt-4.1-mini",
        estimated_cost=0.1,
        estimated_latency_ms=500,
        confidence=0.9,
        reason="lowest cost",
        execution_plan=[
            {
                "type": "provider",
                "provider": "openai",
                "model": "gpt-4.1-mini",
            }
        ],
    )

    assert response.recommended_provider == "openai"
    assert response.execution_plan[0].model == "gpt-4.1-mini"
    assert "execution_model" not in response.model_dump()
