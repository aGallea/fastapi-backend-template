from fastapi.testclient import TestClient


def test_liveness(client: TestClient) -> None:
    response = client.get("/api/v1/healthcheck/liveness")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}


def test_readiness(client: TestClient) -> None:
    response = client.get("/api/v1/healthcheck/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
