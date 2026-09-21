from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_ancestors():
    response = client.get(
        "/units/UNIT-123/ancestors",
        params={"max_depth": 50},
    )

    assert response.status_code == 200
    assert response.json() == {
        "unit_id": "UNIT-123",
        "max_depth": 50,
        "ancestors": [],
    }
