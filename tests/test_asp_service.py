from core.asp.request import ASPRequest
from core.asp.service import ASPService
from domain import DecisionResponse


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
        DecisionResponse,
    )

    assert response.recommendation.provider
    assert response.recommendation.model
    assert response.recommendation_id
    assert response.execution_plan.type == "recommendation_only"
