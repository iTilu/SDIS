"""Тесты для HumiditySensor"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from sensors.humidity_sensor import HumiditySensor
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException


def test_humidity_sensor_creation_valid():
    """Тест создания сенсора влажности с валидными данными"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    assert sensor.sensor_id == "H001"
    assert sensor.min_humidity == 0.0
    assert sensor.max_humidity == 100.0
    assert sensor.precision == 0.5
    assert sensor.is_active == True
    assert sensor.last_maintenance is None
    assert sensor.sensor_type == "capacitive"
    assert sensor.current_humidity is None


def test_humidity_sensor_creation_invalid_id():
    """Тест создания сенсора с невалидным ID"""
    with pytest.raises(ValueError, match="ID сенсора должен быть непустой строкой"):
        HumiditySensor("", 0.0, 100.0, 0.5)

    with pytest.raises(ValueError, match="ID сенсора должен быть непустой строкой"):
        HumiditySensor(None, 0.0, 100.0, 0.5)


def test_humidity_sensor_creation_invalid_min_humidity():
    """Тест создания сенсора с невалидной минимальной влажностью"""
    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        HumiditySensor("H001", -10.0, 100.0, 0.5)

    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        HumiditySensor("H001", 150.0, 100.0, 0.5)


def test_humidity_sensor_creation_invalid_max_humidity():
    """Тест создания сенсора с невалидной максимальной влажностью"""
    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        HumiditySensor("H001", 0.0, -50.0, 0.5)

    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        HumiditySensor("H001", 0.0, 150.0, 0.5)


def test_humidity_sensor_creation_invalid_precision():
    """Тест создания сенсора с невалидной точностью"""
    with pytest.raises(ValueError, match="Точность должна быть неотрицательным числом"):
        HumiditySensor("H001", 0.0, 100.0, -1.0)


def test_humidity_sensor_creation_boundary_values():
    """Тест создания сенсора с граничными значениями"""
    # Нулевые значения
    sensor1 = HumiditySensor("H001", 0.0, 0.0, 0.0)
    assert sensor1.min_humidity == 0.0
    assert sensor1.max_humidity == 0.0
    assert sensor1.precision == 0.0

    # Максимальные значения
    sensor2 = HumiditySensor("H002", 100.0, 100.0, 100.0)
    assert sensor2.min_humidity == 100.0
    assert sensor2.max_humidity == 100.0
    assert sensor2.precision == 100.0


def test_humidity_sensor_read_humidity_valid():
    """Тест чтения валидной влажности"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    sensor.set_humidity(65.0)

    assert sensor.read_humidity() == 65.0
    assert sensor.current_humidity == 65.0


def test_humidity_sensor_read_humidity_inactive():
    """Тест чтения влажности неактивным сенсором"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    sensor.set_humidity(65.0)
    sensor.is_active = False

    with pytest.raises(SensorMalfunctionException, match="Сенсор неактивен"):
        sensor.read_humidity()


def test_humidity_sensor_read_humidity_no_data():
    """Тест чтения влажности без данных"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    with pytest.raises(InvalidSensorDataException, match="Влажность не измерена"):
        sensor.read_humidity()


def test_humidity_sensor_set_humidity_valid():
    """Тест установки валидной влажности"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    sensor.set_humidity(65.0)
    assert sensor.current_humidity == 65.0

    sensor.set_humidity(0.0)
    assert sensor.current_humidity == 0.0

    sensor.set_humidity(100.0)
    assert sensor.current_humidity == 100.0


def test_humidity_sensor_set_humidity_invalid_type():
    """Тест установки влажности с невалидным типом"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    with pytest.raises(TypeError, match="Влажность должна быть числом"):
        sensor.set_humidity("65")

    with pytest.raises(TypeError, match="Влажность должна быть числом"):
        sensor.set_humidity(None)


def test_humidity_sensor_set_humidity_invalid_range():
    """Тест установки влажности вне допустимого диапазона"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    with pytest.raises(InvalidSensorDataException, match="Влажность должна быть от 0 до 100"):
        sensor.set_humidity(-5.0)

    with pytest.raises(InvalidSensorDataException, match="Влажность должна быть от 0 до 100"):
        sensor.set_humidity(150.0)


def test_humidity_sensor_set_humidity_boundary_values():
    """Тест установки граничных значений влажности"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    # Граничные значения
    sensor.set_humidity(0.0)
    assert sensor.current_humidity == 0.0

    sensor.set_humidity(100.0)
    assert sensor.current_humidity == 100.0


def test_humidity_sensor_perform_maintenance():
    """Тест выполнения обслуживания сенсора"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    sensor.is_active = False

    sensor.perform_maintenance()

    assert sensor.last_maintenance == "2024-01-01"
    assert sensor.is_active == True


def test_humidity_sensor_attach_to_station_valid():
    """Тест присоединения к валидной метеостанции"""
    from unittest.mock import Mock
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    station = Mock()
    station.add_humidity_sensor = Mock()

    sensor.attach_to_station(station)
    station.add_humidity_sensor.assert_called_once_with(sensor)


def test_humidity_sensor_attach_to_station_invalid():
    """Тест присоединения к невалидной метеостанции"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    with pytest.raises(ValueError, match="Метеостанция не может быть None"):
        sensor.attach_to_station(None)


def test_humidity_sensor_attach_to_station_inactive():
    """Тест присоединения неактивного сенсора к станции"""
    from unittest.mock import Mock
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    sensor.is_active = False

    station = Mock()

    with pytest.raises(ValueError, match="Сенсор неактивен и не может быть присоединен"):
        sensor.attach_to_station(station)


def test_humidity_sensor_create_measurement_valid():
    """Тест создания валидного измерения"""
    from unittest.mock import Mock
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    sensor.set_humidity(65.0)

    measurement = Mock()
    measurement.value = None
    measurement.set_parameter_type = Mock()
    measurement.set_accuracy = Mock()

    sensor.create_measurement(measurement)
    assert measurement.value == 65.0
    measurement.set_parameter_type.assert_called_once_with("humidity")
    measurement.set_accuracy.assert_called_once_with(0.5)


def test_humidity_sensor_create_measurement_invalid():
    """Тест создания невалидного измерения"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    with pytest.raises(ValueError, match="Измерение не может быть None"):
        sensor.create_measurement(None)


def test_humidity_sensor_create_measurement_no_data():
    """Тест создания измерения без данных сенсора"""
    from unittest.mock import Mock
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    measurement = Mock()
    measurement.value = None
    measurement.set_parameter_type = Mock()
    measurement.set_accuracy = Mock()

    # Метод не должен устанавливать значение, если данных нет
    sensor.create_measurement(measurement)
    assert measurement.value is None
    measurement.set_parameter_type.assert_not_called()
    measurement.set_accuracy.assert_not_called()


def test_humidity_sensor_current_humidity_property():
    """Тест свойства current_humidity"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    # До установки данных
    assert sensor.current_humidity is None

    # После установки данных
    sensor.set_humidity(65.0)
    assert sensor.current_humidity == 65.0

    # Обновление данных
    sensor.set_humidity(70.0)
    assert sensor.current_humidity == 70.0


def test_humidity_sensor_field_types():
    """Тест типов полей сенсора влажности"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)
    sensor.set_humidity(65.0)

    assert isinstance(sensor.sensor_id, str)
    assert isinstance(sensor.min_humidity, (int, float))
    assert isinstance(sensor.max_humidity, (int, float))
    assert isinstance(sensor.precision, (int, float))
    assert isinstance(sensor.is_active, bool)
    assert sensor.last_maintenance is None or isinstance(sensor.last_maintenance, str)
    assert isinstance(sensor.sensor_type, str)
    assert sensor.current_humidity is None or isinstance(sensor.current_humidity, (int, float))


def test_humidity_sensor_data_integrity():
    """Тест целостности данных сенсора влажности"""
    sensor = HumiditySensor("H001", 10.0, 90.0, 0.5)

    # Установка данных
    sensor.set_humidity(65.0)
    sensor.perform_maintenance()

    # Проверяем, что основные поля остались неизменными
    assert sensor.sensor_id == "H001"
    assert sensor.min_humidity == 10.0
    assert sensor.max_humidity == 90.0
    assert sensor.precision == 0.5
    assert sensor.sensor_type == "capacitive"

    # Проверяем измененные поля
    assert sensor.current_humidity == 65.0
    assert sensor.last_maintenance == "2024-01-01"
    assert sensor.is_active == True


def test_humidity_sensor_boundary_values():
    """Тест граничных значений для сенсора влажности"""
    # Минимальные значения
    sensor1 = HumiditySensor("H001", 0.0, 0.0, 0.0)
    sensor1.set_humidity(0.0)
    assert sensor1.read_humidity() == 0.0

    # Максимальные значения
    sensor2 = HumiditySensor("H002", 100.0, 100.0, 100.0)
    sensor2.set_humidity(100.0)
    assert sensor2.read_humidity() == 100.0

    # Высокая точность
    sensor3 = HumiditySensor("H003", 0.0, 100.0, 0.001)
    sensor3.set_humidity(50.123)
    assert sensor3.read_humidity() == 50.123


def test_humidity_sensor_workflow():
    """Тест полного жизненного цикла сенсора влажности"""
    sensor = HumiditySensor("H001", 20.0, 80.0, 0.5)

    # Начальное состояние
    assert sensor.is_active == True
    assert sensor.current_humidity is None
    assert sensor.last_maintenance is None

    # Первое измерение
    sensor.set_humidity(45.0)
    assert sensor.current_humidity == 45.0
    assert sensor.read_humidity() == 45.0

    # Обслуживание
    sensor.perform_maintenance()
    assert sensor.last_maintenance == "2024-01-01"
    assert sensor.is_active == True

    # Новые измерения
    sensor.set_humidity(60.0)
    assert sensor.current_humidity == 60.0

    # Деактивация
    sensor.is_active = False
    with pytest.raises(SensorMalfunctionException):
        sensor.read_humidity()

    # Реактивация и продолжение работы
    sensor.perform_maintenance()
    assert sensor.is_active == True
    assert sensor.read_humidity() == 60.0

    # Финальное измерение
    sensor.set_humidity(75.0)
    assert sensor.current_humidity == 75.0


def test_humidity_sensor_edge_cases():
    """Тест крайних случаев для сенсора влажности"""
    sensor = HumiditySensor("H001", 0.0, 100.0, 0.5)

    # Очень маленькие значения
    sensor.set_humidity(0.001)
    assert sensor.read_humidity() == 0.001

    # Очень большие значения
    sensor.set_humidity(99.999)
    assert sensor.read_humidity() == 99.999

    # Тип int вместо float
    sensor.set_humidity(50)  # int
    assert sensor.read_humidity() == 50.0  # должно работать

    # Деактивация без обслуживания
    sensor.is_active = False
    with pytest.raises(SensorMalfunctionException):
        sensor.read_humidity()

    # Попытка установить влажность неактивному сенсору (должно работать)
    sensor.set_humidity(30.0)  # set_humidity не проверяет is_active
    sensor.is_active = True
    assert sensor.read_humidity() == 30.0


