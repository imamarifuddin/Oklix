"""
Base Provider Interface.
"""

from abc import ABC
from abc import abstractmethod


class BaseProvider(ABC):
    """
    Base interface for every AI provider.
    """

    @abstractmethod
    def chat(
        self,
        prompt: str,
        system_prompt: str = "",
    ) -> str:
        """
        Execute a chat completion.
        """
        raise NotImplementedError

    @abstractmethod
    def health(self) -> bool:
        """
        Check provider availability.
        """
        raise NotImplementedError

    @abstractmethod
    def models(self) -> list[str]:
        """
        Return supported models.
        """
        raise NotImplementedError