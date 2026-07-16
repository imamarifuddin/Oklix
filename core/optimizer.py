"""
Optimizer.
"""

from core.cost_engine import CostEngine
from core.provider_selector import ProviderSelector
from core.ranking_engine import RankingEngine
from core.registry import ModelRegistry
from core.scoring import ScoringEngine
from core.strategy_engine import StrategyEngine

from domain import Recommendation
from domain import TaskProfile


class Optimizer:
    """
    Optimization orchestrator.
    """

    def __init__(self) -> None:

        self.registry = ModelRegistry()

        self.strategy_engine = StrategyEngine()
        self.provider_selector = ProviderSelector()

        self.cost_engine = CostEngine()

        self.scoring_engine = ScoringEngine()

        self.ranking_engine = RankingEngine()

    def optimize(
        self,
        profile: TaskProfile,
    ) -> Recommendation:
        """
        Run the recommendation pipeline.
        """

        # --------------------------------------------------
        # Strategy
        # --------------------------------------------------

        strategy = self.strategy_engine.recommend(
            profile,
        )

        model_name = self.provider_selector.select(profile)

        capability = self.registry.get(model_name)

        estimated_cost = self.cost_engine.estimate(
            profile,
            capability,
        )

        scores = self.scoring_engine.score_models(profile)
        ranking = self.ranking_engine.build(profile, scores)

        return Recommendation(
            strategy=strategy,
            provider=capability.provider,
            recommended_model=capability.name,
            estimated_cost=estimated_cost,
            estimated_latency_ms=capability.latency_ms,
            confidence=0.90,
            reason=(
                "Selected from registry using "
                f"'{strategy}' strategy "
                f"({capability.provider}:{capability.name})."
            ),
            ranking=ranking,
        )
