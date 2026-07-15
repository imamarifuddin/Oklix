from pydantic import BaseModel, Field


class OptimizeRequest(BaseModel):
    task: str = Field(..., description="Task description")
    estimated_input_tokens: int = 0
    estimated_output_tokens: int = 0


class OptimizeResponse(BaseModel):
    strategy: str
    recommended_model: str
    estimated_cost: float