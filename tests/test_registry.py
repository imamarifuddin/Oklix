from core.registry import ModelRegistry


def test_registry_load():
    registry = ModelRegistry()

    assert len(registry.names()) > 0


def test_registry_exists():
    registry = ModelRegistry()

    assert registry.exists("gpt-4.1-mini")


def test_registry_get():
    registry = ModelRegistry()

    model = registry.get("claude-sonnet-4")

    assert model.provider == "anthropic"


def test_registry_cost():
    registry = ModelRegistry()

    model = registry.get("gpt-4.1-mini")

    assert model.cost_per_100k_tokens == 0.35


def test_registry_quality():
    registry = ModelRegistry()

    model = registry.get("claude-sonnet-4")

    assert model.quality == "high"