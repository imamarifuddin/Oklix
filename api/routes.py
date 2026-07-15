"""
API Routes.
"""

from fastapi import APIRouter

from api.version import DESCRIPTION, NAME, VERSION
from core.asp.request import ASPRequest
from core.asp.response import ASPResponse
from core.asp.service import ASPService

router = APIRouter()

service = ASPService()


@router.get("/")
def root():
    return {
        "name": NAME,
        "version": VERSION,
        "description": DESCRIPTION,
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": NAME,
        "version": VERSION,
    }


@router.get("/version")
def version():
    return {
        "name": NAME,
        "version": VERSION,
        "description": DESCRIPTION,
    }


@router.post(
    "/optimize",
    response_model=ASPResponse,
)
def optimize(
    request: ASPRequest,
):
    return service.optimize(request)