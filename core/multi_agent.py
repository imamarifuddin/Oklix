"""
Multi Agent Orchestrator.
"""

from domain import ExecutionContext


class MultiAgent:
    """
    Simple multi-agent registry and orchestrator.
    """

    def __init__(self) -> None:
        self._agents: dict[str, object] = {}

    def register(
        self,
        name: str,
        agent: object,
    ) -> None:
        """
        Register an agent.
        """
        self._agents[name] = agent

    def get(
        self,
        name: str,
    ) -> object:
        """
        Retrieve an agent.
        """
        return self._agents[name]

    def execute(
        self,
        name: str,
        context: ExecutionContext,
    ):
        """
        Execute an agent.

        Supports both the legacy execute(context)
        interface and the new execute_context(context)
        interface.
        """

        agent = self.get(name)

        if hasattr(agent, "execute_context"):
            return agent.execute_context(context)

        if hasattr(agent, "execute"):
            return agent.execute(context)

        raise AttributeError(
            f"{agent.__class__.__name__} has no execution interface."
        )