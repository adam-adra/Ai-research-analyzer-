import random
import hashlib
from app.schemas.report import FeasibilityReport, Competitor

class MockEngine:
    """
    A simple deterministic engine that returns a fake FeasibilityReport 
    without making any LLM or network calls.
    """

    def analyze(self, idea: str) -> FeasibilityReport:
        # 1. Determinism: We want the exact same idea to always return the exact same report.
        # We do this by creating a hash of the idea and seeding the random generator with it.
        idea_hash = int(hashlib.md5(idea.encode("utf-8")).hexdigest(), 16)
        random.seed(idea_hash)

        # 2. Basic Idea Awareness: Grab the first few words to make the report feel customized
        words = idea.split()
        topic = " ".join(words[:4]) if len(words) > 4 else idea

        # 3. Simple Heuristic for Recommendation
        # If the idea is very short, we randomly decide to build or not. 
        # But since random is seeded, it will always be consistent for that specific idea!
        choices = ["build", "dont_build", "build_with_caveats"]
        recommendation = random.choice(choices)

        # 4. Construct and return the perfectly validated Pydantic schema
        return FeasibilityReport(
            idea=idea,
            market_overview=f"The market for '{topic}' is growing rapidly, but highly competitive.",
            competitors=[
                Competitor(
                    name=f"Legacy {topic} Corp",
                    description="The old, slow incumbent in this space.",
                    differentiator="They have deep pockets but terrible UX."
                )
            ],
            opportunities=[
                f"First-mover advantage in modernizing '{topic}'.",
                "Appealing to Gen-Z audiences."
            ],
            gaps=[
                "Lack of AI integration in existing tools.",
                "Poor mobile experience."
            ],
            technical_feasibility="Moderate. Requires a solid backend and clean UI.",
            risks=[
                "Customer acquisition costs are high.",
                "Incumbents might copy the feature."
            ],
            recommendation=recommendation,
            confidence=0.55,  # We are honest that this is a mid-tier mock confidence
            reasoning=f"Based on the analysis of '{topic}', the market has gaps but execution will be key.",
            mvp_suggestion="A simple landing page with a waitlist to gauge real interest.",
            engine="mock"  # We honestly stamp it as a mock report
        )
