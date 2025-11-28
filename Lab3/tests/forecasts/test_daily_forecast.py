"""Тесты для DailyForecast"""
from datetime import date
from forecasts.daily_forecast import DailyForecast


def test_daily_forecast_init():
    forecast_date = date(2024, 1, 15)
    forecast = DailyForecast("D001", "Moscow", forecast_date, 25.0, 15.0)
    assert forecast.forecast_id == "D001"
    assert forecast.high_temp == 25.0
    assert forecast.low_temp == 15.0


