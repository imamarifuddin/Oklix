from core.experience_engine import ExperienceEngine
from core.provider_health import ProviderHealthRegistry
from core.provider_knowledge import ProviderKnowledgeRegistry
from core.recommendation_history import HistoryItem, RecommendationHistory


def test_provider_knowledge_is_local_structured_metadata():
    item = ProviderKnowledgeRegistry().get_model("gpt-4.1-mini")
    assert item["provider"] == "openai" and "reliability_score" in item


def test_health_and_experience_adapt_from_feedback():
    health = ProviderHealthRegistry(); experience = ExperienceEngine()
    health.record("openai", False, 3000); experience.record("gpt-4.1-mini", False, 3000, .1)
    assert health.get("openai").status in {"degraded", "offline"}
    assert experience.get("gpt-4.1-mini").confidence_adjustment < 0


def test_history_exposes_dashboard_metrics():
    history = RecommendationHistory()
    history.add(HistoryItem("one", "openai", "gpt", .9, .1, 100, True))
    assert history.metrics()["fastest_models"] == ["gpt"]
