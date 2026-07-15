from app.agent import OklixAgent


def test_agent_has_multi_agent():

    agent = OklixAgent()

    assert agent.multi_agent is not None

    assert agent.multi_agent.get(
        "executor"
    ) is not None