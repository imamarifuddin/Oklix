"""
Provider Selector.
"""

from domain import TaskProfile
from domain.profile import TaskComplexity, TaskSize
from domain.task import BudgetLevel


class ProviderSelector:
    """
    Select the best model for a task.
    """

    def select(
        self,
        profile: TaskProfile,
    ) -> str:
        """
        Return the recommended model name.
        """

        if profile.budget == BudgetLevel.LOW:
            return "gemini-2.5-flash"

        if profile.size == TaskSize.LARGE:
            return "claude-sonnet-4"

        if profile.complexity == TaskComplexity.HIGH:
            return "claude-sonnet-4"

        return "gpt-4.1-mini"