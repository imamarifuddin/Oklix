"""Recommendation history and dashboard metrics for local decision state."""

from dataclasses import dataclass


@dataclass
class HistoryItem:
    """One recommendation and optional caller outcome."""

    recommendation_id: str
    provider: str
    model: str
    confidence: float
    cost: float
    latency: int
    success: bool | None = None


class RecommendationHistory:
    """Store recommendation history for adaptive metrics."""

    def __init__(self) -> None:
        self.items: dict[str, HistoryItem] = {}

    def add(self, item: HistoryItem) -> None:
        """Add or replace a history item by its stable identifier."""

        self.items[item.recommendation_id] = item

    def get(self, recommendation_id: str) -> HistoryItem | None:
        """Return a history item when it exists."""

        return self.items.get(recommendation_id)

    def metrics(self) -> dict:
        """Return metadata-only dashboard metrics."""

        values = list(self.items.values())
        if not values:
            return {
                "top_providers": [],
                "most_reliable_models": [],
                "fastest_models": [],
                "cheapest_models": [],
                "highest_confidence": [],
            }

        top_provider = max(
            {item.provider for item in values},
            key=lambda provider: sum(item.provider == provider for item in values),
        )
        successful_models = [item for item in values if item.success is True]
        reliable_models = successful_models or values

        return {
            "top_providers": [top_provider],
            "most_reliable_models": [
                max(reliable_models, key=lambda item: item.confidence).model
            ],
            "fastest_models": [min(values, key=lambda item: item.latency).model],
            "cheapest_models": [min(values, key=lambda item: item.cost).model],
            "highest_confidence": [max(values, key=lambda item: item.confidence).model],
        }
