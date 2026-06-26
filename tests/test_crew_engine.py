import os
from unittest.mock import patch, MagicMock
from app.core.crew_engine import CrewEngine
from app.schemas.report import FeasibilityReport

import pytest

@pytest.mark.asyncio
@patch("app.core.crew_engine.Crew.kickoff")
async def test_crew_engine(mock_kickoff):
    os.environ["GEMINI_API_KEY"] = "fake-key"
    os.environ["OPENAI_API_KEY"] = "fake-key"
    
    # Mock the crew output
    mock_result = MagicMock()
    mock_report = FeasibilityReport(
        idea="Test idea",
        market_overview="Test market",
        competitors=[],
        opportunities=[],
        gaps=[],
        technical_feasibility="Feasible",
        risks=[],
        recommendation="build",
        confidence=0.8,
        reasoning="Because.",
        mvp_suggestion="None",
        engine="mock" # Initially mock
    )
    mock_result.pydantic = mock_report
    mock_kickoff.return_value = mock_result
    
    engine = CrewEngine()
    result = await engine.analyze("Test idea")
    
    # The engine provenance should be overwritten to 'crew' by the engine
    assert result.engine == "crew"
    assert result.idea == "Test idea"
    assert result.recommendation == "build"
