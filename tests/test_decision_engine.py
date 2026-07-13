from core.decision_engine import DecisionEngine
import pytest

from core.decision_engine import DecisionEngine

def test_engine_exists():

    engine = DecisionEngine()

    assert engine is not None

def test_decide_not_implemented():

    engine = DecisionEngine()

    with pytest.raises(NotImplementedError):

        engine.decide(None)