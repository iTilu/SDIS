"""Тесты для WindSensor"""
import pytest
from sensors.wind_sensor import WindSensor


def test_wind_sensor_init():
    sensor = WindSensor("W001", 100.0, 0.0, 360)
    assert sensor.sensor_id == "W001"


def test_wind_sensor_set_wind_data():
    sensor = WindSensor("W001", 100.0, 0.0, 360)
    sensor.set_wind_data(25.0, 180)
    assert sensor.current_speed == 25.0
    assert sensor.current_direction == 180


