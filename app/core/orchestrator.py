import time
from typing import Tuple

from app.config import get_settings
from app.core.crew_engine import CrewEngine
from app.core.mock_engine import MockEngine
from app.schemas.report import FeasibilityReport


class Orchestrator:
    async def analyze(self, idea: str) -> Tuple[FeasibilityReport, float]:
        """
        this is the orchestrator of what engine should it choose
        even the mock engine where the api keys are missing or run
        the crew ai system
        """
        settings = get_settings()
        has_key = bool(
            settings.openai_api_key
            or settings.gemini_api_key
            or settings.openrouter_api_key
        )

        start_time = time.time()

        from typing import Union

        engine: Union[CrewEngine, MockEngine]
        if settings.use_real_crew and has_key:
            engine = CrewEngine()
        else:
            engine = MockEngine()

        result = await engine.analyze(idea)

        duration_ms = (time.time() - start_time) * 1000

        return (result, duration_ms)
