from core.asp.request import ASPRequest
from .adapter import MCPAdapter

adapter = MCPAdapter()


def optimize(
    task: str,
    budget: str = "medium",
    quality: str = "medium",
    latency: str = "normal",
    estimated_input_tokens: int = 0,
    estimated_output_tokens: int = 0,
):
    request = ASPRequest(
        task=task,
        budget=budget,
        quality=quality,
        latency=latency,
        estimated_input_tokens=estimated_input_tokens,
        estimated_output_tokens=estimated_output_tokens,
    )

    return adapter.optimize(request)


def recommend_strategy(
    task: str,
    estimated_input_tokens: int,
    estimated_output_tokens: int,
):
    """
    Backward-compatible API.

    Existing tests still use recommend_strategy().
    Internally it delegates to the new ASP pipeline.
    """

    response = optimize(
        task=task,
        estimated_input_tokens=estimated_input_tokens,
        estimated_output_tokens=estimated_output_tokens,
    )

    return {
        "strategy": response.strategy,
        "recommended_model": response.recommended_model,
        "estimated_cost": response.estimated_cost,
    }