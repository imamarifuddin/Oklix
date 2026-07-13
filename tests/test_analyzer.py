from core.analyzer import Analyzer

from domain import TaskRequest
from domain.profile import (
    TaskComplexity,
    TaskSize,
)
from domain.task import QualityLevel


def test_small_task():
    analyzer = Analyzer()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=1000,
            estimated_output_tokens=500,
        )
    )

    assert profile.size == TaskSize.SMALL


def test_medium_task():
    analyzer = Analyzer()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=20000,
            estimated_output_tokens=3000,
        )
    )

    assert profile.size == TaskSize.MEDIUM


def test_large_task():
    analyzer = Analyzer()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=100000,
            estimated_output_tokens=5000,
        )
    )

    assert profile.size == TaskSize.LARGE


def test_low_complexity():
    analyzer = Analyzer()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=1000,
            estimated_output_tokens=500,
            quality=QualityLevel.LOW,
        )
    )

    assert profile.complexity == TaskComplexity.LOW


def test_medium_complexity():
    analyzer = Analyzer()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=1000,
            estimated_output_tokens=500,
            quality=QualityLevel.MEDIUM,
        )
    )

    assert profile.complexity == TaskComplexity.MEDIUM


def test_high_complexity():
    analyzer = Analyzer()

    profile = analyzer.analyze(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=1000,
            estimated_output_tokens=500,
            quality=QualityLevel.HIGH,
        )
    )

    assert profile.complexity == TaskComplexity.HIGH