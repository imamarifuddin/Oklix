from fastapi.testclient import TestClient

from core.asp.server import app


client = TestClient(app)


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

    assert "execution_model" in data

def test_root():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Oklix ASP"

    assert data["version"] == "0.1.0"

def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"   