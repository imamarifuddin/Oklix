"""
Cost Engine.
"""

from domain import (
    ModelCapability,
    TaskProfile,
)


class CostEngine:
    """
    Estimate execution cost.
    """

    def estimate(
        self,
        profile: TaskProfile,
        capability: ModelCapability,
    ) -> float:

        return round(
            (
                profile.total_tokens
                / 100000
            )
            * capability.cost_per_100k_tokens,
            4,
        )