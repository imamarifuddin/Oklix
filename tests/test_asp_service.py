from core.asp.request import ASPRequest
from core.asp.response import ASPResponse
from core.asp.service import ASPService


def test_service_exists():

    service = ASPService()

    assert service is not None


def test_service_has_request_parser():

    service = ASPService()

    assert service.request_parser is not None


def test_service_has_recommendation_builder():

    service = ASPService()

    assert service.recommendation_builder is not None


def test_service_has_response_builder():

    service = ASPService()

    assert service.response_builder is not None


def test_optimize():

    service = ASPService()

    response = service.optimize(
        ASPRequest(
            task="chat",
        )
    )

    assert isinstance(
        response,
        ASPResponse,
    )

    assert response.recommended_provider != ""

    assert response.recommended_model != ""

    assert response.execution_provider != ""

    assert response.execution_model != ""