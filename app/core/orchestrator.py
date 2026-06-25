from app.config import get_settings
from app.core.mock_engine import MockEngine
from app.schemas.report import FeasibilityReport
from typing import Tuple
import time


class Orchestrator:
    def analyze(self, idea: str) -> Tuple[FeasibilityReport, float]:
        """
        this is the orchestrator of what engine should it choose
        even the mock engine where the api keys are missing or run
        the crew ai system
        """
        settings = get_settings()

        if not settings.use_real_crew or not settings.openai_api_key:
            start_time = time.time()
            mockengine = MockEngine()

            result = mockengine.analyze(idea)
            result.engine = "mock"
            duration_ms = (time.time() - start_time) * 1000

            return (result, duration_ms)

        elif settings.use_real_crew and settings.openai_api_key:
            # here you have to add the agent chain
            raise NotImplementedError("Real crew not implemented yet")

        raise ValueError("Invalid configuration state")
