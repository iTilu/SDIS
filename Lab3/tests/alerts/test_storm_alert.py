"""Тесты для StormAlert"""
from alerts.storm_alert import StormAlert


def test_storm_alert_init():
    alert = StormAlert("SA001", "Thunderstorm", 35.0, "Moscow")
    assert alert.alert_id == "SA001"
    assert alert.wind_speed == 35.0


