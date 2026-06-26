from crewai import Task

from app.schemas.report import FeasibilityReport


def build_tasks(agents: dict) -> list[Task]:
    """
    Builds the 4 sequential tasks and wires them together via the context parameter.
    """

    research_task = Task(
        description="Research the idea: {idea}. Use the web_search tool to find concrete demand signals, competitors, and context.",
        expected_output="A bulleted list of demand signals, competitors, and sources.",
        agent=agents["research"],
    )

    market_task = Task(
        description="Analyze demand, audience, and competitors for {idea} based on the research provided.",
        expected_output="Market overview + competitor list + opportunities and gaps.",
        agent=agents["market"],
        context=[research_task],
    )

    risk_task = Task(
        description="Evaluate technical, market, cost, and feasibility risks for {idea}.",
        expected_output="Categorized risk list with severity.",
        agent=agents["risk"],
        context=[research_task, market_task],
    )

    decision_task = Task(
        description="Synthesize all findings for {idea} into a final recommendation.",
        expected_output="A complete feasibility report including build/don't-build decision and reasoning.",
        agent=agents["strategy"],
        context=[research_task, market_task, risk_task],
        output_pydantic=FeasibilityReport,
    )

    return [research_task, market_task, risk_task, decision_task]
