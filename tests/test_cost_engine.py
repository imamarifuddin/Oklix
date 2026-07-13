from core.analyzer import Analyzer
from core.cost_engine import CostEngine
from core.registry import ModelRegistry

from domain import TaskRequest


def test_cost_positive():

    analyzer = Analyzer()

    registry = ModelRegistry()

    engine = CostEngine()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=5000,
            estimated_output_tokens=1000,
        )
    )

    capability = registry.get("gpt-4.1-mini")

    cost = engine.estimate(
        profile,
        capability,
    )

    assert cost > 0


def test_cost_matches():

    analyzer = Analyzer()

    registry = ModelRegistry()

    engine = CostEngine()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=5000,
            estimated_output_tokens=1000,
        )
    )

    capability = registry.get("gpt-4.1-mini")

    assert engine.estimate(
        profile,
        capability,
    ) == 0.021