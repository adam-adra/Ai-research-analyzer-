from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch
from app.config import Settings

client = TestClient(app)

@patch("app.core.orchestrator.get_settings")
def test_analyze_valid_idea(mock_get_settings):
    # Force the orchestrator to use the mock engine for this test
    mock_get_settings.return_value = Settings(use_real_crew=False)

    response = client.post(
        "/analyze",
        json={"idea": "Should I build an AI study assistant for medical students?"},
    )

    assert response.status_code == 200

    data = response.json()
    assert "report" in data
    assert data["report"]["engine"] == "mock"
    assert data["meta"]["engine"] == "mock"
    assert "durations_ms" in data["meta"]


def test_analyze_idea_too_short():
    response = client.post("/analyze", json={"idea": "hi"})

    assert response.status_code == 422


def test_analyze_empty_body():
    response = client.post("/analyze", json={})

    # Should be rejected by Pydantic validation
    assert response.status_code == 422
