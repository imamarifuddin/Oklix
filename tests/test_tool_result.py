from domain.tool_result import ToolResult


def test_tool_result():

    result = ToolResult(
        success=True,
        output="hello",
    )

    assert result.success is True
    assert result.output == "hello"
    assert result.error is None