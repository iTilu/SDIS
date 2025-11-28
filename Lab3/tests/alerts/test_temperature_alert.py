"""Тесты для TemperatureAlert"""
from alerts.temperature_alert import TemperatureAlert


def test_temperature_alert_init():
    alert = TemperatureAlert("TA001", "Heat", 40.0, 35.0)
    assert alert.alert_id == "TA001"
    assert alert.temperature == 40.0


