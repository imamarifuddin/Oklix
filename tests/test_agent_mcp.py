from app.agent import OklixAgent


def test_agent_has_mcp_server():

    agent = OklixAgent()

    assert agent.mcp_server is not None