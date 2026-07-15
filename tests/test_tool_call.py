from domain import ToolCall


def test_tool_call():

    call = ToolCall(
        name="filesystem",
        arguments={
            "path": "README.md",
        },
    )

    assert call.name == "filesystem"

    assert call.arguments["path"] == "README.md"