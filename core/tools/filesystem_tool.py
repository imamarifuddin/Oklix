"""
Filesystem Tool.

Provides basic filesystem operations for the MCP server.
"""

from pathlib import Path

from .base_tool import BaseTool


class FilesystemTool(BaseTool):
    """
    Filesystem tool.
    """

    name = "filesystem"

    description = "Read, write and delete files."

    def exists(
        self,
        path: str,
    ) -> bool:
        return Path(path).exists()

    def read(
        self,
        path: str,
    ) -> str:
        return Path(path).read_text(
            encoding="utf-8",
        )

    def write(
        self,
        path: str,
        content: str,
    ) -> None:

        target = Path(path)

        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        target.write_text(
            content,
            encoding="utf-8",
        )

    def delete(
        self,
        path: str,
    ) -> None:

        target = Path(path)

        if target.exists():
            target.unlink()

    def execute(
        self,
        **kwargs,
    ):
        """
        Generic MCP execution entrypoint.
        """

        action = kwargs["action"]

        if action == "exists":
            return self.exists(kwargs["path"])

        if action == "read":
            return self.read(kwargs["path"])

        if action == "write":
            self.write(
                kwargs["path"],
                kwargs["content"],
            )
            return True

        if action == "delete":
            self.delete(kwargs["path"])
            return True

        raise ValueError(
            f"Unknown filesystem action: {action}"
        )