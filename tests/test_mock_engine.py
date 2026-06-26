import pytest
from app.core.mock_engine import MockEngine

@pytest.mark.asyncio
async def test_mock_engine_determinism():
    engine = MockEngine()
    idea = "I want to build an AI study assistant"

    report1 = await engine.analyze(idea)
    report2 = await engine.analyze(idea)

    assert report1.model_dump() == report2.model_dump()


@pytest.mark.asyncio
async def test_mock_engine_idea_awareness():
    engine = MockEngine()

    report1 = await engine.analyze("A new kind of electric bicycle")
    report2 = await engine.analyze("A social network for dogs")

    assert report1.market_overview != report2.market_overview

    assert report1.engine == "mock"
