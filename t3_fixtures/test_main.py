from main import get_weather

def test_get_weather():
    assert get_weather(21)=="hot"
    assert get_weather(25)!="cold"
    assert get_weather(25)=="hot"
    assert get_weather(18)=="cold"