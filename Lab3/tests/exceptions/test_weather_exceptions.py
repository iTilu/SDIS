"""Тесты для исключений"""
import pytest
from exceptions.weather_exceptions import (
    WeatherException,
    InvalidSensorDataException,
    ForecastNotFoundException,
    SensorMalfunctionException
)


def test_weather_exception():
    """Тест базового исключения"""
    exc = WeatherException("Test error")
    assert str(exc) == "Test error"
    assert exc.message == "Test error"


def test_invalid_sensor_data_exception():
    """Тест исключения невалидных данных сенсора"""
    exc = InvalidSensorDataException("Invalid data")
    assert isinstance(exc, WeatherException)
    assert exc.message == "Invalid data"


def test_forecast_not_found_exception():
    """Тест исключения отсутствия прогноза"""
    exc = ForecastNotFoundException("Forecast not found")
    assert isinstance(exc, WeatherException)


