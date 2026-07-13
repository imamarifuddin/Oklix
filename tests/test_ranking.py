from core.analyzer import Analyzer
from core.ranking import RankingEngine
from core.scoring import ScoringEngine
from domain import TaskRequest


def build_profile():
    analyzer = Analyzer()

    return analyzer.analyze(
        TaskRequest(
            task="summarize_pdf",
            estimated_input_tokens=5000,
            estimated_output_tokens=1000,
        )
    )


def build_ranking():
    profile = build_profile()

    scoring = ScoringEngine()

    scores = scoring.score_models(profile)

    ranking = RankingEngine().build(
        profile,
        scores,
    )

    return ranking


def test_ranking_not_empty():

    ranking = build_ranking()

    assert len(ranking) > 0


def test_first_rank():

    ranking = build_ranking()

    assert ranking[0].rank == 1


def test_sorted():

    ranking = build_ranking()

    assert ranking[0].score >= ranking[1].score


def test_provider_exists():

    ranking = build_ranking()

    assert ranking[0].provider != ""


def test_strength_exists():

    ranking = build_ranking()

    assert ranking[0].strength != ""