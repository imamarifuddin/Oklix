"""Alternative recommendation generation for decision consumers."""

from domain import RankedModel, TradeoffRecommendation


class TradeoffEngine:
    """Select justified alternatives from an existing ranked model list."""

    def build(self, ranking: list[RankedModel]) -> list[TradeoffRecommendation]:
        """Return preference-oriented alternatives without executing them."""

        if not ranking:
            return []
        selections = {
            "Balanced": ranking[0],
            "Cheapest": min(ranking, key=lambda item: item.estimated_cost),
            "Fastest": min(ranking, key=lambda item: item.estimated_latency_ms),
            "Highest Quality": max(ranking, key=lambda item: item.score),
        }
        return [
            TradeoffRecommendation(
                category=category,
                provider=model.provider,
                model=model.model,
                justification=f"{category} option based on ranked cost, latency, and score.",
                score=model.score,
            )
            for category, model in selections.items()
        ]
