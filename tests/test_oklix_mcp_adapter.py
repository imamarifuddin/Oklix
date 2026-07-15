from oklix_mcp.adapter import MCPAdapter


def test_adapter_exists():
    adapter = MCPAdapter()
    assert adapter is not None


def test_has_service():
    adapter = MCPAdapter()
    assert adapter.service is not None


def test_optimize():
    ...