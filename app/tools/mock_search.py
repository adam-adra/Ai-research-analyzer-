from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class SearchInput(BaseModel):
    query: str = Field(..., description="Search query for market/competitor research")


class MockWebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = (
        "Search the web for market data, competitors, and demand signals."
    )
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        query_lower = query.lower()
        if "competitor" in query_lower or "market" in query_lower:
            results = [
                "1. Market Overview: Growing rapidly with key players like Quizlet.",
                "2. Competitor Analysis: Startups are focusing on spaced repetition.",
                "3. Pricing: Average subscription costs range from $5 to $15/month.",
            ]
        elif "risk" in query_lower or "technical" in query_lower:
            results = [
                "1. Technical Risks: High LLM API costs and latency are concerns.",
                "2. Data Privacy: Strict educational privacy laws required.",
                "3. Accuracy: AI hallucinations remain a critical challenge.",
            ]
        else:
            results = [
                f"1. Top Result for '{query}': Significant interest observed.",
                f"2. Industry Trend: Many developers are exploring '{query}'.",
                "3. User Feedback: Early adopters report high satisfaction.",
            ]

        return "Mock Search Results:\n" + "\n".join(results)
