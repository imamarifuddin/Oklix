"""
Ranking Engine.

Convert scored models into ranked recommendations.
"""

from core.cost_estimator import CostEstimator

from core.scoring import ModelScore

from core.registry import ModelRegistry

from domain import RankedModel
from domain import TaskProfile


class RankingEngine:
    """
    Build ranked model recommendations.
    """

    def __init__(self) -> None:
        self.registry = ModelRegistry()

    def build(
        self,
        profile: TaskProfile,
        scores: list[ModelScore],
    ) -> list[RankedModel]:
        """
        Convert scored models into ranked recommendations.
        """

        ranking: list[RankedModel] = []

        for rank, score in enumerate(
            scores,
            start=1,
        ):

            capability = self.registry.get(
                score.name,
            )

            ranking.append(
                RankedModel(
                    rank=rank,
                    model=capability.name,
                    provider=capability.provider,
                    score=score.score,
                    estimated_cost=CostEstimator.estimate(
                        profile,
                        capability.cost_per_100k_tokens,
                    ),
                    estimated_latency_ms=capability.latency_ms,
                    strength=capability.quality,
                )
            )

        return ranking

    @staticmethod
    def best(
        ranking: list[RankedModel],
    ) -> RankedModel:
        """
        Return the highest-ranked model.
        """

        if not ranking:
            raise ValueError(
                "Ranking is empty."
            )

        return ranking[0]