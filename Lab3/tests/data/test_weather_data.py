"""Тесты для WeatherData"""
import pytest
from datetime import datetime
from data.weather_data import WeatherData
from exceptions.weather_exceptions import DataValidationException


def test_weather_data_init():
    """Тест инициализации данных о погоде"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)
    assert data.data_id == "WD001"
    assert data.temperature == 20.0
    assert data.humidity == 60.0


def test_weather_data_add_pressure():
    """Тест добавления давления"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)
    data.add_pressure(1013.25)
    assert data.pressure == 1013.25


def test_weather_data_validate():
    """Тест валидации данных"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)
    assert data.validate_data() is True


def test_weather_data_invalid_temperature():
    """Тест невалидной температуры"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)
    data.temperature = 150.0
    with pytest.raises(DataValidationException):
        data.validate_data()


