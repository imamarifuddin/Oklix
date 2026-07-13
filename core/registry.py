"""
Model Registry.
"""

from pathlib import Path

import yaml

from domain.model_capability import ModelCapability


class ModelRegistry:
    """
    Load AI model configuration from YAML.
    """

    def __init__(self) -> None:
        registry_path = (
            Path(__file__).parent.parent
            / "registry"
            / "models.yaml"
        )

        with registry_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = yaml.safe_load(file)

        self._models: dict[str, ModelCapability] = {}

        for name, config in data["models"].items():
            self._models[name] = ModelCapability(
                name=name,
                provider=config["provider"],
                quality=config["quality"],
                speed=config["speed"],
                latency_ms=config["latency_ms"],
                cost_per_100k_tokens=config["cost_per_100k_tokens"],
                context_window=config["context_window"],
                max_output_tokens=config["max_output_tokens"],
                supports=config.get("supports", {}),
                strengths=config.get("strengths", []),
                weaknesses=config.get("weaknesses", []),
            )

    def get(
        self,
        name: str,
    ) -> ModelCapability:
        """
        Return one model.
        """

        if name not in self._models:
            raise KeyError(
                f"Unknown model: {name}"
            )

        return self._models[name]

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Whether model exists.
        """

        return name in self._models

    def all(
        self,
    ) -> dict[str, ModelCapability]:
        """
        Return every model.
        """

        return self._models

    def names(
        self,
    ) -> list[str]:
        """
        Return every model name.
        """

        return list(self._models.keys())