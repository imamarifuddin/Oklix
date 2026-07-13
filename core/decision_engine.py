"""
Decision Engine.
"""

from core.analyzer import Analyzer
from core.optimizer import Optimizer

from domain import Recommendation
from domain import TaskRequest


class DecisionEngine:
    """
    End-to-end decision pipeline.

    TaskRequest
        ↓
    Analyzer
        ↓
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
        request: TaskRequest,
    ) -> Recommendation:
        """
        Execute the complete decision pipeline.
        """

        profile = self.analyzer.analyze(request)

        return self.optimizer.optimize(profile)