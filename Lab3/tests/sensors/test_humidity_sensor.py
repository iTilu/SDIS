"""Тесты для HumiditySensor"""
import pytest
from sensors.humidity_sensor import HumiditySensor
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException


def test_humidity_sensor_init():
    """Тест инициализации сенсора влажности"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    assert sensor.sensor_id == "H001"
    assert sensor.min_humidity == 0.0
    assert sensor.max_humidity == 100.0
    assert sensor.precision == 0.5


def test_humidity_sensor_set_humidity():
    """Тест установки влажности"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    sensor.set_humidity(65.0)
    assert sensor.current_humidity == 65.0


def test_humidity_sensor_invalid_humidity():
    """Тест невалидной влажности"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    with pytest.raises(InvalidSensorDataException):
        sensor.set_humidity(150.0)


