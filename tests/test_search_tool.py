from app.tools.search_tool import get_search_tool
from app.tools.mock_search import MockWebSearchTool
from app.config import Settings


def test_search_tool_instantiation_serper(monkeypatch):
    monkeypatch.setattr(
        "app.tools.search_tool.get_settings",
        lambda: Settings(serper_api_key="dummy_serper", tavily_api_key=None),
    )

    tool = get_search_tool()
    assert tool is not None
    assert "Search" in tool.name


def test_search_tool_instantiation_tavily(monkeypatch):
    monkeypatch.setattr(
        "app.tools.search_tool.get_settings",
        lambda: Settings(serper_api_key=None, tavily_api_key="dummy_tavily"),
    )

    tool = get_search_tool()
    assert tool is not None


def test_search_tool_mock_fallback(monkeypatch):
    monkeypatch.setattr(
        "app.tools.search_tool.get_settings",
        lambda: Settings(serper_api_key=None, tavily_api_key=None),
    )

    tool = get_search_tool()
    assert isinstance(tool, MockWebSearchTool)
    
    result = tool._run("competitor")
    assert "Mock Search Results" in result
