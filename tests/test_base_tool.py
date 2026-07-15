from core.tools import BaseTool
from core.tools import FilesystemTool


def test_base_tool():

    tool = FilesystemTool()

    assert isinstance(
        tool,
        BaseTool,
    )

    assert tool.name == "filesystem"