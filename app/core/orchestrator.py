import time
from typing import Tuple

from app.config import get_settings
from app.core.crew_engine import CrewEngine
from app.core.mock_engine import MockEngine
from app.schemas.report import FeasibilityReport

import asyncio
import logging
from fastapi import HTTPException


class Orchestrator:
    async def analyze(self, idea: str) -> Tuple[FeasibilityReport, float]:
        """
        this is the orchestrator of what engine should it choose
        even the mock engine where the api keys are missing or run
        the crew ai system
        """
        logger = logging.getLogger(__name__)
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

        try:
            result = await asyncio.wait_for(
                engine.analyze(idea),
                timeout=settings.request_timeout_seconds
            )
        except asyncio.TimeoutError:
            logger.warning(
                f"Engine {engine.__class__.__name__} timed out after {settings.request_timeout_seconds}s. Degrading to MockEngine."
            )
            engine = MockEngine()
            result = await engine.analyze(idea)
            result.engine = "mock_fallback"
        except Exception as e:
            logger.error(f"Unexpected error during analysis: {e}", exc_info=True)
            raise HTTPException(
                status_code=500,
                detail="An internal error occurred during analysis. Please try again later.",
            )

        duration_ms = (time.time() - start_time) * 1000

        return (result, duration_ms)
