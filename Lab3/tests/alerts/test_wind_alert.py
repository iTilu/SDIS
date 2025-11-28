"""Тесты для WindAlert"""
from alerts.wind_alert import WindAlert


def test_wind_alert_init():
    alert = WindAlert("WA001", 30.0, 270, "Moscow")
    assert alert.alert_id == "WA001"
    assert alert.wind_speed == 30.0


