"""Тесты для UVSensor"""
from sensors.uv_sensor import UVSensor


def test_uv_sensor_init():
    sensor = UVSensor("UV001", 15.0, "280-400nm", 0.5)
    assert sensor.sensor_id == "UV001"


def test_uv_sensor_set_uv_index():
    sensor = UVSensor("UV001", 15.0, "280-400nm", 0.5)
    sensor.set_uv_index(7.5)
    assert sensor.current_uv_index == 7.5


