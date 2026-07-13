"""
Tests for DecisionEngine.
"""

import pytest

from core.decision_engine import DecisionEngine
from domain import TaskRequest


def test_engine_exists():
    engine = DecisionEngine()

    assert engine is not None


def test_decide_returns_recommendation():
    engine = DecisionEngine()

    recommendation = engine.decide(
        TaskRequest(
            task="summarize",
            estimated_input_tokens=5000,
            estimated_output_tokens=1000,
        )
    )

    assert recommendation is not None
    assert recommendation.recommended_model != ""
    assert recommendation.provider != ""
    assert recommendation.estimated_cost > 0
    assert recommendation.confidence > 0