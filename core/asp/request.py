"""
ASP Request.
"""

from pydantic import BaseModel


class ASPRequest(BaseModel):

    task: str

    budget: str = "medium"

    quality: str = "medium"

    latency: str = "normal"

    estimated_input_tokens: int = 0

    estimated_output_tokens: int = 0