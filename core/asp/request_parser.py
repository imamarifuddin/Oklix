"""
ASP Request Parser.

Convert ASP requests into internal TaskRequest objects.
"""

from core.asp.request import ASPRequest

from domain import TaskRequest
from domain.task import (
    BudgetLevel,
    LatencyLevel,
    QualityLevel,
)


class RequestParser:
    """
    Convert ASP requests into TaskRequest objects.
    """

    def parse(
        self,
        request: ASPRequest,
    ) -> TaskRequest:
        """
        Convert an ASP request into a TaskRequest.
        """

        return TaskRequest(
            task=request.task,
            estimated_input_tokens=request.estimated_input_tokens,
            estimated_output_tokens=request.estimated_output_tokens,
            budget=BudgetLevel(request.budget),
            quality=QualityLevel(request.quality),
            latency=LatencyLevel(request.latency),
        )