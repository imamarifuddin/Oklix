from fastapi.testclient import TestClient

from api.app import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["name"] == "Oklix ASP"


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

    assert "execution_model" in data