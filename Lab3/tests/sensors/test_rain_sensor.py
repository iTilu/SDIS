"""Тесты для RainSensor"""
from sensors.rain_sensor import RainSensor


def test_rain_sensor_init():
    sensor = RainSensor("R001", 200.0, 50.0, 0.1)
    assert sensor.sensor_id == "R001"


def test_rain_sensor_set_rain_data():
    sensor = RainSensor("R001", 200.0, 50.0, 0.1)
    sensor.set_rain_data(10.5, 5.2)
    assert sensor.rainfall_amount == 10.5


