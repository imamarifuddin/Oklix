from core.mcp_server import MCPServer


class DummyTool:
    pass


def test_mcp_server():

    server = MCPServer()

    server.register(
        "dummy",
        DummyTool(),
    )

    assert server.has("dummy")

    assert server.get("dummy") is not None

    assert server.list_tools() == [
        "dummy",
    ]