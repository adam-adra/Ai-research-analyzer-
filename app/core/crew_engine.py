import asyncio

from crewai import Crew, Process

from app.agents.agent import build_agents
from app.config import get_settings
from app.schemas.report import FeasibilityReport
from app.tasks.tasks import build_tasks
from app.tools.search_tool import get_search_tool


class CrewEngine:
    async def analyze(self, idea: str) -> FeasibilityReport:
        """
        Kicks off the real CrewAI multi-agent pipeline.
        """
        settings = get_settings()
        tools = [get_search_tool()]

        agents_dict = build_agents(settings, tools)
        tasks_list = build_tasks(agents_dict)

        crew = Crew(
            agents=list(agents_dict.values()),
            tasks=tasks_list,
            process=Process.sequential,
            verbose=True,
        )

        result = await asyncio.to_thread(crew.kickoff, inputs={"idea": idea})

        from typing import cast

        # type: ignore[union-attr]
        report = cast(FeasibilityReport, getattr(result, "pydantic", None))

        if not report:
            raise ValueError("Crew failed to produce a valid FeasibilityReport JSON.")

        report.engine = "crew"

        return report
