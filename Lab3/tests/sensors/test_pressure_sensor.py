"""Тесты для PressureSensor"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from sensors.pressure_sensor import PressureSensor
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException


def test_pressure_sensor_creation_valid():
    """Тест создания сенсора давления с валидными данными"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    assert sensor.sensor_id == "P001"
    assert sensor.min_pressure == 800.0
    assert sensor.max_pressure == 1100.0
    assert sensor.resolution == 0.01
    assert sensor.is_active == True
    assert sensor.altitude_correction == 0.0
    assert sensor.sensor_model == "barometric"


def test_pressure_sensor_creation_invalid_id():
    """Тест создания сенсора с невалидным ID"""
    with pytest.raises(ValueError, match="ID сенсора должен быть непустой строкой"):
        PressureSensor("", 800.0, 1100.0, 0.01)

    with pytest.raises(ValueError, match="ID сенсора должен быть непустой строкой"):
        PressureSensor(None, 800.0, 1100.0, 0.01)


def test_pressure_sensor_creation_invalid_min_pressure():
    """Тест создания сенсора с невалидным минимальным давлением"""
    with pytest.raises(ValueError, match="Давление должно быть положительным"):
        PressureSensor("P001", -100.0, 1100.0, 0.01)

    with pytest.raises(ValueError, match="Давление должно быть положительным"):
        PressureSensor("P001", "800", 1100.0, 0.01)


def test_pressure_sensor_creation_invalid_max_pressure():
    """Тест создания сенсора с невалидным максимальным давлением"""
    with pytest.raises(ValueError, match="Давление должно быть положительным"):
        PressureSensor("P001", 800.0, -500.0, 0.01)


def test_pressure_sensor_creation_invalid_resolution():
    """Тест создания сенсора с невалидным разрешением"""
    with pytest.raises(ValueError, match="Разрешение должно быть неотрицательным числом"):
        PressureSensor("P001", 800.0, 1100.0, -0.01)


def test_pressure_sensor_set_pressure_valid():
    """Тест установки валидного давления"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    sensor.set_pressure(1013.25)
    assert sensor.read_pressure() == 1013.25


def test_pressure_sensor_set_pressure_boundary():
    """Тест установки давления на границах диапазона"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    sensor.set_pressure(800.0)
    assert sensor.read_pressure() == 800.0

    sensor.set_pressure(1100.0)
    assert sensor.read_pressure() == 1100.0


def test_pressure_sensor_set_pressure_invalid_type():
    """Тест установки давления невалидного типа"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    with pytest.raises(TypeError, match="Давление должно быть числом"):
        sensor.set_pressure("1013.25")

    with pytest.raises(TypeError, match="Давление должно быть числом"):
        sensor.set_pressure(None)


def test_pressure_sensor_set_pressure_out_of_range():
    """Тест установки давления вне диапазона"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    with pytest.raises(InvalidSensorDataException, match="Давление вне допустимого диапазона"):
        sensor.set_pressure(700.0)  # Слишком низкое

    with pytest.raises(InvalidSensorDataException, match="Давление вне допустимого диапазона"):
        sensor.set_pressure(1200.0)  # Слишком высокое


def test_pressure_sensor_read_pressure_uninitialized():
    """Тест чтения неинициализированного давления"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    with pytest.raises(InvalidSensorDataException, match="Давление не измерено"):
        sensor.read_pressure()


def test_pressure_sensor_read_inactive():
    """Тест чтения давления неактивным сенсором"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    sensor.set_pressure(1013.25)
    sensor.is_active = False

    with pytest.raises(SensorMalfunctionException, match="Сенсор неактивен"):
        sensor.read_pressure()


def test_pressure_sensor_calibrate_valid():
    """Тест калибровки сенсора с валидными данными"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    sensor.calibrate(1013.25)
    assert sensor.read_pressure() == 1013.25


def test_pressure_sensor_calibrate_invalid_type():
    """Тест калибровки с невалидным типом данных"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    with pytest.raises(TypeError, match="Эталонное давление должно быть числом"):
        sensor.calibrate("1013.25")


def test_pressure_sensor_calibrate_inactive():
    """Тест калибровки неактивного сенсора"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    sensor.is_active = False

    with pytest.raises(SensorMalfunctionException, match="Сенсор неактивен"):
        sensor.calibrate(1013.25)


def test_pressure_sensor_calibrate_out_of_range():
    """Тест калибровки вне диапазона сенсора"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    with pytest.raises(InvalidSensorDataException, match="Давление вне допустимого диапазона"):
        sensor.calibrate(1200.0)


def test_pressure_sensor_set_altitude_correction_valid():
    """Тест установки валидной коррекции высоты"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    sensor.set_altitude_correction(-50.0)
    assert sensor.altitude_correction == -50.0


def test_pressure_sensor_set_altitude_correction_invalid():
    """Тест установки невалидной коррекции высоты"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    with pytest.raises(TypeError, match="Коррекция высоты должна быть числом"):
        sensor.set_altitude_correction("50.0")


def test_pressure_sensor_get_status():
    """Тест получения статуса сенсора"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    # Активный сенсор без данных
    status = sensor.get_status()
    assert "активен" in status
    assert "не измерено" in status

    # Активный сенсор с данными
    sensor.set_pressure(1013.25)
    status = sensor.get_status()
    assert "активен" in status
    assert "1013.25" in status

    # Неактивный сенсор
    sensor.is_active = False
    status = sensor.get_status()
    assert "неактивен" in status


def test_pressure_sensor_reset():
    """Тест сброса сенсора"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    sensor.set_pressure(1013.25)
    sensor.altitude_correction = 50.0

    sensor.reset()

    # Проверяем, что данные сброшены, но настройки остались
    assert sensor.sensor_id == "P001"
    assert sensor.min_pressure == 800.0
    assert sensor.max_pressure == 1100.0
    assert sensor.resolution == 0.01
    assert sensor.is_active == True

    # Проверяем, что данные сброшены
    with pytest.raises(InvalidSensorDataException):
        sensor.read_pressure()
    assert sensor.altitude_correction == 0.0


def test_pressure_sensor_field_types():
    """Тест типов полей сенсора давления"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)
    sensor.set_pressure(1013.25)
    sensor.set_altitude_correction(25.0)

    assert isinstance(sensor.sensor_id, str)
    assert isinstance(sensor.min_pressure, float)
    assert isinstance(sensor.max_pressure, float)
    assert isinstance(sensor.resolution, float)
    assert isinstance(sensor.is_active, bool)
    assert isinstance(sensor.altitude_correction, float)
    assert isinstance(sensor.sensor_model, str)


def test_pressure_sensor_data_integrity():
    """Тест целостности данных сенсора"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    # Изменяем поля
    sensor.set_pressure(1013.25)
    sensor.set_altitude_correction(50.0)

    # Проверяем, что основные поля остались неизменными
    assert sensor.sensor_id == "P001"
    assert sensor.min_pressure == 800.0
    assert sensor.max_pressure == 1100.0
    assert sensor.resolution == 0.01

    # Проверяем измененные поля
    assert sensor.read_pressure() == 1013.25
    assert sensor.altitude_correction == 50.0


def test_pressure_sensor_boundary_values():
    """Тест граничных значений для сенсора давления"""
    # Экстремальные диапазоны
    extreme_sensor = PressureSensor("P001", 1.0, 5000.0, 0.001)
    extreme_sensor.set_pressure(1.0)  # Очень низкое давление
    assert extreme_sensor.read_pressure() == 1.0

    extreme_sensor.set_pressure(5000.0)  # Очень высокое давление
    assert extreme_sensor.read_pressure() == 5000.0

    # Нулевое разрешение
    zero_res_sensor = PressureSensor("P002", 800.0, 1100.0, 0.0)
    assert zero_res_sensor.resolution == 0.0


def test_pressure_sensor_extreme_pressures():
    """Тест экстремальных давлений"""
    sensor = PressureSensor("P001", 500.0, 1500.0, 0.01)

    # Атмосферные давления
    pressures = [500.0, 700.0, 900.0, 1013.25, 1100.0, 1300.0, 1500.0]

    for pressure in pressures:
        sensor.set_pressure(pressure)
        assert sensor.read_pressure() == pressure


def test_pressure_sensor_precision():
    """Тест точности сенсора"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.001)

    # Тест с высокой точностью
    sensor.set_pressure(1013.256789)
    assert sensor.read_pressure() == 1013.256789


def test_pressure_sensor_altitude_corrections():
    """Тест коррекций высоты"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    # Разные коррекции высоты
    corrections = [-100.0, -50.0, 0.0, 50.0, 100.0, 500.0, 1000.0]

    for correction in corrections:
        sensor.set_altitude_correction(correction)
        assert sensor.altitude_correction == correction


def test_pressure_sensor_workflow():
    """Тест полного жизненного цикла сенсора давления"""
    # Создание сенсора
    sensor = PressureSensor("BARO001", 900.0, 1100.0, 0.1)

    # Инициализация
    assert sensor.is_active == True
    assert sensor.altitude_correction == 0.0

    # Измерение давления
    sensor.set_pressure(1013.25)
    assert sensor.read_pressure() == 1013.25

    # Калибровка
    sensor.calibrate(1012.8)
    assert sensor.read_pressure() == 1012.8

    # Коррекция высоты
    sensor.set_altitude_correction(150.0)  # Для высоты 150 м
    assert sensor.altitude_correction == 150.0

    # Проверка статуса
    status = sensor.get_status()
    assert "активен" in status

    # Сброс
    sensor.reset()
    assert sensor.altitude_correction == 0.0
    with pytest.raises(InvalidSensorDataException):
        sensor.read_pressure()


def test_pressure_sensor_multiple_measurements():
    """Тест множественных измерений"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    # Серия измерений
    pressures = [950.0, 980.0, 1013.25, 1020.0, 1050.0]

    for pressure in pressures:
        sensor.set_pressure(pressure)
        assert sensor.read_pressure() == pressure


def test_pressure_sensor_models():
    """Тест различных моделей сенсоров"""
    models = ["barometric", "piezoresistive", "capacitive", "optical", "MEMS"]

    for model in models:
        sensor = PressureSensor("TEST", 800.0, 1100.0, 0.01)
        sensor.sensor_model = model  # Предполагаем, что поле можно менять
        assert sensor.sensor_model == model


def test_pressure_sensor_error_handling():
    """Тест обработки ошибок сенсора"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    # Попытка чтения без установки давления
    with pytest.raises(InvalidSensorDataException):
        sensor.read_pressure()

    # Попытка чтения неактивным сенсором
    sensor.set_pressure(1013.25)
    sensor.is_active = False
    with pytest.raises(SensorMalfunctionException):
        sensor.read_pressure()

    # Попытка калибровки неактивного сенсора
    with pytest.raises(SensorMalfunctionException):
        sensor.calibrate(1013.25)

    # Попытка калибровки вне диапазона
    sensor.is_active = True
    with pytest.raises(InvalidSensorDataException):
        sensor.calibrate(1200.0)


def test_pressure_sensor_state_transitions():
    """Тест переходов состояний сенсора"""
    sensor = PressureSensor("P001", 800.0, 1100.0, 0.01)

    # Активное состояние без данных
    assert sensor.is_active == True
    with pytest.raises(InvalidSensorDataException):
        sensor.read_pressure()

    # Установка данных
    sensor.set_pressure(1013.25)
    assert sensor.read_pressure() == 1013.25

    # Переход в неактивное состояние
    sensor.is_active = False
    with pytest.raises(SensorMalfunctionException):
        sensor.read_pressure()

    # Возврат в активное состояние
    sensor.is_active = True
    assert sensor.read_pressure() == 1013.25


