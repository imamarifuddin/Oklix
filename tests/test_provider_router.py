from core.provider_router import ProviderRouter
from core.providers import ProviderRegistry

from domain import Recommendation


def test_provider_router_returns_provider():

    registry = ProviderRegistry()

    router = ProviderRouter(registry)

    recommendation = Recommendation(
        strategy="direct_execution",
        provider="qwen",
        recommended_model="qwen-plus",
        execution_provider="qwen",
        execution_model="qwen-plus",
        estimated_cost=0.01,
        estimated_latency_ms=500,
        confidence=0.95,
    )

    provider = router.resolve(recommendation)

    assert provider is not None