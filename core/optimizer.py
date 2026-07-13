"""
Optimizer.
"""

from core.registry import ModelRegistry

from domain import Recommendation
from domain import TaskProfile
from domain.profile import TaskSize
from domain.task import BudgetLevel


class Optimizer:
    """
    Simple optimization engine.
    """

    def __init__(self) -> None:
        self.registry = ModelRegistry()

    def optimize(
        self,
        profile: TaskProfile,
    ) -> Recommendation:

        strategy = self._select_strategy(profile)

        model_name = self._select_model(profile)

        capability = self.registry.get(model_name)

        estimated_cost = round(
            (
                profile.total_tokens / 100000
            )
            * capability.cost_per_100k_tokens,
            4,
        )

        return Recommendation(
            strategy=strategy,
            recommended_model=capability.name,
            provider=capability.provider,
            estimated_cost=estimated_cost,
            estimated_latency_ms=5000
            if profile.size == TaskSize.LARGE
            else capability.latency_ms,
            confidence=0.90,
            reason=(
                f"Selected from registry using "
                f"'{strategy}' strategy "
                f"({capability.provider}:{capability.name})."
            ),
            ranking=[],
        )

    def _select_strategy(
        self,
        profile: TaskProfile,
    ) -> str:

        if profile.size == TaskSize.LARGE:
            return "parallel_chunk_merge"

        return "direct_execution"

    def _select_model(
        self,
        profile: TaskProfile,
    ) -> str:

        if profile.budget == BudgetLevel.LOW:
            return "gemini-2.5-flash"

        if profile.size == TaskSize.LARGE:
            return "claude-sonnet-4"

        return "gpt-4.1-mini"