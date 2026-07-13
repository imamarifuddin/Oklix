"""
Decision Engine.

Main orchestration pipeline.
"""

from core.analyzer import Analyzer
from core.optimizer import Optimizer
from core.ranking import RankingEngine
from core.scoring import ScoringEngine

from domain import Recommendation
from domain import TaskRequest


class DecisionEngine:
    """
    End-to-end decision pipeline.
    """

    def __init__(self) -> None:
        self.analyzer = Analyzer()
        self.scoring = ScoringEngine()
        self.ranking = RankingEngine()
        self.optimizer = Optimizer()

    def decide(
        self,
        request: TaskRequest,
    ) -> Recommendation:
        """
        Execute complete decision pipeline.
        """

        profile = self.analyzer.analyze(request)

        strategy = self.optimizer._select_strategy(profile)

        if strategy == "parallel_chunk_merge":
            decision_profile = "quality"
        elif request.budget.value == "low":
            decision_profile = "cheap"
        else:
            decision_profile = "balanced"

        scores = self.scoring.score_models(
            profile,
            decision_profile,
        )

        ranking = self.ranking.build(
            profile,
            scores,
        )

        recommendation = self.optimizer.optimize(
            profile,
        )

        recommendation.ranking = ranking

        return recommendation