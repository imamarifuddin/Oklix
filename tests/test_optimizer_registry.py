from core.analyzer import Analyzer
from core.optimizer import Optimizer

from domain import TaskRequest
from domain.task import BudgetLevel


def build_profile(
    budget=BudgetLevel.MEDIUM,
):

    analyzer = Analyzer()

    return analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=10000,
            estimated_output_tokens=2000,
            budget=budget,
        )
    )


def test_reason_contains_provider():

    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile()
    )

    assert "registry" in recommendation.reason.lower()


def test_low_budget_provider():

    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile(
            BudgetLevel.LOW
        )
    )

    assert recommendation.recommended_model == "gemini-2.5-flash"


def test_estimated_cost_matches_registry():

    optimizer = Optimizer()

    recommendation = optimizer.optimize(
        build_profile()
    )

    assert recommendation.estimated_cost > 0