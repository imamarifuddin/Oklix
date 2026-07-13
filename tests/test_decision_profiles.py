"""
Decision profiles.

Each profile defines the weighting used by the Scoring Engine.
"""


class DecisionProfiles:
    """Repository of decision profiles."""

    def __init__(self) -> None:
        self._profiles = {
            "balanced": {
                "cost": 0.40,
                "quality": 0.35,
                "speed": 0.25,
            },
            "quality_first": {
                "cost": 0.15,
                "quality": 0.65,
                "speed": 0.20,
            },
            "speed_first": {
                "cost": 0.20,
                "quality": 0.20,
                "speed": 0.60,
            },
            "cheapest": {
                "cost": 0.80,
                "quality": 0.10,
                "speed": 0.10,
            },
        }

    def get(self, name: str) -> dict:
        """Return a decision profile."""

        return self._profiles[name]

    def exists(self, name: str) -> bool:
        """Check whether profile exists."""

        return name in self._profiles

    def all(self) -> dict:
        """Return all profiles."""

        return self._profiles