from core.cost_estimator import CostEstimator

from domain import (
    BudgetLevel,
    LatencyLevel,
    QualityLevel,
    TaskComplexity,
    TaskProfile,
    TaskSize,
)


def build_profile(tokens: int) -> TaskProfile:
    return TaskProfile(
        task="summarize_pdf",
        total_tokens=tokens,
        size=TaskSize.SMALL if tokens < 8000 else TaskSize.MEDIUM,
        complexity=TaskComplexity.LOW,
        budget=BudgetLevel.MEDIUM,
        quality=QualityLevel.MEDIUM,
        latency=LatencyLevel.NORMAL,
    )


def test_cost_positive():
    estimator = CostEstimator()

    profile = build_profile(6000)

    cost = estimator.estimate(
        profile,
        0.30,
    )

    assert cost > 0


def test_cost_small():
    estimator = CostEstimator()

    profile = build_profile(2000)

    cost = estimator.estimate(
        profile,
        0.30,
    )

    assert cost < 1