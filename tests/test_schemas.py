from pydantic import ValidationError
import pytest
from app.schemas.report import AnalyzeRequest, FeasibilityReport, Competitor

def test_analyze_request_valid():
    req = AnalyzeRequest(idea="I want to build an AI study assistant")
    assert req.idea == "I want to build an AI study assistant"

def test_analyze_request_too_short():
    with pytest.raises(ValidationError):
        AnalyzeRequest(idea="too short")

def test_feasibility_report_valid():
    report = FeasibilityReport(
        idea="A great app",
        market_overview="Huge market",
        competitors=[
            Competitor(name="Rival", description="They do things", differentiator=None)
        ],
        opportunities=["Big money"],
        gaps=["No AI features yet"],
        technical_feasibility="Easy",
        risks=["People don't like it"],
        recommendation="build",
        confidence=0.85,
        reasoning="Because it's awesome",
        mvp_suggestion="A simple landing page",
        engine="mock"
    )
    assert report.recommendation == "build"
    assert report.confidence == 0.85

def test_feasibility_report_invalid_recommendation():
    with pytest.raises(ValidationError):
        FeasibilityReport(
            idea="A great app",
            market_overview="Huge market",
            competitors=[],
            opportunities=[],
            gaps=[],
            technical_feasibility="Easy",
            risks=[],
            recommendation="maybe", 
            confidence=0.85,
            reasoning="Because it's awesome",
            mvp_suggestion=None,
            engine="mock"
        )
