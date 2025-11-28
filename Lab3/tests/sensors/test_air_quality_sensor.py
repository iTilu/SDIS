"""Тесты для AirQualitySensor"""
from sensors.air_quality_sensor import AirQualitySensor


def test_air_quality_sensor_init():
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    assert sensor.sensor_id == "AQ001"


def test_air_quality_sensor_set_data():
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    sensor.set_air_quality_data(25.0, 30.0, 5.0)
    assert sensor.pm25_value == 25.0
    assert sensor.pm10_value == 30.0


