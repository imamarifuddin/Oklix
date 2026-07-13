"""
Decision Profile Registry
"""

from pathlib import Path

import yaml


class DecisionProfileRegistry:

    def __init__(self):

        path = (
            Path(__file__).parent.parent
            / "registry"
            / "decision_profiles.yaml"
        )

        with open(path, encoding="utf-8") as f:
            self._profiles = yaml.safe_load(f)["profiles"]

    def get(self, name="balanced"):

        return self._profiles[name]

    def exists(self, name):

        return name in self._profiles

    def all(self):

        return self._profiles