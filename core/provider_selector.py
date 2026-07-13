"""
Provider Selector.
"""

from core.registry import ModelRegistry

from domain import TaskProfile
from domain.profile import TaskComplexity
from domain.profile import TaskSize
from domain.task import BudgetLevel


class ProviderSelector:
    """
    Select the most appropriate model.
    """

    def __init__(self) -> None:
        self.registry = ModelRegistry()

    def select(
        self,
        profile: TaskProfile,
    ) -> str:

        if profile.budget == BudgetLevel.LOW:
            return "gemini-2.5-flash"

        if profile.size == TaskSize.LARGE:
            return "claude-sonnet-4"

        if profile.complexity == TaskComplexity.HIGH:
            return "claude-sonnet-4"

        return "gpt-4.1-mini"