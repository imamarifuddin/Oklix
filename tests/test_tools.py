from mcp.tools import recommend_strategy


def test_recommend_strategy():

    result = recommend_strategy(
        task="summarize_pdf",
        estimated_input_tokens=5000,
        estimated_output_tokens=1000,
    )

    assert result["strategy"] is not None
    assert result["recommended_model"] is not None
    assert result["estimated_cost"] > 0