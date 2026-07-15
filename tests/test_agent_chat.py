from app.agent import OklixAgent


def test_agent_chat_exists():

    agent = OklixAgent()

    assert hasattr(agent, "chat")