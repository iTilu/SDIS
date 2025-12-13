"""Тесты для TemperatureSensor"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from sensors.temperature_sensor import TemperatureSensor
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException


def test_temperature_sensor_creation_valid():
    """Тест создания сенсора температуры с валидными данными"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    assert sensor.sensor_id == "T001"
    assert sensor.min_temp == -50.0
    assert sensor.max_temp == 50.0
    assert sensor.accuracy == 0.1
    assert sensor.is_active == True
    assert sensor.battery_level == 100.0
    assert sensor.calibration_date is None


def test_temperature_sensor_creation_invalid_id():
    """Тест создания сенсора с невалидным ID"""
    with pytest.raises(ValueError, match="ID сенсора должен быть непустой строкой"):
        TemperatureSensor("", -50.0, 50.0, 0.1)

    with pytest.raises(ValueError, match="ID сенсора должен быть непустой строкой"):
        TemperatureSensor(None, -50.0, 50.0, 0.1)


def test_temperature_sensor_creation_invalid_min_temp():
    """Тест создания сенсора с невалидной минимальной температурой"""
    with pytest.raises(TypeError, match="Минимальная температура должна быть числом"):
        TemperatureSensor("T001", "min", 50.0, 0.1)


def test_temperature_sensor_creation_invalid_max_temp():
    """Тест создания сенсора с невалидной максимальной температурой"""
    with pytest.raises(TypeError, match="Максимальная температура должна быть числом"):
        TemperatureSensor("T001", -50.0, "max", 0.1)


def test_temperature_sensor_creation_invalid_accuracy():
    """Тест создания сенсора с невалидной точностью"""
    with pytest.raises(ValueError, match="Точность должна быть неотрицательным числом"):
        TemperatureSensor("T001", -50.0, 50.0, -0.1)

    with pytest.raises(ValueError, match="Точность должна быть неотрицательным числом"):
        TemperatureSensor("T001", -50.0, 50.0, "accuracy")


def test_temperature_sensor_set_temperature_valid():
    """Тест установки валидной температуры"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.set_temperature(25.0)
    assert sensor.read_temperature() == 25.0

    sensor.set_temperature(-25.0)
    assert sensor.read_temperature() == -25.0

    sensor.set_temperature(0.0)
    assert sensor.read_temperature() == 0.0


def test_temperature_sensor_set_temperature_boundary():
    """Тест установки температуры на границах диапазона"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Граничные значения
    sensor.set_temperature(-50.0)
    assert sensor.read_temperature() == -50.0

    sensor.set_temperature(50.0)
    assert sensor.read_temperature() == 50.0


def test_temperature_sensor_set_temperature_invalid_type():
    """Тест установки температуры невалидного типа"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    with pytest.raises(TypeError, match="Температура должна быть числом"):
        sensor.set_temperature("25.0")

    with pytest.raises(TypeError, match="Температура должна быть числом"):
        sensor.set_temperature(None)


def test_temperature_sensor_set_temperature_out_of_range():
    """Тест установки температуры вне диапазона"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Слишком высокая температура
    with pytest.raises(InvalidSensorDataException, match="Температура вне допустимого диапазона"):
        sensor.set_temperature(100.0)

    # Слишком низкая температура
    with pytest.raises(InvalidSensorDataException, match="Температура вне допустимого диапазона"):
        sensor.set_temperature(-100.0)


def test_temperature_sensor_read_temperature_uninitialized():
    """Тест чтения неинициализированной температуры"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    with pytest.raises(InvalidSensorDataException, match="Температура не измерена"):
        sensor.read_temperature()


def test_temperature_sensor_read_inactive():
    """Тест чтения температуры неактивным сенсором"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.set_temperature(25.0)
    sensor.is_active = False

    with pytest.raises(SensorMalfunctionException, match="Сенсор неактивен"):
        sensor.read_temperature()


def test_temperature_sensor_calibrate_valid():
    """Тест калибровки сенсора с валидными данными"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Калибровка с эталонной температурой
    sensor.calibrate(20.0)
    assert sensor.read_temperature() == 20.0


def test_temperature_sensor_calibrate_invalid_type():
    """Тест калибровки с невалидным типом данных"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    with pytest.raises(TypeError, match="Эталонная температура должна быть числом"):
        sensor.calibrate("20.0")


def test_temperature_sensor_calibrate_inactive():
    """Тест калибровки неактивного сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.is_active = False

    with pytest.raises(SensorMalfunctionException, match="Сенсор неактивен"):
        sensor.calibrate(20.0)


def test_temperature_sensor_calibrate_out_of_range():
    """Тест калибровки вне диапазона сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    with pytest.raises(InvalidSensorDataException, match="Температура вне допустимого диапазона"):
        sensor.calibrate(100.0)


def test_temperature_sensor_check_battery_valid():
    """Тест проверки батареи с нормальным уровнем"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.check_battery()  # Должен работать без ошибок


def test_temperature_sensor_check_battery_low():
    """Тест проверки батареи с низким уровнем"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.battery_level = 5.0

    with pytest.raises(SensorMalfunctionException, match="Низкий уровень батареи"):
        sensor.check_battery()


def test_temperature_sensor_get_status():
    """Тест получения статуса сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Активный сенсор без данных
    status = sensor.get_status()
    assert "активен" in status
    assert "не измерена" in status

    # Активный сенсор с данными
    sensor.set_temperature(25.0)
    status = sensor.get_status()
    assert "активен" in status
    assert "25.0" in status

    # Неактивный сенсор
    sensor.is_active = False
    status = sensor.get_status()
    assert "неактивен" in status


def test_temperature_sensor_reset():
    """Тест сброса сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.set_temperature(25.0)
    sensor.calibration_date = "2024-01-01"
    sensor.battery_level = 50.0

    sensor.reset()

    # Проверяем, что данные сброшены, но настройки остались
    assert sensor.sensor_id == "T001"
    assert sensor.min_temp == -50.0
    assert sensor.max_temp == 50.0
    assert sensor.accuracy == 0.1
    assert sensor.is_active == True

    # Проверяем, что данные сброшены
    with pytest.raises(InvalidSensorDataException):
        sensor.read_temperature()
    assert sensor.calibration_date is None
    assert sensor.battery_level == 100.0


def test_temperature_sensor_field_types():
    """Тест типов полей сенсора температуры"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)
    sensor.set_temperature(25.0)

    assert isinstance(sensor.sensor_id, str)
    assert isinstance(sensor.min_temp, float)
    assert isinstance(sensor.max_temp, float)
    assert isinstance(sensor.accuracy, float)
    assert isinstance(sensor.is_active, bool)
    assert isinstance(sensor.battery_level, float)


def test_temperature_sensor_data_integrity():
    """Тест целостности данных сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Изменяем поля
    sensor.set_temperature(25.0)
    sensor.calibrate(20.0)
    sensor.battery_level = 80.0

    # Проверяем, что основные поля остались неизменными
    assert sensor.sensor_id == "T001"
    assert sensor.min_temp == -50.0
    assert sensor.max_temp == 50.0
    assert sensor.accuracy == 0.1

    # Проверяем измененные поля
    assert sensor.read_temperature() == 20.0  # Изменено калибровкой
    assert sensor.battery_level == 80.0
    assert sensor.is_active == True  # Не изменяли

    # Теперь изменяем активность
    sensor.is_active = False
    assert not sensor.is_active


def test_temperature_sensor_boundary_values():
    """Тест граничных значений для сенсора температуры"""
    # Экстремальные диапазоны
    extreme_sensor = TemperatureSensor("T001", -273.15, 1000.0, 0.01)
    extreme_sensor.set_temperature(-273.15)  # Абсолютный ноль
    assert extreme_sensor.read_temperature() == -273.15

    extreme_sensor.set_temperature(1000.0)  # Очень высокая температура
    assert extreme_sensor.read_temperature() == 1000.0

    # Нулевая точность
    zero_accuracy_sensor = TemperatureSensor("T002", -50.0, 50.0, 0.0)
    assert zero_accuracy_sensor.accuracy == 0.0


def test_temperature_sensor_extreme_temperatures():
    """Тест экстремальных температур"""
    sensor = TemperatureSensor("T001", -100.0, 100.0, 0.1)

    # Очень низкие температуры
    sensor.set_temperature(-99.0)
    assert sensor.read_temperature() == -99.0

    # Очень высокие температуры
    sensor.set_temperature(99.0)
    assert sensor.read_temperature() == 99.0

    # Переход через ноль
    sensor.set_temperature(-0.1)
    assert sensor.read_temperature() == -0.1

    sensor.set_temperature(0.1)
    assert sensor.read_temperature() == 0.1


def test_temperature_sensor_precision():
    """Тест точности сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.01)

    # Тест с высокой точностью
    sensor.set_temperature(25.123456)
    assert sensor.read_temperature() == 25.123456

    # Тест с десятичными дробями
    sensor.set_temperature(0.5)
    assert sensor.read_temperature() == 0.5


def test_temperature_sensor_workflow():
    """Тест полного жизненного цикла сенсора температуры"""
    # Создание сенсора
    sensor = TemperatureSensor("T001", -40.0, 40.0, 0.5)

    # Инициализация
    assert sensor.is_active == True
    assert sensor.battery_level == 100.0

    # Измерение температуры
    sensor.set_temperature(20.0)
    assert sensor.read_temperature() == 20.0

    # Калибровка
    sensor.calibrate(19.5)
    assert sensor.read_temperature() == 19.5

    # Проверка статуса
    status = sensor.get_status()
    assert "активен" in status

    # Сброс
    sensor.reset()
    assert sensor.battery_level == 100.0
    with pytest.raises(InvalidSensorDataException):
        sensor.read_temperature()


def test_temperature_sensor_multiple_measurements():
    """Тест множественных измерений"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Серия измерений
    temperatures = [10.0, 15.5, -5.0, 0.0, 25.0, -25.0, 40.0]

    for temp in temperatures:
        sensor.set_temperature(temp)
        assert sensor.read_temperature() == temp


def test_temperature_sensor_battery_management():
    """Тест управления батареей сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Нормальный уровень батареи
    sensor.battery_level = 50.0
    sensor.check_battery()  # Должен работать

    # Критический уровень
    sensor.battery_level = 10.0
    sensor.check_battery()  # Должен работать

    # Низкий уровень
    sensor.battery_level = 5.0
    with pytest.raises(SensorMalfunctionException):
        sensor.check_battery()

    # Нулевой уровень
    sensor.battery_level = 0.0
    with pytest.raises(SensorMalfunctionException):
        sensor.check_battery()


def test_temperature_sensor_different_ranges():
    """Тест сенсоров с разными диапазонами"""
    # Комнатный сенсор
    room_sensor = TemperatureSensor("ROOM", 15.0, 35.0, 0.1)
    room_sensor.set_temperature(25.0)
    assert room_sensor.read_temperature() == 25.0

    # Уличный сенсор
    outdoor_sensor = TemperatureSensor("OUTDOOR", -60.0, 60.0, 0.1)
    outdoor_sensor.set_temperature(-30.0)
    assert outdoor_sensor.read_temperature() == -30.0

    # Промышленный сенсор
    industrial_sensor = TemperatureSensor("INDUSTRIAL", -200.0, 500.0, 1.0)
    industrial_sensor.set_temperature(200.0)
    assert industrial_sensor.read_temperature() == 200.0


def test_temperature_sensor_error_handling():
    """Тест обработки ошибок сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Попытка чтения без установки температуры
    with pytest.raises(InvalidSensorDataException):
        sensor.read_temperature()

    # Попытка чтения неактивным сенсором
    sensor.set_temperature(25.0)
    sensor.is_active = False
    with pytest.raises(SensorMalfunctionException):
        sensor.read_temperature()

    # Попытка калибровки неактивного сенсора
    with pytest.raises(SensorMalfunctionException):
        sensor.calibrate(20.0)

    # Попытка калибровки вне диапазона
    sensor.is_active = True
    with pytest.raises(InvalidSensorDataException):
        sensor.calibrate(100.0)


def test_temperature_sensor_state_transitions():
    """Тест переходов состояний сенсора"""
    sensor = TemperatureSensor("T001", -50.0, 50.0, 0.1)

    # Активное состояние без данных
    assert sensor.is_active == True
    with pytest.raises(InvalidSensorDataException):
        sensor.read_temperature()

    # Установка данных
    sensor.set_temperature(25.0)
    assert sensor.read_temperature() == 25.0

    # Переход в неактивное состояние
    sensor.is_active = False
    with pytest.raises(SensorMalfunctionException):
        sensor.read_temperature()

    # Возврат в активное состояние
    sensor.is_active = True
    assert sensor.read_temperature() == 25.0


