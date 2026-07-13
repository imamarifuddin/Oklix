"""
Capability Engine.
"""

from core.registry import ModelRegistry


class CapabilityEngine:
    """
    Access model capabilities from the registry.
    """

    def __init__(self) -> None:
        self.registry = ModelRegistry()

    def supports(
        self,
        model: str,
        capability: str,
    ) -> bool:

        info = self.registry.get(model)

        return info.supports.get(
            capability,
            False,
        )

    def has_strength(
        self,
        model: str,
        task: str,
    ) -> bool:

        info = self.registry.get(model)

        return task.lower() in info.strengths

    def context_window(
        self,
        model: str,
    ) -> int:

        return self.registry.get(
            model
        ).context_window

    def max_output_tokens(
        self,
        model: str,
    ) -> int:

        return self.registry.get(
            model
        ).max_output_tokens