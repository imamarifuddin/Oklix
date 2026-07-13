"""
Cost Estimation Engine.
"""

from domain import TaskProfile


class CostEstimator:
    """Estimate execution cost."""

    @staticmethod
    def estimate(
        profile: TaskProfile,
        cost_per_100k_tokens: float,
    ) -> float:
        """
        Estimate total execution cost.

        Formula:

        total_tokens / 100000 * model_price
        """

        return round(
            (
                profile.total_tokens
                / 100000
            )
            * cost_per_100k_tokens,
            4,
        )