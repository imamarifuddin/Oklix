from fastapi.testclient import TestClient

from api.app import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["name"] == "Oklix Decision Intelligence API"


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_optimize():

    response = client.post(
        "/optimize",
        json={
            "task": "chat",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "recommended_model" in data

    assert "execution_model" not in data
    assert data["execution_plan"][0]["model"] == data["recommended_model"]
    assert data["recommendation"]["model"] == data["recommended_model"]
    assert data["estimated_cost_detail"]["total_cost"] >= 0
    assert data["estimated_latency"]["lower_bound_ms"] > 0
    assert data["explanation"]["reasons"]
    assert data["tradeoffs"]
    feedback = client.post("/feedback", json={"recommendation_id": data["recommendation"]["recommendation_id"], "success": True, "latency": 100, "actual_cost": 0.01})
    assert feedback.json()["accepted"] is True
    assert client.get("/metrics").status_code == 200

def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0-rc.1"


def test_openapi_describes_recommendation_only_api():
    """Public OpenAPI metadata describes the stable recommendation endpoints."""

    schema = client.get("/openapi.json").json()

    optimize = schema["paths"]["/optimize"]["post"]
    assert optimize["summary"] == "Recommend an AI Strategy"
    assert "does not execute providers" in optimize["description"]

    feedback = schema["paths"]["/feedback"]["post"]
    assert feedback["summary"] == "Record Recommendation Feedback"
