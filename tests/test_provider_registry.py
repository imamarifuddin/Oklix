from core.providers import ProviderRegistry


def test_registry_exists():

    registry = ProviderRegistry()

    assert registry.get("qwen")


def test_qwen_registered():

    registry = ProviderRegistry()

    provider = registry.get()

    assert registry.get("qwen")