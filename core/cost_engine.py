"""
Cost Engine.
"""

from domain import (
    CostEstimate,
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

    def estimate_detailed(
        self,
        profile: TaskProfile,
        capability: ModelCapability,
        cached_tokens: int = 0,
    ) -> CostEstimate:
        """Return an explainable v2 estimate using token category pricing."""

        input_tokens = max(0, profile.total_tokens - profile.total_tokens // 5)
        output_tokens = profile.total_tokens - input_tokens
        cached_tokens = min(max(0, cached_tokens), input_tokens)
        input_rate = capability.input_cost_per_1m_tokens or capability.cost_per_100k_tokens * 10
        output_rate = capability.output_cost_per_1m_tokens or input_rate
        cached_rate = capability.cached_cost_per_1m_tokens or input_rate * 0.25
        input_cost = (input_tokens - cached_tokens) * input_rate / 1_000_000
        output_cost = output_tokens * output_rate / 1_000_000
        cached_cost = cached_tokens * cached_rate / 1_000_000
        total = round(input_cost + output_cost + cached_cost, 6)

        return CostEstimate(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cached_tokens=cached_tokens,
            input_cost=round(input_cost, 6),
            output_cost=round(output_cost, 6),
            cached_cost=round(cached_cost, 6),
            total_cost=total,
            calculation="input + output + cached token pricing",
        )
