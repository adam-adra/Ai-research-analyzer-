import os
from app.tasks.tasks import build_tasks
from app.agents.agent import build_agents
from app.tools.search_tool import get_search_tool
from app.schemas.report import FeasibilityReport

class MockSettings:
    model_name = "gemini/gemini-1.5-pro"

def test_build_tasks():
    os.environ["GEMINI_API_KEY"] = "fake-key"
    settings = MockSettings()
    tools = [get_search_tool()]
    
    agents = build_agents(settings, tools)
    tasks = build_tasks(agents)
    
    assert len(tasks) == 4
    
    research_task = tasks[0]
    market_task = tasks[1]
    risk_task = tasks[2]
    decision_task = tasks[3]
    
    # Check contexts
    assert len(market_task.context) == 1
    assert market_task.context[0] == research_task
    
    assert len(risk_task.context) == 2
    assert research_task in risk_task.context
    assert market_task in risk_task.context
    
    assert len(decision_task.context) == 3
    assert research_task in decision_task.context
    assert market_task in decision_task.context
    assert risk_task in decision_task.context
    
    # Check pydantic output on final task
    assert decision_task.output_pydantic == FeasibilityReport
