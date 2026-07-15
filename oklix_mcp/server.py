from oklix_mcp.tools import recommend_strategy
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Oklix")


@mcp.tool()
def recommend(
    task: str,
    estimated_input_tokens: int = 0,
    estimated_output_tokens: int = 0,
):
    """
    Recommend the best execution strategy.
    """

    return recommend_strategy(
        task=task,
        estimated_input_tokens=estimated_input_tokens,
        estimated_output_tokens=estimated_output_tokens,
    )


if __name__ == "__main__":
    mcp.run()