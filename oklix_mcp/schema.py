from pydantic import BaseModel


class OptimizeRequest(BaseModel):
    task: str
    budget: str = "medium"
    quality: str = "medium"
    latency: str = "normal"


class OptimizeResponse(BaseModel):
    provider: str
    model: str
    strategy: str