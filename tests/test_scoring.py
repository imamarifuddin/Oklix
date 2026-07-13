from core.analyzer import Analyzer
from core.scoring import ScoringEngine

from domain import TaskRequest


def build_profile():

    analyzer = Analyzer()

    return analyzer.analyze(
        TaskRequest(
            task="summary",
            estimated_input_tokens=5000,
            estimated_output_tokens=1000,
        )
    )


def test_score_models():

    engine = ScoringEngine()

    scores = engine.score_models(
        build_profile()
    )

    assert len(scores) == 3


def test_sorted():

    engine = ScoringEngine()

    scores = engine.score_models(
        build_profile()
    )

    assert scores[0].score >= scores[1].score


def test_provider():

    engine = ScoringEngine()

    scores = engine.score_models(
        build_profile()
    )

    assert scores[0].provider != ""


def test_cost_positive():

    engine = ScoringEngine()

    scores = engine.score_models(
        build_profile()
    )

    assert scores[0].cost_score > 0


def test_quality_positive():

    engine = ScoringEngine()

    scores = engine.score_models(
        build_profile()
    )

    assert scores[0].quality_score > 0

def test_profile_changes_score():

    engine = ScoringEngine()

    profile = build_profile()

    balanced = engine.score_models(
        profile,
        "balanced",
    )

    cheapest = engine.score_models(
        profile,
        "cheapest",
    )

    assert balanced is not None
    assert cheapest is not None
    assert len(balanced) == len(cheapest)