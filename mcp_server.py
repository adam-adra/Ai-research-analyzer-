from mcp.server.fastmcp import FastMCP
from app.core.orchestrator import Orchestrator

mcp = FastMCP("AI product researcher")

@mcp.tool()
async def analyze_idea(idea: str) -> str:
    """
    Analyzes a product or startup idea using a multi-agent AI crew.
    Returns a detailed feasibility report including market analysis, competitors, and risks.
    """
    import sys
    import os
    import contextlib
    
    orchestrator = Orchestrator()
    
    # Redirect stdout to stderr to prevent CrewAI from corrupting the MCP JSON-RPC protocol over stdio
    with contextlib.redirect_stdout(sys.stderr):
        report, duration_ms = await orchestrator.analyze(idea)

    competitors_str = "\n".join([f"- {c.name}: {c.description}" for c in report.competitors])
    opps_str = "\n".join([f"- {o}" for o in report.opportunities])
    gaps_str = "\n".join([f"- {g}" for g in report.gaps])
        
    return f"""
    # Feasibility Report for: {report.idea}
    (Generated in {duration_ms:.0f}ms via {report.engine})
    
    ## Market Overview
    {report.market_overview}
    
    ## Technical Feasibility
    {report.technical_feasibility}
    
    ## Opportunities
    {opps_str}

    ## Market Gaps
    {gaps_str}

    ## Top Competitors
    {competitors_str}
    """

if __name__ == "__main__":
    mcp.run()
