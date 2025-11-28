"""Тесты для WeatherStation"""
import pytest
from stations.weather_station import WeatherStation


def test_weather_station_init():
    """Тест инициализации метеостанции"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)
    assert station.station_id == "WS001"
    assert station.name == "Main Station"
    assert station.latitude == 55.7558
    assert station.longitude == 37.6173


def test_weather_station_invalid_latitude():
    """Тест невалидной широты"""
    with pytest.raises(ValueError):
        WeatherStation("WS001", "Main Station", 100.0, 37.6173)


def test_weather_station_set_elevation():
    """Тест установки высоты"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)
    station.set_elevation(150.0)
    assert station.elevation == 150.0


