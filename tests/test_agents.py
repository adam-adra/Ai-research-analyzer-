import os
import pytest
from app.agents.agent import build_agents
from app.tools.search_tool import get_search_tool

class MockSettings:
    model_name = "gemini/gemini-1.5-pro"

def test_build_agents():
    # Inject fake key for tests so CrewAI doesn't crash
    os.environ["GEMINI_API_KEY"] = "fake-key"
    
    settings = MockSettings()
    tools = [get_search_tool()]
    
    agents = build_agents(settings, tools)
    
    # Assert 4 agents are returned
    assert len(agents) == 4
    assert "research" in agents
    assert "market" in agents
    assert "risk" in agents
    assert "strategy" in agents
    
    # Assert roles
    assert agents["research"].role == "Senior Product Researcher"
    assert agents["market"].role == "Market Analyst"
    assert agents["risk"].role == "Risk & Feasibility Analyst"
    assert agents["strategy"].role == "Head of Strategy"
    
    # Assert tool assignment (only research should have tools)
    assert len(agents["research"].tools) == 1
    assert agents["research"].tools[0].name == "web_search"
    
    assert len(agents["market"].tools) == 0
    assert len(agents["risk"].tools) == 0
    assert len(agents["strategy"].tools) == 0
    
    # Assert delegation is off
    assert agents["research"].allow_delegation is False
    assert agents["market"].allow_delegation is False
    assert agents["risk"].allow_delegation is False
    assert agents["strategy"].allow_delegation is False
