"""Architecture-boundary tests for the recommendation-only product."""

from pathlib import Path


ROOT = Path(__file__).parents[1]


def _source_files(directory: str) -> list[Path]:
    """Return Python source files below a repository package."""

    return list((ROOT / directory).rglob("*.py"))


def test_dependency_direction_is_inward_only():
    """Core and domain layers remain independent of API and application layers."""

    for path in _source_files("core"):
        content = path.read_text(encoding="utf-8")
        assert "from api" not in content
        assert "import api" not in content
        assert "from app" not in content
        assert "import app" not in content

    for path in _source_files("domain"):
        content = path.read_text(encoding="utf-8")
        assert "from core" not in content
        assert "import core" not in content
        assert "from api" not in content
        assert "import api" not in content


def test_execution_and_runtime_packages_are_absent():
    """The repository contains no legacy execution, agent, provider, or MCP runtimes."""

    forbidden_modules = (
        "core/execution_executor.py",
        "core/tool_router.py",
    )
    forbidden_packages = ("app", "core/executors", "core/mcp", "core/providers")

    for relative_path in forbidden_modules:
        assert not (ROOT / relative_path).exists()

    for relative_path in forbidden_packages:
        assert not list((ROOT / relative_path).glob("*.py"))


def test_decision_core_has_no_provider_sdk_imports():
    """Decision logic relies on local metadata, never provider SDKs."""

    for path in _source_files("core"):
        content = path.read_text(encoding="utf-8")
        assert "from openai" not in content
        assert "import openai" not in content
        assert "fastmcp" not in content.lower()
