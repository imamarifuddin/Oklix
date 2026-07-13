"""
MCP Tools exposed by Oklix.
"""

from fastmcp import FastMCP

from core.analyzer import Analyzer
from core.optimizer import Optimizer
from domain import TaskRequest

mcp = FastMCP("Oklix")

_analyzer = Analyzer()
_optimizer = Optimizer()


@mcp.tool
def recommend_strategy(
    task: str,
    estimated_input_tokens: int,
    estimated_output_tokens: int,
    budget: str = "medium",
    quality: str = "medium",
    latency: str = "normal",
):
    """
    Recommend the best execution strategy.
    """

    request = TaskRequest(
        task=task,
        estimated_input_tokens=estimated_input_tokens,
        estimated_output_tokens=estimated_output_tokens,
        budget=budget,
        quality=quality,
        latency=latency,
    )

    profile = _analyzer.analyze(request)

    recommendation = _optimizer.optimize(profile)

    return recommendation.model_dump()