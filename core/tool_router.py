"""
Tool Router.

Chooses the correct tool for a task.
"""

from core.tool_registry import ToolRegistry


class ToolRouter:

    def __init__(
        self,
        registry: ToolRegistry,
    ):
        self.registry = registry

    def route(
        self,
        name: str,
    ):

        return self.registry.get(name)