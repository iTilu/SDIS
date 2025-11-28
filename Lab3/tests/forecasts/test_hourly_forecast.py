"""Тесты для HourlyForecast"""
from forecasts.hourly_forecast import HourlyForecast


def test_hourly_forecast_init():
    forecast = HourlyForecast("H001", "Moscow", 14, 20.0)
    assert forecast.forecast_id == "H001"
    assert forecast.hour == 14


