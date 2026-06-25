from app.core.mock_engine import MockEngine

def test_mock_engine_determinism():
    engine = MockEngine()
    idea = "I want to build an AI study assistant"
    
    # Generate two reports from the exact same idea
    report1 = engine.analyze(idea)
    report2 = engine.analyze(idea)
    
    # Assert they are perfectly identical (Deterministic)
    assert report1.model_dump() == report2.model_dump()

def test_mock_engine_idea_awareness():
    engine = MockEngine()
    
    report1 = engine.analyze("A new kind of electric bicycle")
    report2 = engine.analyze("A social network for dogs")
    
    # Assert that different ideas yield different reports
    # (specifically, the templated strings should differ)
    assert report1.market_overview != report2.market_overview
    
    # Assert it correctly stamps the engine as 'mock'
    assert report1.engine == "mock"
