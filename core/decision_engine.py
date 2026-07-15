"""
Decision Engine.
"""

from core.analyzer import Analyzer
from core.optimizer import Optimizer

from domain import Recommendation
from domain import TaskProfile, TaskRequest


class DecisionEngine:
    """
    Decision pipeline.

    TaskProfile
        ↓
    Optimizer
        ↓
    Recommendation
    """

    def __init__(self) -> None:
        self.analyzer = Analyzer()
        self.optimizer = Optimizer()

    def decide(
        self,
        request: TaskRequest | TaskProfile,
    ) -> Recommendation:
        """
        Produce a recommendation from a request or an analyzed task profile.
        """

        profile = (
            request
            if isinstance(request, TaskProfile)
            else self.analyzer.analyze(request)
        )
        return self.optimizer.optimize(profile)
