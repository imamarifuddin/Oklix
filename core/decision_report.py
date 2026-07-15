"""
Decision Report.

Presentation layer for Decision Intelligence.

This module does NOT perform any decision making.

It only formats existing objects into a human-readable report.
"""

from domain import (
    ExecutionContext,
    Recommendation,
    TaskProfile,
    TaskRequest,
)


class DecisionReport:
    """
    Builds a readable Decision Intelligence report.
    """

    @staticmethod
    def build(
        request: TaskRequest,
        profile: TaskProfile,
        recommendation: Recommendation,
        context: ExecutionContext | None = None,
    ) -> str:

        lines: list[str] = []

        lines.append("")
        lines.append("=" * 60)
        lines.append("OKLIX DECISION REPORT")
        lines.append("=" * 60)
        lines.append("")

        # -------------------------------------------------
        # Request
        # -------------------------------------------------

        lines.append("Request")
        lines.append("-" * 60)
        lines.append(request.task)
        lines.append("")

        # -------------------------------------------------
        # Analysis
        # -------------------------------------------------

        lines.append("Analysis")
        lines.append("-" * 60)
        lines.append(f"Task Size          : {profile.size.value}")
        lines.append(f"Complexity         : {profile.complexity.value}")
        lines.append(f"Budget             : {profile.budget.value}")
        lines.append("")

        # -------------------------------------------------
        # Decision
        # -------------------------------------------------

        lines.append("Decision")
        lines.append("-" * 60)
        lines.append(f"Strategy           : {recommendation.strategy}")
        lines.append(f"Provider           : {recommendation.provider}")
        lines.append(f"Recommended Model  : {recommendation.recommended_model}")
        lines.append("")

        # -------------------------------------------------
        # Execution
        # -------------------------------------------------

        lines.append("Execution")
        lines.append("-" * 60)

        if context is not None:

            provider = (
                context.execution_provider
                or recommendation.execution_provider
            )

            model = (
                context.execution_model
                or recommendation.execution_model
            )

        else:

            provider = recommendation.execution_provider
            model = recommendation.execution_model

        lines.append(f"Execution Provider : {provider}")
        lines.append(f"Execution Model    : {model}")
        lines.append("")

        # -------------------------------------------------
        # Performance
        # -------------------------------------------------

        lines.append("Performance")
        lines.append("-" * 60)
        lines.append(
            f"Estimated Cost     : ${recommendation.estimated_cost:.4f}"
        )
        lines.append(
            f"Latency            : {recommendation.estimated_latency_ms} ms"
        )
        lines.append(
            f"Confidence         : {recommendation.confidence:.0%}"
        )
        lines.append("")

        # -------------------------------------------------
        # Reason
        # -------------------------------------------------

        lines.append("Reason")
        lines.append("-" * 60)
        lines.append(recommendation.reason or "-")
        lines.append("")

        # -------------------------------------------------
        # Model Ranking
        # -------------------------------------------------

        lines.append("Model Ranking")
        lines.append("-" * 60)

        if recommendation.ranking:

            for index, model in enumerate(
                recommendation.ranking,
                start=1,
            ):
                lines.append(
                    f"{index}. "
                    f"{model.provider}/{model.model} "
                    f"(score={model.score:.2f})"
                )

        else:

            lines.append("No ranking available.")

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)