"""Statistical adaptation from caller-reported recommendation outcomes."""

from dataclasses import dataclass


@dataclass
class ExperienceRecord:
    """Aggregated local outcome statistics for one model."""

    recommendation_count: int = 0
    success_count: int = 0
    failure_count: int = 0
    average_latency: float = 0.0
    average_cost: float = 0.0

    latency_sample_count: int = 0
    cost_sample_count: int = 0

    @property
    def confidence_adjustment(self) -> float:
        """Return a bounded statistical confidence adjustment."""

        if not self.recommendation_count:
            return 0.0
        return round(((self.success_count / self.recommendation_count) - .5) * .2, 3)


class ExperienceEngine:
    """Store local historical outcomes without machine learning."""

    def __init__(self) -> None:
        self._records: dict[str, ExperienceRecord] = {}

    def get(self, model: str) -> ExperienceRecord:
        """Return accumulated experience for a model."""

        return self._records.setdefault(model, ExperienceRecord())

    def record(
        self,
        model: str,
        success: bool,
        latency: int | None,
        cost: float | None,
    ) -> None:
        """Update statistics using caller-reported outcome data."""

        item = self.get(model)
        item.recommendation_count += 1
        item.success_count += int(success)
        item.failure_count += int(not success)

        if latency is not None:
            item.latency_sample_count += 1
            item.average_latency += (
                latency - item.average_latency
            ) / item.latency_sample_count

        if cost is not None:
            item.cost_sample_count += 1
            item.average_cost += (cost - item.average_cost) / item.cost_sample_count
