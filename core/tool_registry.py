"""
Tool Registry.

Stores all tools available through the MCP Server.
"""

from typing import Any


class ToolRegistry:
    """
    Registry of executable tools.
    """

    def __init__(self) -> None:
        self._tools: dict[str, Any] = {}

    def register(
        self,
        name: str,
        tool: Any,
    ) -> None:
        """
        Register a tool.
        """
        self._tools[name] = tool

    def has(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a tool exists.
        """
        return name in self._tools

    def get(
        self,
        name: str,
    ) -> Any:
        """
        Retrieve a registered tool.
        """

        if name not in self._tools:
            raise ValueError(
                f"Unknown tool: {name}"
            )

        return self._tools[name]

    def list(self) -> list[str]:
        """
        Return all registered tool names.
        """

        return sorted(self._tools.keys())