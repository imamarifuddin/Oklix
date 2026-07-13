from core.capability_engine import CapabilityEngine


def test_supports_json():

    engine = CapabilityEngine()

    assert engine.supports(
        "gpt-4.1-mini",
        "json_mode",
    )


def test_strength():

    engine = CapabilityEngine()

    assert engine.has_strength(
        "claude-sonnet-4",
        "reasoning",
    )


def test_context():

    engine = CapabilityEngine()

    assert (
        engine.context_window(
            "gemini-2.5-flash"
        )
        > 100000
    )


def test_output_tokens():

    engine = CapabilityEngine()

    assert (
        engine.max_output_tokens(
            "claude-sonnet-4"
        )
        == 64000
    )