from core.tool_router import ToolRouter
from core.tool_registry import ToolRegistry

from core.tools.base_tool import BaseTool


class DummyTool(BaseTool):

    name = "dummy"

    def execute(self, **kwargs):
        return "ok"


def test_tool_router():

    registry = ToolRegistry()

    registry.register(
        "dummy",
        DummyTool(),
    )

    router = ToolRouter(
        registry,
    )

    tool = router.route(
        "dummy",
    )

    assert tool.name == "dummy"