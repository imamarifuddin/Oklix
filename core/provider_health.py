"""In-memory provider health tracking for adaptive decisions."""

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class ProviderHealth:
    """Health state derived from caller-reported outcomes."""

    availability: str = "available"
    status: str = "healthy"
    average_latency_ms: float = 0.0
    average_failures: float = 0.0
    last_updated: str = ""

    observation_count: int = 0
    latency_sample_count: int = 0

    @property
    def score(self) -> float:
        """Return a normalized health contribution for scoring."""

        return {"healthy": 1.0, "degraded": 0.65, "offline": 0.1}.get(self.status, 0.5)


class ProviderHealthRegistry:
    """Store local health observations by provider."""

    def __init__(self) -> None:
        self._health: dict[str, ProviderHealth] = {}

    def get(self, provider: str) -> ProviderHealth:
        """Return current health or the healthy default."""

        return self._health.setdefault(provider, ProviderHealth())

    def record(self, provider: str, success: bool, latency_ms: int | None = None) -> None:
        """Update local health from a caller-reported outcome."""

        health = self.get(provider)
        health.observation_count += 1
        health.average_failures += (
            (0 if success else 1) - health.average_failures
        ) / health.observation_count

        if latency_ms is not None:
            health.latency_sample_count += 1
            health.average_latency_ms += (
                latency_ms - health.average_latency_ms
            ) / health.latency_sample_count

        if health.average_failures >= 0.75:
            health.status = "offline"
        elif health.average_failures >= 0.25:
            health.status = "degraded"
        else:
            health.status = "healthy"

        health.last_updated = datetime.now(timezone.utc).isoformat()
