from core.tool_executor import ToolExecutor
from core.tool_registry import ToolRegistry

from core.tools.base_tool import BaseTool

from domain.tool_call import ToolCall


class DummyTool(BaseTool):

    name = "dummy"

    def execute(self, **kwargs):
        return "ok"


def test_tool_executor():

    registry = ToolRegistry()

    registry.register(
        "dummy",
        DummyTool(),
    )

    executor = ToolExecutor(
        registry,
    )

    result = executor.execute(
        ToolCall(
            name="dummy",
            arguments={},
        )
    )

    assert result == "ok"