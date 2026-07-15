from app.agent import OklixAgent


def test_agent_exists():

    agent = OklixAgent()

    assert agent is not None


def test_provider_exists():

    agent = OklixAgent()

    assert agent.provider is not None