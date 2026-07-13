from core.analyzer import Analyzer
from core.provider_selector import ProviderSelector

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


def test_default():

    selector = ProviderSelector()

    assert (
        selector.select(
            build_profile(5000)
        )
        == "gpt-4.1-mini"
    )


def test_low_budget():

    selector = ProviderSelector()

    assert (
        selector.select(
            build_profile(
                5000,
                budget=BudgetLevel.LOW,
            )
        )
        == "gemini-2.5-flash"
    )


def test_large_context():

    selector = ProviderSelector()

    assert (
        selector.select(
            build_profile(100000)
        )
        == "claude-sonnet-4"
    )


def test_complex_reasoning():

    selector = ProviderSelector()

    assert (
        selector.select(
            build_profile(
                5000,
                task="design distributed microservice architecture",
            )
        )
        in [
            "claude-sonnet-4",
            "gpt-4.1-mini",
        ]
    )