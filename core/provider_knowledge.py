"""Local metadata knowledge base for provider and model decisions."""

from core.registry import ModelRegistry


class ProviderKnowledgeRegistry:
    """Expose local-only provider/model metadata for decision engines."""

    def __init__(self) -> None:
        self.models = ModelRegistry()

    def get_model(self, model: str) -> dict:
        """Return structured metadata for a registered model."""

        item = self.models.get(model)
        return {
            "provider": item.provider, "model": item.name,
            "pricing": item.cost_per_100k_tokens, "context_window": item.context_window,
            "vision": item.supports.get("vision", False),
            "reasoning": item.supports.get("reasoning", False),
            "coding": "coding" in item.strengths,
            "json_mode": item.supports.get("json_mode", False),
            "streaming": item.supports.get("streaming", False),
            "tool_calling": item.supports.get("function_calling", False),
            "reliability_score": {"high": .95, "medium": .75, "low": .55}.get(item.quality, .6),
            "default_latency_ms": item.latency_ms,
            "release_date": None, "deprecated": False,
        }

    def list_models(self) -> list[dict]:
        """Return all local model metadata records."""

        return [self.get_model(name) for name in self.models.names()]
