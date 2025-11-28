"""Тесты для VisibilitySensor"""
from sensors.visibility_sensor import VisibilitySensor


def test_visibility_sensor_init():
    sensor = VisibilitySensor("V001", 50.0, 0.0, "km")
    assert sensor.sensor_id == "V001"


def test_visibility_sensor_set_visibility():
    sensor = VisibilitySensor("V001", 50.0, 0.0, "km")
    sensor.set_visibility(10.0)
    assert sensor.current_visibility == 10.0


