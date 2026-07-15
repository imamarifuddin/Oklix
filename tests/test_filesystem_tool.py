from core.tools import FilesystemTool


def test_filesystem_tool(tmp_path):

    tool = FilesystemTool()

    file = tmp_path / "hello.txt"

    tool.write(
        str(file),
        "Hello Oklix",
    )

    assert tool.exists(
        str(file),
    )

    assert tool.read(
        str(file),
    ) == "Hello Oklix"

    tool.delete(
        str(file),
    )

    assert not tool.exists(
        str(file),
    )