"""
API Routes.
"""

from fastapi import APIRouter, status

from api.version import DESCRIPTION, NAME, VERSION
from core.asp.request import ASPRequest
from core.asp.response import ASPResponse
from core.asp.service import ASPService
from api.models import FeedbackRequest

router = APIRouter()

service = ASPService()


@router.get(
    "/",
    tags=["System"],
    summary="API Information",
    description="Return general information about the Oklix Decision Intelligence API.",
    response_description="Application metadata",
)
def root():
    return {
        "name": NAME,
        "version": VERSION,
        "description": DESCRIPTION,
    }


@router.get(
    "/health",
    tags=["System"],
    summary="Health Check",
    description="Verify that the API service is running correctly.",
    response_description="Health status",
)
def health():
    return {
        "status": "healthy",
        "service": NAME,
        "version": VERSION,
    }


@router.get(
    "/version",
    tags=["System"],
    summary="Version Information",
    description="Return version and build information.",
    response_description="Version information",
)
def version():
    return {
        "name": NAME,
        "version": VERSION,
        "build": "hackathon-2026",
    }


@router.post(
    "/optimize",
    tags=["Optimization"],
    summary="Recommend an AI Strategy",
    description="""
Analyze an AI workload and return a recommendation for the caller to execute.

The recommendation considers:

- AI capability
- Cost efficiency
- Latency
- Estimated token usage
- Provider availability
- Decision Intelligence ranking and explainable tradeoffs

Oklix does not execute providers, tools, or workflows.
""",
    response_model=ASPResponse,
    response_description="Structured, non-executable decision recommendation",
    responses={
        200: {
            "description": "Recommendation generated successfully.",
            "content": {
                "application/json": {
                    "example": {
                        "strategy": "balanced",
                        "recommended_provider": "openai",
                        "recommended_model": "gpt-4.1-mini",
                        "estimated_cost": 0.01,
                        "estimated_latency_ms": 900,
                        "confidence": 0.9,
                        "reason": "Best balance of task fit, cost, and latency.",
                    }
                }
            },
        }
    },
)
def optimize(
    request: ASPRequest,
):
    return service.optimize(request)


@router.post(
    "/feedback",
    tags=["Optimization"],
    status_code=status.HTTP_200_OK,
    summary="Record Recommendation Feedback",
    description="Record caller-reported outcomes to adapt future recommendations; no task is executed.",
    response_description="Feedback acceptance status",
)
def feedback(request: FeedbackRequest):
    """Record caller-reported outcomes without executing any task."""
    return {"accepted": service.feedback(request.recommendation_id, request.success, request.latency, request.actual_cost, request.error)}


@router.get(
    "/metrics",
    tags=["Optimization"],
    summary="Read Decision Metrics",
    description="Return metadata-only recommendation-history metrics.",
    response_description="Decision Intelligence metrics",
)
def metrics():
    """Return metadata-only Decision Intelligence dashboard metrics."""
    return service.history.metrics()
