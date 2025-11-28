"""Тесты для Forecast"""
import pytest
from datetime import date
from forecasts.forecast import Forecast
from exceptions.weather_exceptions import InvalidForecastDataException


def test_forecast_init():
    """Тест инициализации прогноза"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)
    assert forecast.forecast_id == "F001"
    assert forecast.location_name == "Moscow"
    assert forecast.temperature == 15.0


def test_forecast_set_precipitation_probability():
    """Тест установки вероятности осадков"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)
    forecast.set_precipitation_probability(75.0)
    assert forecast.precipitation_probability == 75.0


def test_forecast_invalid_probability():
    """Тест невалидной вероятности"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)
    with pytest.raises(InvalidForecastDataException):
        forecast.set_precipitation_probability(150.0)


