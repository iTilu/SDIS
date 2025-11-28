"""Тесты для PressureSensor"""
import pytest
from sensors.pressure_sensor import PressureSensor


def test_pressure_sensor_init():
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    assert sensor.sensor_id == "P001"
    assert sensor.is_active is True


def test_pressure_sensor_set_pressure():
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    sensor.set_pressure(1013.25)
    assert sensor.current_pressure == 1013.25


