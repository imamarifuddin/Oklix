"""
Scoring Engine.

Calculate a score for every available model.
"""

from dataclasses import dataclass

from core.cost_estimator import CostEstimator
from core.decision_profiles import DecisionProfileRegistry
from core.registry import ModelRegistry

from domain import TaskProfile
from domain.task import BudgetLevel


@dataclass(slots=True)
class ModelScore:
    """Score information for a single model."""

    name: str
    score: float
    cost_score: float
    quality_score: float
    speed_score: float
    provider: str


class ScoringEngine:
    """Calculate weighted scores for every registered model."""

    def __init__(self) -> None:
        self.registry = ModelRegistry()
        self.profile_registry = DecisionProfileRegistry()

    def score_models(
        self,
        profile: TaskProfile,
        decision_profile: str = "balanced",
    ) -> list[ModelScore]:
        """
        Score all available models using the selected decision profile.
        """

        weights = self.profile_registry.get(
            decision_profile,
        )

        results: list[ModelScore] = []

        for capability in self.registry.all().values():

            estimated_cost = CostEstimator.estimate(
                profile,
                capability.cost_per_100k_tokens,
            )

            cost_score = self._cost_score(
                profile,
                estimated_cost,
            )

            quality_score = self._quality_score(
                capability.quality,
            )

            speed_score = self._speed_score(
                capability.speed,
            )

            final_score = (
                cost_score * weights["cost"]
                + quality_score * weights["quality"]
                + speed_score * weights["speed"]
            )

            results.append(
                ModelScore(
                    name=capability.name,
                    score=round(final_score, 2),
                    cost_score=round(cost_score, 2),
                    quality_score=round(quality_score, 2),
                    speed_score=round(speed_score, 2),
                    provider=capability.provider,
                )
            )

        results.sort(
            key=lambda item: item.score,
            reverse=True,
        )

        return results

    @staticmethod
    def _cost_score(
        profile: TaskProfile,
        estimated_cost: float,
    ) -> float:
        """
        Convert estimated execution cost into score.
        """

        if profile.budget == BudgetLevel.LOW:
            multiplier = 800
        elif profile.budget == BudgetLevel.MEDIUM:
            multiplier = 500
        else:
            multiplier = 300

        return max(
            0.0,
            100 - (estimated_cost * multiplier),
        )

    @staticmethod
    def _quality_score(
        quality: str,
    ) -> float:
        """
        Convert quality level into score.
        """

        mapping = {
            "high": 100.0,
            "medium": 80.0,
            "low": 60.0,
        }

        return mapping.get(
            quality,
            50.0,
        )

    @staticmethod
    def _speed_score(
        speed: str,
    ) -> float:
        """
        Convert speed level into score.
        """

        mapping = {
            "fast": 100.0,
            "medium": 80.0,
            "slow": 60.0,
        }

        return mapping.get(
            speed,
            50.0,
        )