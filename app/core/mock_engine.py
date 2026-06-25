import random
import hashlib
from app.schemas.report import FeasibilityReport, Competitor


class MockEngine:
    """
    A simple deterministic engine that returns a fake FeasibilityReport
    without making any LLM or network calls.
    """

    def analyze(self, idea: str) -> FeasibilityReport:
        idea_hash = int(hashlib.md5(idea.encode("utf-8")).hexdigest(), 16)
        random.seed(idea_hash)

        words = idea.split()
        topic = " ".join(words[:4]) if len(words) > 4 else idea

        from typing import cast, Literal

        choices = ["build", "dont_build", "build_with_caveats"]
        raw_rec = random.choice(choices)
        recommendation = cast(
            Literal["build", "dont_build", "build_with_caveats"], raw_rec
        )

        return FeasibilityReport(
            idea=idea,
            market_overview=(
                f"The market for '{topic}' is growing rapidly, but highly competitive."
            ),
            competitors=[
                Competitor(
                    name=f"Legacy {topic} Corp",
                    description="The old, slow incumbent in this space.",
                    differentiator="They have deep pockets but terrible UX.",
                )
            ],
            opportunities=[
                f"First-mover advantage in modernizing '{topic}'.",
                "Appealing to Gen-Z audiences.",
            ],
            gaps=[
                "Lack of AI integration in existing tools.",
                "Poor mobile experience.",
            ],
            technical_feasibility=("Moderate. Requires a solid backend and clean UI."),
            risks=[
                "Customer acquisition costs are high.",
                "Incumbents might copy the feature.",
            ],
            recommendation=recommendation,
            confidence=0.55,
            reasoning=(
                f"Based on the analysis of '{topic}', the market has "
                "gaps but execution will be key."
            ),
            mvp_suggestion=(
                "A simple landing page with a waitlist to gauge real interest."
            ),
            engine="mock",
        )
