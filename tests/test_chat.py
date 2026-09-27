from fastapi.testclient import TestClient

from app.main import app
from app.api import chat


client = TestClient(app)


def test_chat(monkeypatch):

    def mock_generate_response(message: str) -> str:
        return f"Mock response for: {message}"

    monkeypatch.setattr(
        chat,
        "generate_response",
        mock_generate_response
    )

    response = client.post(
        "/api/chat",
        json={
            "message": "Explain dependency injection."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "response" in data
    assert data["response"] == "Mock response for: Explain dependency injection."


def test_chat_validation():

    response = client.post(
        "/api/chat",
        json={}
    )

    assert response.status_code == 422