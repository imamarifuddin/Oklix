"""
Tool Call domain model.
"""

from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    """
    Represents a request to execute a tool.
    """

    name: str = Field(
        ...,
        description="Tool name",
    )

    arguments: dict = Field(
        default_factory=dict,
        description="Tool arguments",
    )