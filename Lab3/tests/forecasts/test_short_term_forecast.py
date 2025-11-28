"""Тесты для ShortTermForecast"""
from forecasts.short_term_forecast import ShortTermForecast


def test_short_term_forecast_init():
    forecast = ShortTermForecast("ST001", "Moscow", 24, 18.0)
    assert forecast.forecast_id == "ST001"
    assert forecast.hours_ahead == 24


