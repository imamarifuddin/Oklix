"""Latency estimation for recommendation-only decisions."""

from domain import LatencyEstimate, ModelCapability, TaskProfile


class LatencyEngine:
    """Estimate model latency with confidence intervals."""

    def estimate(self, profile: TaskProfile, capability: ModelCapability) -> LatencyEstimate:
        """Estimate latency from model baseline, task size, and output volume."""

        size_factor = 1 + min(1.0, profile.total_tokens / capability.context_window)
        expected = round(capability.latency_ms * size_factor)
        spread = max(100, round(expected * 0.2))
        return LatencyEstimate(
            expected_ms=expected,
            lower_bound_ms=max(1, expected - spread),
            upper_bound_ms=expected + spread,
            confidence=0.8,
            factors={"baseline_ms": capability.latency_ms, "size_factor": round(size_factor, 3)},
        )
