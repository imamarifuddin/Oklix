# Oklix

Oklix is a Decision Intelligence Engine for AI agents and applications. It analyzes a task, evaluates local model metadata, and returns an explainable recommendation. The caller remains solely responsible for execution.

## What Oklix does

- Analyzes task requirements and token estimates.
- Compares model capability, cost, latency, reliability, provider health, and historical experience.
- Produces a ranked, explainable, non-executable recommendation with alternatives and tradeoffs.
- Accepts caller-reported feedback to adapt future recommendations.

## What Oklix never does

- Call an AI provider or SDK.
- Execute tools, workflows, filesystems, browsers, or MCP servers.
- Orchestrate agents or act as an agent runtime.

## Architecture

```text
Caller Agent
    -> FastAPI API
    -> ASP Service
    -> Decision Core
    -> Domain models
    -> DecisionResponse
    -> Caller Agent executes independently
```

The complete architectural contract is in [docs/VISION.md](docs/VISION.md), [docs/PRINCIPLES.md](docs/PRINCIPLES.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/ROADMAP.md](docs/ROADMAP.md), and [docs/DECISIONS.md](docs/DECISIONS.md).

## Installation

```bash
python -m venv .venv
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn api.app:app --reload
```

OpenAPI documentation is available at `http://127.0.0.1:8000/docs`.

## API

`POST /optimize` returns a `DecisionResponse` that includes the selected model, ranking, explainable cost and latency estimates, alternatives, tradeoffs, and a recommendation-only execution plan.

```json
{
  "task": "Review a Python pull request",
  "estimated_input_tokens": 6000,
  "estimated_output_tokens": 1200
}
```

`POST /feedback` records outcomes reported by the caller. `GET /metrics` exposes metadata-only recommendation history metrics.

## Testing

```bash
pytest
```

## License

MIT
