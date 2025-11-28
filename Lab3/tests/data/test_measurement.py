"""Тесты для Measurement"""
from datetime import datetime
from data.measurement import Measurement


def test_measurement_init():
    timestamp = datetime.now()
    measurement = Measurement("M001", 25.5, "Celsius", timestamp)
    assert measurement.measurement_id == "M001"
    assert measurement.value == 25.5


