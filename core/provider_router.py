"""
Provider Router.

Resolves the execution provider from a recommendation.
"""

from core.providers import ProviderRegistry

from domain import Recommendation


class ProviderRouter:
    """
    Resolve the provider used during execution.
    """

    def __init__(
        self,
        registry: ProviderRegistry | None = None,
    ) -> None:

        self.registry = registry or ProviderRegistry()

    def resolve(
        self,
        recommendation: Recommendation,
    ):
        """
        Resolve execution provider.
        """

        provider_name = (
            recommendation.execution_provider
            or recommendation.provider
        )

        provider = self.registry.get(provider_name)

        if provider is None:
            provider = self.registry.default()

        return provider