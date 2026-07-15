from core.asp.request import ASPRequest
from core.asp.request_parser import RequestParser

from domain import TaskRequest
from domain.task import (
    BudgetLevel,
    LatencyLevel,
    QualityLevel,
)


def test_parser_exists():

    parser = RequestParser()

    assert parser is not None


def test_parse():

    parser = RequestParser()

    request = ASPRequest(
        task="chat",
    )

    task = parser.parse(request)

    assert isinstance(
        task,
        TaskRequest,
    )


def test_task_name():

    parser = RequestParser()

    request = ASPRequest(
        task="chat",
    )

    task = parser.parse(request)

    assert task.task == "chat"


def test_budget_mapping():

    parser = RequestParser()

    request = ASPRequest(
        task="chat",
        budget="low",
    )

    task = parser.parse(request)

    assert task.budget == BudgetLevel.LOW


def test_quality_mapping():

    parser = RequestParser()

    request = ASPRequest(
        task="chat",
        quality="high",
    )

    task = parser.parse(request)

    assert task.quality == QualityLevel.HIGH


def test_latency_mapping():

    parser = RequestParser()

    request = ASPRequest(
        task="chat",
        latency="fast",
    )

    task = parser.parse(request)

    assert task.latency == LatencyLevel.FAST