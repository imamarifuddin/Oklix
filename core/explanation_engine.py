"""Machine-readable explanation generation for recommendations."""

from core.capability_engine import CapabilityEngine
from core.scoring import ModelScore
from domain import RecommendationExplanation, RankedModel


class RecommendationExplanationEngine:
    """Explain why a ranked model was selected."""

    def __init__(self) -> None:
        self.capability_engine = CapabilityEngine()

    def explain(self, model: RankedModel, score: ModelScore) -> RecommendationExplanation:
        """Build structured reasons from the selected score and capabilities."""

        capabilities = self.capability_engine.normalized(model.model)
        reasons = ["Highest explainable weighted score", "Meets selected cost and quality profile"]
        if capabilities["reasoning"] >= 0.8:
            reasons.append("Strong normalized reasoning capability")
        if capabilities["long_context"] >= 0.5:
            reasons.append("Supports long-context workloads")
        return RecommendationExplanation(
            summary=f"{model.provider}/{model.model} is the balanced recommendation.",
            reasons=reasons,
            confidence=min(0.99, model.score / 100),
            factors={**score.factors, **{f"capability_{key}": value for key, value in capabilities.items()}},
        )
