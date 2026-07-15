"""
Oklix Logger.
"""

from domain import Recommendation, TaskProfile


class OklixLogger:
    """
    Pretty logger for demo.
    """

    @staticmethod
    def analyzer(profile: TaskProfile) -> None:

        print("\n" + "=" * 60)
        print("Analyzer")
        print("=" * 60)

        print(f"Task Size       : {profile.size.value}")
        print(f"Complexity      : {profile.complexity.value}")
        print(f"Budget          : {profile.budget.value}")

    @staticmethod
    def decision(recommendation: Recommendation) -> None:

        print("\n" + "=" * 60)
        print("Decision")
        print("=" * 60)

        print(f"Strategy        : {recommendation.strategy}")

        print(
            f"Recommended Model : "
            f"{recommendation.provider}"
            f"/"
            f"{recommendation.recommended_model}"
        )

        print(
            f"Execution Backend : "
            f"{recommendation.execution_provider}"
            f"/"
            f"{recommendation.execution_model}"
        )

        print(
            f"Estimated Cost  : "
            f"${recommendation.estimated_cost:.4f}"
        )

        print(
            f"Latency         : "
            f"{recommendation.estimated_latency_ms} ms"
        )

        print(
            f"Confidence      : "
            f"{recommendation.confidence:.0%}"
        )

        print("\nReason")
        print(recommendation.reason)

    @staticmethod
    def ranking(recommendation: Recommendation) -> None:

        if not recommendation.ranking:
            return

        print("\n" + "=" * 60)
        print("MODEL RANKING")
        print("=" * 60)

        for i, model in enumerate(
            recommendation.ranking,
            start=1,
        ):

            print(
                f"{i}. "
                f"{model.provider}"
                f"/"
                f"{model.model}"
            )

            print(
                f"   Score : {model.score:.2f}"
            )

    @staticmethod
    def planner() -> None:

        print("\n" + "=" * 60)
        print("Planner")
        print("=" * 60)

        print("Execution plan created.")

    @staticmethod
    def executor() -> None:

        print("\n" + "=" * 60)
        print("Execution")
        print("=" * 60)

        print("Executing using Qwen backend...\n")
