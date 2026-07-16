"""API-boundary validation for completed Decision Intelligence responses."""

from domain import DecisionResponse


class ResponseBuilder:
    """Validate a complete decision response before it reaches the API layer."""

    def build(self, response: DecisionResponse) -> DecisionResponse:
        """Return a validated copy of the complete response model."""

        return DecisionResponse.model_validate(response)
