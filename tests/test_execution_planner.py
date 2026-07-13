from core.analyzer import Analyzer
from core.execution_planner import ExecutionPlanner
from core.optimizer import Optimizer

from domain import TaskRequest


def test_small_execution_plan():

    analyzer = Analyzer()
    optimizer = Optimizer()
    planner = ExecutionPlanner()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=1000,
            estimated_output_tokens=500,
        )
    )

    recommendation = optimizer.optimize(profile)

    plan = planner.build(
        profile,
        recommendation,
    )

    assert len(plan.steps) == 2

    assert plan.steps[0].description != ""

    assert plan.strategy == recommendation.strategy


def test_large_execution_plan():

    analyzer = Analyzer()
    optimizer = Optimizer()
    planner = ExecutionPlanner()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=100000,
            estimated_output_tokens=50000,
        )
    )

    recommendation = optimizer.optimize(profile)

    plan = planner.build(
        profile,
        recommendation,
    )

    assert len(plan.steps) >= 5

    assert plan.steps[0].type.value == "chunk"

    assert plan.steps[-1].type.value == "return"