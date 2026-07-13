"""
Execution Context.
"""

from pydantic import BaseModel, Field


class ExecutionContext(BaseModel):
    """
    Runtime execution state.
    """

    variables: dict[str, object] = Field(
        default_factory=dict,
    )

    logs: list[str] = Field(
        default_factory=list,
    )

    metadata: dict[str, str] = Field(
        default_factory=dict,
    )

    def log(self, message: str) -> None:
        self.logs.append(message)