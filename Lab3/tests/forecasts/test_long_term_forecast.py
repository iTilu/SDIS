"""Тесты для LongTermForecast"""
from forecasts.long_term_forecast import LongTermForecast


def test_long_term_forecast_init():
    forecast = LongTermForecast("LT001", "Moscow", 7, 15.0)
    assert forecast.forecast_id == "LT001"
    assert forecast.days_ahead == 7


