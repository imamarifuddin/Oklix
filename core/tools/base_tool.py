"""
Base Tool.

All MCP tools inherit from this class.
"""

from abc import ABC
from abc import abstractmethod


class BaseTool(ABC):
    """
    Base interface for every executable tool.
    """

    name: str = ""

    description: str = ""

    @abstractmethod
    def execute(
        self,
        **kwargs,
    ):
        """
        Execute the tool.
        """
        raise NotImplementedError