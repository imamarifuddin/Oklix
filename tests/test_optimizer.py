from core.analyzer import Analyzer
from core.optimizer import Optimizer

from domain import TaskRequest
from domain.profile import TaskSize
from domain.task import BudgetLevel


def build_profile(
    tokens: int,
    budget=BudgetLevel.MEDIUM,
):
    analyzer = Analyzer()

    return analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=tokens,
            estimated_output_tokens=1000,
            budget=budget,
        )
    )


def test_strategy_small():
    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile(1000)
    )

    assert recommendation.strategy == "direct_execution"


def test_strategy_large():
    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile(100000)
    )

    assert recommendation.strategy == "parallel_chunk_merge"


def test_budget_low():
    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile(
            5000,
            budget=BudgetLevel.LOW,
        )
    )

    assert recommendation.recommended_model == "gemini-2.5-flash"


def test_cost_positive():
    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile(5000)
    )

    assert recommendation.estimated_cost > 0


def test_latency_large():
    analyzer = Analyzer()
    optimizer = Optimizer()

    profile = analyzer.analyze(
        TaskRequest(
            task="summary",
            estimated_input_tokens=100000,
            estimated_output_tokens=5000,
        )
    )

    assert profile.size == TaskSize.LARGE

    recommendation = optimizer.optimize(profile)

    assert recommendation.estimated_latency_ms == 5000


def test_confidence():
    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile(5000)
    )

    assert recommendation.confidence == 0.90


def test_reason_exists():
    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile(5000)
    )

    assert recommendation.reason != ""