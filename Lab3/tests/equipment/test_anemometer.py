"""Тесты для Anemometer"""
from equipment.anemometer import Anemometer


def test_anemometer_init():
    anemo = Anemometer("AN001", 100.0, 0.1, "cup")
    assert anemo.device_id == "AN001"
    assert anemo.sensor_type == "cup"


