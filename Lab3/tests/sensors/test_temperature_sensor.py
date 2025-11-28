"""Тесты для TemperatureSensor"""
import pytest
from sensors.temperature_sensor import TemperatureSensor
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException


def test_temperature_sensor_init():
    """Тест инициализации сенсора температуры"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    assert sensor.sensor_id == "T001"
    assert sensor.min_temp == -50.0
    assert sensor.max_temp == 50.0
    assert sensor.accuracy == 0.1
    assert sensor.is_active is True


def test_temperature_sensor_set_temperature():
    """Тест установки температуры"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.set_temperature(25.0)
    assert sensor.current_temperature == 25.0


def test_temperature_sensor_invalid_temperature():
    """Тест невалидной температуры"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    with pytest.raises(InvalidSensorDataException):
        sensor.set_temperature(100.0)


def test_temperature_sensor_read_inactive():
    """Тест чтения неактивного сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.is_active = False
    with pytest.raises(SensorMalfunctionException):
        sensor.read_temperature()


