from fastapi.testclient import TestClient


def test_post_request(client: TestClient) -> None:
    response = client.post("/api/v1/utils/test-request")
    assert response.status_code == 201
    assert response.json() == {"message": "Test response"}
