"""
Result returned by a Tool execution.
"""

from pydantic import BaseModel


class ToolResult(BaseModel):
    """
    Result produced by a tool.
    """

    success: bool

    output: str | None = None

    error: str | None = None

    metadata: dict = {}