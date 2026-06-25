import os
from crewai_tools import SerperDevTool, TavilySearchTool

from app.config import get_settings
from app.tools.mock_search import MockWebSearchTool


def get_search_tool():
    """
    Returns a prebuilt web search tool from crewai_tools.
    Prefers Serper if available, otherwise falls back to Tavily.
    If no keys are found, falls back to a Mock Search Tool.
    """
    settings = get_settings()

    if settings.serper_api_key:
        os.environ["SERPER_API_KEY"] = settings.serper_api_key
        return SerperDevTool()

    elif settings.tavily_api_key:
        os.environ["TAVILY_API_KEY"] = settings.tavily_api_key
        return TavilySearchTool()

    else:
        return MockWebSearchTool()
