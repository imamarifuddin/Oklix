"""
Provider Registry.
"""

from .qwen_provider import QwenProvider
from .base_provider import BaseProvider


class ProviderRegistry:
    """
    Registry of all available providers.
    """

    def __init__(self) -> None:

        self.providers = {
            "qwen": QwenProvider(),
        }

    def get(
        self,
        name: str = "qwen",
    ) -> BaseProvider:

        return self.providers[name]

    def default(self):

        return self.providers["qwen"]

    def names(self) -> list[str]:

        return list(self.providers.keys())
