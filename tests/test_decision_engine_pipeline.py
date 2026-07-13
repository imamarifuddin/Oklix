from core.decision_engine import DecisionEngine

from domain import (
    BudgetLevel,
    LatencyLevel,
    QualityLevel,
    TaskRequest,
)


def build_request():

    return TaskRequest(
        task="summarize_pdf",
        estimated_input_tokens=5000,
        estimated_output_tokens=1000,
        budget=BudgetLevel.MEDIUM,
        quality=QualityLevel.MEDIUM,
        latency=LatencyLevel.NORMAL,
    )


def test_pipeline():

    engine = DecisionEngine()

    result = engine.decide(build_request())

    assert result.recommended_model != ""

    assert result.provider != ""

    assert len(result.ranking) > 0

    assert result.estimated_cost > 0

    assert result.confidence > 0