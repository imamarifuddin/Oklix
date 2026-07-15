from core.tool_registry import ToolRegistry


class DummyTool:
    pass


def test_tool_registry():

    registry = ToolRegistry()

    registry.register(
        "dummy",
        DummyTool(),
    )

    assert registry.has("dummy")

    assert registry.get("dummy") is not None

    assert registry.list() == [
        "dummy",
    ]