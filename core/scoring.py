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
    weights: dict[str, float]
    factors: dict[str, float]
    penalties: dict[str, float]
    bonuses: dict[str, float]


class ScoringEngine:
    """Calculate weighted scores for every registered model."""

    def __init__(self, health_registry=None, experience_engine=None) -> None:
        self.registry = ModelRegistry()
        self.profile_registry = DecisionProfileRegistry()
        self.health_registry = health_registry
        self.experience_engine = experience_engine

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
            penalties = {
                "context_shortfall": 10.0
                if capability.context_window < profile.total_tokens
                else 0.0,
            }
            bonuses = {
                "reasoning": 5.0
                if capability.supports.get("reasoning")
                else 0.0,
            }
            if self.health_registry:
                health = self.health_registry.get(capability.provider)
                bonuses["provider_health"] = round(health.score * 5, 2)
            if self.experience_engine:
                experience = self.experience_engine.get(capability.name)
                bonuses["experience"] = experience.confidence_adjustment * 100
            final_score = final_score - sum(penalties.values()) + sum(bonuses.values())

            results.append(
                ModelScore(
                    name=capability.name,
                    score=round(final_score, 2),
                    cost_score=round(cost_score, 2),
                    quality_score=round(quality_score, 2),
                    speed_score=round(speed_score, 2),
                    provider=capability.provider,
                    weights=dict(weights),
                    factors={
                        "cost": round(cost_score, 2),
                        "quality": round(quality_score, 2),
                        "speed": round(speed_score, 2),
                    },
                    penalties=penalties,
                    bonuses=bonuses,
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
