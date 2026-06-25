import os
from crewai import Agent, LLM
from app.config import get_settings, Settings

os.environ["GEMINI_API_KEY"] = get_settings().gemini_api_key or "fake-key"

def build_llm(s: Settings) -> LLM:
    return LLM(model=s.model_name, temperature=0.3)

def build_agents(settings: Settings, tools: list) -> dict[str, Agent]:
    """
    Factory to build and return the 4 pipeline agents.
    """
    my_llm = build_llm(settings)
    
    research_agent = Agent(
        role="Senior Product Researcher",
        goal="Gather demand signals, competitors, and context for {idea}",
        backstory="You are meticulous and only trust evidence you can cite. You dig deep to find real market data.",
        tools=tools,
        llm=my_llm,
        allow_delegation=False,
        verbose=True,
    )
    
    market_agent = Agent(
        role="Market Analyst",
        goal="Assess demand, audience, competitive landscape; identify similar products",
        backstory="You are an expert at identifying market trends, target demographics, and analyzing competitor strengths and weaknesses.",
        llm=my_llm,
        allow_delegation=False,
        verbose=True,
    )
    
    risk_agent = Agent(
        role="Risk & Feasibility Analyst",
        goal="Evaluate technical risk, market saturation, cost/complexity, feasibility constraints",
        backstory="You are a skeptical, pragmatic analyst who looks for reasons an idea might fail. You prioritize technical and financial reality over hype.",
        llm=my_llm,
        allow_delegation=False,
        verbose=True,
    )
    
    strategy_agent = Agent(
        role="Head of Strategy",
        goal="Synthesize everything into build / don't-build with reasoning + MVP",
        backstory="You are a decisive product leader who makes data-driven decisions on whether to invest in a project.",
        llm=my_llm,
        allow_delegation=False,
        verbose=True,
    )
    
    return {
        "research": research_agent,
        "market": market_agent,
        "risk": risk_agent,
        "strategy": strategy_agent
    }
