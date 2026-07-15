"""
Tool Executor.

Executes tool calls using the ToolRegistry.
"""

from core.tool_registry import ToolRegistry
from domain.tool_call import ToolCall


class ToolExecutor:
    """
    Execute registered tools.
    """

    def __init__(
        self,
        registry: ToolRegistry | None = None,
    ) -> None:

        self.registry = registry or ToolRegistry()

    def execute(
        self,
        call: ToolCall,
    ):

        tool = self.registry.get(call.name)

        return tool.execute(
            **call.arguments,
        )