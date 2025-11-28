"""Тесты для WeatherAlert"""
from datetime import datetime
from alerts.weather_alert import WeatherAlert


def test_weather_alert_init():
    alert = WeatherAlert("A001", "Storm", "High", "Moscow")
    assert alert.alert_id == "A001"
    assert alert.severity == "High"


