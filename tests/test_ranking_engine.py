from core.ranking_engine import RankingEngine

from domain import TaskRequest
from core.analyzer import Analyzer
from core.scoring import ScoringEngine


def build_profile():

    analyzer = Analyzer()

    return analyzer.analyze(
        TaskRequest(
            task="chat",
        )
    )


def test_engine_exists():

    engine = RankingEngine()

    assert engine is not None


def test_rank_returns_list():

    scoring = ScoringEngine()
    engine = RankingEngine()

    profile = build_profile()

    scores = scoring.score_models(profile)

    ranking = engine.build(
        profile,
        scores,
    )

    assert isinstance(
        ranking,
        list,
    )


def test_rank_not_empty():

    scoring = ScoringEngine()
    engine = RankingEngine()

    profile = build_profile()

    scores = scoring.score_models(
        profile,
    )

    ranking = engine.build(
        profile,
        scores,
    )

    assert len(ranking) > 0


def test_first_has_highest_score():

    scoring = ScoringEngine()
    engine = RankingEngine()

    profile = build_profile()

    scores = scoring.score_models(profile)

    ranking = engine.build(
        profile,
        scores,
    )

    best = engine.best(ranking)

    assert best.rank == 1