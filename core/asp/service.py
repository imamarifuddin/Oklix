from core.asp.request import ASPRequest
from core.asp.request_parser import RequestParser
from core.asp.response import ASPResponse
from core.asp.response_builder import ResponseBuilder

from core.recommendation_builder import RecommendationBuilder


class ASPService:
    """
    ASP orchestration service.
    """

    def __init__(self) -> None:

        self.request_parser = RequestParser()

        self.recommendation_builder = RecommendationBuilder()

        self.response_builder = ResponseBuilder()

    def optimize(
        self,
        request: ASPRequest,
    ) -> ASPResponse:
        """
        Execute the complete optimization pipeline.
        """

        task = self.request_parser.parse(
            request,
        )

        recommendation = self.recommendation_builder.build(
            task,
        )

        return self.response_builder.build(
            recommendation,
        )