"""Тесты для Barometer"""
from equipment.barometer import Barometer


def test_barometer_init():
    baro = Barometer("BAR001", 1100.0, 0.01, "mercury")
    assert baro.device_id == "BAR001"
    assert baro.type == "mercury"


