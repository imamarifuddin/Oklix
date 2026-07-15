from core.providers import QwenProvider


def test_provider_instance():
    provider = QwenProvider()
    assert provider is not None


def test_models():
    provider = QwenProvider()
    assert len(provider.models()) > 0


def test_health_returns_bool():
    provider = QwenProvider()
    assert isinstance(provider.health(), bool)