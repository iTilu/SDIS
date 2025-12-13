"""Тесты для AirQualitySensor"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from sensors.air_quality_sensor import AirQualitySensor
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException


def test_air_quality_sensor_creation_valid():
    """Тест создания сенсора качества воздуха с валидными данными"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    assert sensor.sensor_id == "AQ001"
    assert sensor.pm25_max == 500.0
    assert sensor.pm10_max == 600.0
    assert sensor.co_max == 50.0
    assert sensor.is_active == True
    assert sensor.air_quality_index == 0
    assert sensor.pm25_value is None  # Через property


def test_air_quality_sensor_creation_invalid_id():
    """Тест создания сенсора с невалидным ID"""
    with pytest.raises(ValueError, match="ID сенсора должен быть непустой строкой"):
        AirQualitySensor("", 500.0, 600.0, 50.0)

    with pytest.raises(ValueError, match="ID сенсора должен быть непустой строкой"):
        AirQualitySensor(None, 500.0, 600.0, 50.0)


def test_air_quality_sensor_creation_invalid_pm25_max():
    """Тест создания сенсора с невалидным максимумом PM2.5"""
    with pytest.raises(ValueError, match="Максимальный PM2.5 должен быть неотрицательным"):
        AirQualitySensor("AQ001", -100.0, 600.0, 50.0)

    with pytest.raises(ValueError, match="Максимальный PM2.5 должен быть неотрицательным"):
        AirQualitySensor("AQ001", "500", 600.0, 50.0)


def test_air_quality_sensor_creation_invalid_pm10_max():
    """Тест создания сенсора с невалидным максимумом PM10"""
    with pytest.raises(ValueError, match="Максимальный PM10 должен быть неотрицательным"):
        AirQualitySensor("AQ001", 500.0, -200.0, 50.0)

    with pytest.raises(ValueError, match="Максимальный PM10 должен быть неотрицательным"):
        AirQualitySensor("AQ001", 500.0, None, 50.0)


def test_air_quality_sensor_creation_invalid_co_max():
    """Тест создания сенсора с невалидным максимумом CO"""
    with pytest.raises(ValueError, match="Максимальный CO должен быть неотрицательным"):
        AirQualitySensor("AQ001", 500.0, 600.0, -10.0)


def test_air_quality_sensor_set_data_valid():
    """Тест установки валидных данных качества воздуха"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    sensor.set_air_quality_data(25.0, 30.0, 5.0)

    assert sensor.read_pm25() == 25.0
    assert sensor.read_pm10() == 30.0
    assert sensor.read_co() == 5.0
    assert sensor.air_quality_index == (25.0 + 30.0) / 2  # 27.5


def test_air_quality_sensor_set_data_invalid_pm25():
    """Тест установки данных с невалидным PM2.5"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    with pytest.raises(ValueError, match="PM2.5 должен быть неотрицательным"):
        sensor.set_air_quality_data(-5.0, 30.0, 5.0)

    with pytest.raises(ValueError, match="PM2.5 должен быть неотрицательным"):
        sensor.set_air_quality_data("25", 30.0, 5.0)


def test_air_quality_sensor_set_data_invalid_pm10():
    """Тест установки данных с невалидным PM10"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    with pytest.raises(ValueError, match="PM10 должен быть неотрицательным"):
        sensor.set_air_quality_data(25.0, -10.0, 5.0)


def test_air_quality_sensor_set_data_invalid_co():
    """Тест установки данных с невалидным CO"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    with pytest.raises(ValueError, match="CO должен быть неотрицательным"):
        sensor.set_air_quality_data(25.0, 30.0, -1.0)


def test_air_quality_sensor_read_pm25_inactive():
    """Тест чтения PM2.5 неактивным сенсором"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    sensor.is_active = False

    with pytest.raises(SensorMalfunctionException, match="Сенсор неактивен"):
        sensor.read_pm25()


def test_air_quality_sensor_read_pm25_no_data():
    """Тест чтения PM2.5 без данных"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    with pytest.raises(InvalidSensorDataException, match="PM2.5 не измерен"):
        sensor.read_pm25()


def test_air_quality_sensor_read_pm10_inactive():
    """Тест чтения PM10 неактивным сенсором"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    sensor.set_air_quality_data(25.0, 30.0, 5.0)
    sensor.is_active = False

    with pytest.raises(SensorMalfunctionException, match="Сенсор неактивен"):
        sensor.read_pm10()


def test_air_quality_sensor_read_pm10_no_data():
    """Тест чтения PM10 без данных"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    with pytest.raises(InvalidSensorDataException, match="PM10 не измерен"):
        sensor.read_pm10()


def test_air_quality_sensor_read_co_inactive():
    """Тест чтения CO неактивным сенсором"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    sensor.set_air_quality_data(25.0, 30.0, 5.0)
    sensor.is_active = False

    with pytest.raises(SensorMalfunctionException, match="Сенсор неактивен"):
        sensor.read_co()


def test_air_quality_sensor_read_co_no_data():
    """Тест чтения CO без данных"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    with pytest.raises(InvalidSensorDataException, match="CO не измерен"):
        sensor.read_co()


def test_air_quality_sensor_calculate_aqi():
    """Тест расчета индекса качества воздуха"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    # До установки данных
    assert sensor.air_quality_index == 0

    # После установки данных
    sensor.set_air_quality_data(25.0, 30.0, 5.0)
    assert sensor.air_quality_index == 27.5  # (25 + 30) / 2

    # Обновление данных
    sensor.set_air_quality_data(40.0, 50.0, 10.0)
    assert sensor.air_quality_index == 45.0  # (40 + 50) / 2


def test_air_quality_sensor_attach_to_station_valid():
    """Тест присоединения к валидной метеостанции"""
    from unittest.mock import Mock
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    station = Mock()
    station.name = "Test Station"

    # Метод не должен выбрасывать исключение
    sensor.attach_to_station(station)


def test_air_quality_sensor_attach_to_station_invalid():
    """Тест присоединения к невалидной метеостанции"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    with pytest.raises(ValueError, match="Метеостанция не может быть None"):
        sensor.attach_to_station(None)


def test_air_quality_sensor_attach_to_station_inactive():
    """Тест присоединения неактивного сенсора к станции"""
    from unittest.mock import Mock
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    sensor.is_active = False

    station = Mock()
    station.name = "Test Station"

    with pytest.raises(ValueError, match="Сенсор неактивен и не может быть присоединен"):
        sensor.attach_to_station(station)


def test_air_quality_sensor_create_measurement_valid():
    """Тест создания валидного измерения"""
    from unittest.mock import Mock
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    sensor.set_air_quality_data(25.0, 30.0, 5.0)

    measurement = Mock()
    measurement.value = None
    measurement.set_parameter_type = Mock()

    sensor.create_measurement(measurement)
    assert measurement.value == 25.0
    measurement.set_parameter_type.assert_called_once_with("pm25")


def test_air_quality_sensor_create_measurement_invalid():
    """Тест создания невалидного измерения"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    with pytest.raises(ValueError, match="Измерение не может быть None"):
        sensor.create_measurement(None)


def test_air_quality_sensor_create_measurement_no_data():
    """Тест создания измерения без данных сенсора"""
    from unittest.mock import Mock
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    measurement = Mock()
    measurement.value = None
    measurement.set_parameter_type = Mock()

    # Метод не должен устанавливать значение, если данных нет
    sensor.create_measurement(measurement)
    # value остается None, так как данных нет
    assert measurement.value is None
    measurement.set_parameter_type.assert_not_called()


def test_air_quality_sensor_pm25_value_property():
    """Тест свойства pm25_value"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    # До установки данных
    assert sensor.pm25_value is None

    # После установки данных
    sensor.set_air_quality_data(25.0, 30.0, 5.0)
    assert sensor.pm25_value == 25.0


def test_air_quality_sensor_boundary_values():
    """Тест граничных значений для сенсора"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    # Нулевые значения (допустимые)
    sensor.set_air_quality_data(0.0, 0.0, 0.0)
    assert sensor.read_pm25() == 0.0
    assert sensor.read_pm10() == 0.0
    assert sensor.read_co() == 0.0
    assert sensor.air_quality_index == 0.0

    # Максимальные значения из конструктора
    # (хотя метод set_air_quality_data не проверяет максимумы)
    sensor.set_air_quality_data(500.0, 600.0, 50.0)
    assert sensor.read_pm25() == 500.0
    assert sensor.read_pm10() == 600.0
    assert sensor.read_co() == 50.0
    assert sensor.air_quality_index == (500.0 + 600.0) / 2


def test_air_quality_sensor_field_types():
    """Тест типов полей сенсора качества воздуха"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)
    sensor.set_air_quality_data(25.0, 30.0, 5.0)

    assert isinstance(sensor.sensor_id, str)
    assert isinstance(sensor.pm25_max, (int, float))
    assert isinstance(sensor.pm10_max, (int, float))
    assert isinstance(sensor.co_max, (int, float))
    assert isinstance(sensor.is_active, bool)
    assert isinstance(sensor.air_quality_index, (int, float))
    assert sensor.pm25_value is None or isinstance(sensor.pm25_value, (int, float))


def test_air_quality_sensor_data_integrity():
    """Тест целостности данных сенсора качества воздуха"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    # Установка данных
    sensor.set_air_quality_data(25.0, 30.0, 5.0)

    # Проверка, что основные поля остались неизменными
    assert sensor.sensor_id == "AQ001"
    assert sensor.pm25_max == 500.0
    assert sensor.pm10_max == 600.0
    assert sensor.co_max == 50.0

    # Проверка измененных полей
    assert sensor.pm25_value == 25.0
    assert sensor.air_quality_index == 27.5
    assert sensor.is_active == True


def test_air_quality_sensor_workflow():
    """Тест полного жизненного цикла сенсора качества воздуха"""
    sensor = AirQualitySensor("AQ001", 500.0, 600.0, 50.0)

    # Начальное состояние
    assert sensor.is_active == True
    assert sensor.pm25_value is None
    assert sensor.air_quality_index == 0

    # Установка данных
    sensor.set_air_quality_data(25.0, 30.0, 5.0)
    assert sensor.pm25_value == 25.0
    assert sensor.air_quality_index == 27.5

    # Чтение данных
    assert sensor.read_pm25() == 25.0
    assert sensor.read_pm10() == 30.0
    assert sensor.read_co() == 5.0

    # Деактивация
    sensor.is_active = False
    with pytest.raises(SensorMalfunctionException):
        sensor.read_pm25()

    # Реактивация и новые данные
    sensor.is_active = True
    sensor.set_air_quality_data(40.0, 45.0, 8.0)
    assert sensor.read_pm25() == 40.0
    assert sensor.air_quality_index == (40.0 + 45.0) / 2  # 42.5


