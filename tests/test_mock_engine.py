from app.core.mock_engine import MockEngine


def test_mock_engine_determinism():
    engine = MockEngine()
    idea = "I want to build an AI study assistant"

    report1 = engine.analyze(idea)
    report2 = engine.analyze(idea)

    assert report1.model_dump() == report2.model_dump()


def test_mock_engine_idea_awareness():
    engine = MockEngine()

    report1 = engine.analyze("A new kind of electric bicycle")
    report2 = engine.analyze("A social network for dogs")

    assert report1.market_overview != report2.market_overview

    assert report1.engine == "mock"
