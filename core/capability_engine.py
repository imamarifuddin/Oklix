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

    def normalized(
        self,
        model: str,
    ) -> dict[str, float]:
        """Return normalized v2 capabilities for a registered model."""

        capability = self.registry.get(model)
        defaults = {
            "reasoning": 1.0 if capability.supports.get("reasoning") else 0.4,
            "coding": 1.0 if "coding" in capability.strengths else 0.5,
            "math": 0.8 if capability.supports.get("reasoning") else 0.4,
            "long_context": min(1.0, capability.context_window / 1_000_000),
            "vision": 1.0 if capability.supports.get("vision") else 0.0,
            "tool_use": 1.0 if capability.supports.get("function_calling") else 0.0,
            "instruction_following": 0.9 if capability.quality == "high" else 0.7,
            "speed": {"fast": 1.0, "medium": 0.7, "slow": 0.4}.get(capability.speed, 0.5),
            "reliability": {"high": 0.95, "medium": 0.75, "low": 0.55}.get(capability.quality, 0.6),
        }

        return {**defaults, **capability.capabilities}
