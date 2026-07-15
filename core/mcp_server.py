"""
MCP Server.

Gateway for all tools exposed through the Model Context Protocol.
"""

from typing import Any

from core.tool_registry import ToolRegistry


class MCPServer:
    """
    Simple MCP server implementation.
    """

    def __init__(self) -> None:
        self.registry = ToolRegistry()

    def register(
        self,
        name: str,
        tool: Any,
    ) -> None:
        """
        Register a tool.
        """
        self.registry.register(
            name,
            tool,
        )

    def has(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a tool exists.
        """
        return self.registry.has(
            name,
        )

    def get(
        self,
        name: str,
    ) -> Any:
        """
        Retrieve a registered tool.
        """
        return self.registry.get(
            name,
        )

    def list_tools(
        self,
    ) -> list[str]:
        """
        Return all available tools.
        """
        return self.registry.list()