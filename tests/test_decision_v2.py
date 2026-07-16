from core.analyzer import Analyzer
from core.capability_engine import CapabilityEngine
from core.cost_engine import CostEngine
from core.explanation_engine import RecommendationExplanationEngine
from core.latency_engine import LatencyEngine
from core.registry import ModelRegistry
from core.scoring import ScoringEngine
from core.tradeoff_engine import TradeoffEngine
from domain import TaskRequest


def build_profile():
    """Build a representative profile for v2 engine tests."""

    return Analyzer().analyze(
        TaskRequest(
            task="reason about code",
            estimated_input_tokens=8_000,
            estimated_output_tokens=2_000,
        )
    )


def test_normalized_capabilities_expose_all_decision_dimensions():

    capabilities = CapabilityEngine().normalized("gpt-4.1-mini")

    assert set(capabilities) == {
        "reasoning", "coding", "math", "long_context", "vision",
        "tool_use", "instruction_following", "speed", "reliability",
    }
    assert all(0 <= value <= 1 for value in capabilities.values())


def test_cost_and_latency_v2_are_explainable():

    profile = build_profile()
    capability = ModelRegistry().get("gpt-4.1-mini")

    cost = CostEngine().estimate_detailed(profile, capability, cached_tokens=500)
    latency = LatencyEngine().estimate(profile, capability)

    assert cost.total_cost == cost.input_cost + cost.output_cost + cost.cached_cost
    assert "pricing" in cost.calculation
    assert latency.lower_bound_ms < latency.expected_ms < latency.upper_bound_ms


def test_scoring_explanations_and_tradeoffs_are_machine_readable():

    profile = build_profile()
    scores = ScoringEngine().score_models(profile)
    from core.ranking_engine import RankingEngine
    ranking = RankingEngine().build(profile, scores)

    explanation = RecommendationExplanationEngine().explain(ranking[0], scores[0])
    tradeoffs = TradeoffEngine().build(ranking)

    assert scores[0].weights
    assert scores[0].factors
    assert "reasoning" in scores[0].bonuses
    assert explanation.reasons
    assert {item.category for item in tradeoffs} >= {"Balanced", "Cheapest", "Fastest"}
