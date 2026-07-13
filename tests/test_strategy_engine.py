from core.analyzer import Analyzer
from core.strategy_engine import StrategyEngine

from domain import TaskRequest
from domain.task import BudgetLevel


def build_profile(
    tokens: int,
    budget=BudgetLevel.MEDIUM,
    task="summarize",
):
    analyzer = Analyzer()

    return analyzer.analyze(
        TaskRequest(
            task=task,
            estimated_input_tokens=tokens,
            estimated_output_tokens=1000,
            budget=budget,
        )
    )


def test_small():

    engine = StrategyEngine()

    assert (
        engine.recommend(
            build_profile(1000)
        )
        == "direct_execution"
    )


def test_large():

    engine = StrategyEngine()

    assert (
        engine.recommend(
            build_profile(100000)
        )
        == "parallel_chunk_merge"
    )


def test_budget_low():

    engine = StrategyEngine()

    assert (
        engine.recommend(
            build_profile(
                5000,
                budget=BudgetLevel.LOW,
            )
        )
        == "cheap_execution"
    )


def test_complex():

    engine = StrategyEngine()

    assert (
        engine.recommend(
            build_profile(
                5000,
                task="design distributed microservice architecture",
            )
        )
        in [
            "deep_reasoning",
            "direct_execution",
        ]
    )