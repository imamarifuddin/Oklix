"""
Oklix Agent.
"""

from core.analyzer import Analyzer
from core.decision_engine import DecisionEngine
from core.execution_executor import ExecutionExecutor
from core.execution_planner import ExecutionPlanner
from core.providers import ProviderRegistry

from core.logger import OklixLogger
from core.decision_report import DecisionReport

from domain import TaskRequest

from core.runtime import Runtime
from core.multi_agent import MultiAgent
from domain import ExecutionContext
from core.mcp_server import MCPServer


class OklixAgent:
    """
    Main Oklix Agent.
    """

    def __init__(self) -> None:

        """
        Initialize the Oklix agent.
        """

        # Provider registry
        self.registry = ProviderRegistry()

        # Default execution backend (kept for backward compatibility)
        self.provider = self.registry.default()

        # Pipeline components
        self.analyzer = Analyzer()

        self.decision_engine = DecisionEngine()

        self.execution_planner = ExecutionPlanner()

        self.executor = ExecutionExecutor()

        self.runtime = Runtime()

        self.multi_agent = MultiAgent()

        self.mcp_server = MCPServer()

        self.multi_agent.register(
            "executor",
            self.executor,
        )
           

    def chat(
        self,
        prompt: str,
    ) -> str:
        """
        Execute one complete Decision Intelligence pipeline.
        """

        # --------------------------------------------------
        # Build request
        # --------------------------------------------------

        request = TaskRequest(
            task=prompt,
            estimated_input_tokens=max(
                1,
                len(prompt) // 4,
            ),
            estimated_output_tokens=1024,
        )

        # --------------------------------------------------
        # Analyze
        # --------------------------------------------------

        profile = self.analyzer.analyze(request)

        OklixLogger.analyzer(profile)

        # --------------------------------------------------
        # Decide
        # --------------------------------------------------

        recommendation = self.decision_engine.decide(profile)

        OklixLogger.decision(recommendation)

        OklixLogger.ranking(recommendation)

        # --------------------------------------------------
        # NEW
        # Decision Report
        # --------------------------------------------------

        print(
            DecisionReport.build(
                request=request,
                profile=profile,
                recommendation=recommendation,
            )
        )

        # --------------------------------------------------
        # Planner
        # --------------------------------------------------

        plan = self.execution_planner.build(
            profile=profile,
            recommendation=recommendation,
            prompt=prompt,
        )

        OklixLogger.planner()

        # --------------------------------------------------
        # Execute
        # --------------------------------------------------

        context = self.runtime.create_context(
            plan=plan,
            profile=profile,
            recommendation=recommendation,
            prompt=prompt,
        )

        result = self.multi_agent.execute(
            "executor",
            context,
        )

        return result.output