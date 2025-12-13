"""Тесты для WeatherData"""
import pytest
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from data.weather_data import WeatherData
from exceptions.weather_exceptions import DataValidationException


def test_weather_data_creation_valid():
    """Тест создания данных о погоде с валидными параметрами"""
    timestamp = datetime(2024, 1, 15, 12, 30)
    data = WeatherData("WD001", timestamp, 20.5, 65.0)

    assert data.data_id == "WD001"
    assert data.timestamp == timestamp
    assert data.temperature == 20.5
    assert data.humidity == 65.0
    assert data.pressure is None
    assert data.wind_speed is None
    assert data.wind_direction is None
    assert data.rainfall is None
    assert data.visibility is None
    assert data.data_quality == "good"


def test_weather_data_creation_invalid_id():
    """Тест создания данных с невалидным ID"""
    timestamp = datetime.now()

    with pytest.raises(ValueError, match="ID данных должен быть непустой строкой"):
        WeatherData("", timestamp, 20.0, 60.0)

    with pytest.raises(ValueError, match="ID данных должен быть непустой строкой"):
        WeatherData(None, timestamp, 20.0, 60.0)


def test_weather_data_creation_invalid_timestamp():
    """Тест создания данных с невалидной временной меткой"""
    with pytest.raises(TypeError, match="Временная метка должна быть datetime"):
        WeatherData("WD001", "2024-01-15", 20.0, 60.0)

    with pytest.raises(TypeError, match="Временная метка должна быть datetime"):
        WeatherData("WD001", None, 20.0, 60.0)


def test_weather_data_creation_invalid_temperature():
    """Тест создания данных с невалидной температурой"""
    timestamp = datetime.now()

    with pytest.raises(TypeError, match="Температура должна быть числом"):
        WeatherData("WD001", timestamp, "20.0", 60.0)

    with pytest.raises(TypeError, match="Температура должна быть числом"):
        WeatherData("WD001", timestamp, None, 60.0)


def test_weather_data_creation_invalid_humidity():
    """Тест создания данных с невалидной влажностью"""
    timestamp = datetime.now()

    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        WeatherData("WD001", timestamp, 20.0, -5.0)

    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        WeatherData("WD001", timestamp, 20.0, 150.0)

    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        WeatherData("WD001", timestamp, 20.0, "60.0")


def test_weather_data_creation_boundary_humidity():
    """Тест создания данных с граничными значениями влажности"""
    timestamp = datetime.now()

    # Граничные значения влажности
    data1 = WeatherData("WD001", timestamp, 20.0, 0.0)
    assert data1.humidity == 0.0

    data2 = WeatherData("WD002", timestamp, 20.0, 100.0)
    assert data2.humidity == 100.0


def test_weather_data_add_pressure_valid():
    """Тест добавления валидного давления"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    data.add_pressure(1013.25)
    assert data.pressure == 1013.25


def test_weather_data_add_pressure_invalid():
    """Тест добавления невалидного давления"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    with pytest.raises(ValueError, match="Давление должно быть положительным"):
        data.add_pressure(-100.0)

    # Проверка типа (не число)
    with pytest.raises(ValueError, match="Давление должно быть положительным"):
        data.add_pressure("1013.25")


def test_weather_data_add_pressure_update():
    """Тест обновления давления"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    data.add_pressure(1013.25)
    assert data.pressure == 1013.25

    data.add_pressure(1020.5)  # Обновление
    assert data.pressure == 1020.5


def test_weather_data_add_wind_data_valid():
    """Тест добавления валидных данных ветра"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    data.add_wind_data(5.5, 180)
    assert data.wind_speed == 5.5
    assert data.wind_direction == 180


def test_weather_data_add_wind_data_invalid_speed():
    """Тест добавления данных ветра с невалидной скоростью"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    with pytest.raises(ValueError, match="Скорость ветра должна быть неотрицательной"):
        data.add_wind_data(-5.0, 180)

    with pytest.raises(ValueError, match="Скорость ветра должна быть неотрицательной"):
        data.add_wind_data("5.5", 180)


def test_weather_data_add_wind_data_invalid_direction():
    """Тест добавления данных ветра с невалидным направлением"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    with pytest.raises(ValueError, match="Направление должно быть от 0 до 360"):
        data.add_wind_data(5.5, -10)

    with pytest.raises(ValueError, match="Направление должно быть от 0 до 360"):
        data.add_wind_data(5.5, 400)

    with pytest.raises(ValueError, match="Направление должно быть от 0 до 360"):
        data.add_wind_data(5.5, "180")


def test_weather_data_add_wind_data_boundary_direction():
    """Тест добавления данных ветра с граничными значениями направления"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    # Граничные значения направления
    data.add_wind_data(0.0, 0)
    assert data.wind_speed == 0.0
    assert data.wind_direction == 0

    data.add_wind_data(10.0, 360)
    assert data.wind_speed == 10.0
    assert data.wind_direction == 360


def test_weather_data_rainfall_visibility_assignment():
    """Тест присваивания осадков и видимости"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    # Прямое присваивание полей (методы не существуют)
    data.rainfall = 2.5
    data.visibility = 10000.0

    assert data.rainfall == 2.5
    assert data.visibility == 10000.0


def test_weather_data_validate_data_valid():
    """Тест валидации валидных данных"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)
    assert data.validate_data() == True


def test_weather_data_validate_data_basic():
    """Тест базовой валидации данных"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    # Проверка, что данные валидны после создания
    assert data.validate_data() == True
    assert data.temperature is not None
    assert data.humidity is not None


def test_weather_data_field_types():
    """Тест типов полей данных о погоде"""
    timestamp = datetime(2024, 1, 15, 12, 30)
    data = WeatherData("WD001", timestamp, 20.5, 65.0)

    data.add_pressure(1013.25)
    data.add_wind_data(5.5, 180)
    data.rainfall = 2.5  # Осадки
    data.visibility = 10000.0  # Видимость

    assert isinstance(data.data_id, str)
    assert isinstance(data.timestamp, datetime)
    assert isinstance(data.temperature, (int, float))
    assert isinstance(data.humidity, (int, float))
    assert data.pressure is None or isinstance(data.pressure, (int, float))
    assert data.wind_speed is None or isinstance(data.wind_speed, (int, float))
    assert data.wind_direction is None or isinstance(data.wind_direction, int)
    assert data.rainfall is None or isinstance(data.rainfall, (int, float))
    assert data.visibility is None or isinstance(data.visibility, (int, float))
    assert isinstance(data.data_quality, str)


def test_weather_data_data_integrity():
    """Тест целостности данных о погоде"""
    timestamp = datetime(2024, 1, 15, 12, 30)
    data = WeatherData("WD001", timestamp, 20.5, 65.0)

    # Изменяем поля
    data.add_pressure(1013.25)
    data.add_wind_data(5.5, 180)
    data.rainfall = 2.5  # Осадки
    data.visibility = 10000.0  # Видимость
    data.data_quality = "excellent"

    # Проверяем, что основные поля остались неизменными
    assert data.data_id == "WD001"
    assert data.timestamp == timestamp
    assert data.temperature == 20.5
    assert data.humidity == 65.0

    # Проверяем измененные поля
    assert data.pressure == 1013.25
    assert data.wind_speed == 5.5
    assert data.wind_direction == 180
    assert data.rainfall == 2.5
    assert data.visibility == 10000.0
    assert data.data_quality == "excellent"


def test_weather_data_extreme_values():
    """Тест экстремальных значений данных о погоде"""
    timestamp = datetime.now()

    # Экстремальные температуры
    data1 = WeatherData("WD001", timestamp, -50.0, 0.0)
    assert data1.temperature == -50.0

    data2 = WeatherData("WD002", timestamp, 60.0, 100.0)
    assert data2.temperature == 60.0

    # Экстремальные значения других параметров
    data2.add_pressure(1200.0)  # Высокое давление
    data2.add_wind_data(150.0, 270)  # Сильный ветер
    data2.rainfall = 500.0  # Сильный дождь (прямое присваивание)
    data2.visibility = 50000.0  # Отличная видимость (прямое присваивание)

    assert data2.pressure == 1200.0
    assert data2.wind_speed == 150.0
    assert data2.rainfall == 500.0
    assert data2.visibility == 50000.0


def test_weather_data_zero_values():
    """Тест нулевых значений данных о погоде"""
    timestamp = datetime.now()

    data = WeatherData("WD001", timestamp, 0.0, 0.0)
    assert data.temperature == 0.0
    assert data.humidity == 0.0

    data.add_pressure(0.001)  # Минимальное положительное давление
    data.add_wind_data(0.0, 0)  # Штиль
    data.rainfall = 0.0  # Без осадков
    data.visibility = 0.001  # Минимальная видимость

    assert data.pressure == 0.001
    assert data.wind_speed == 0.0
    assert data.rainfall == 0.0
    assert data.visibility == 0.001


def test_weather_data_workflow():
    """Тест полного жизненного цикла данных о погоде"""
    timestamp = datetime(2024, 1, 15, 12, 30)

    # Создание базовых данных
    data = WeatherData("WD001", timestamp, 15.5, 70.0)

    # Добавление дополнительных параметров
    data.add_pressure(1015.2)
    data.add_wind_data(3.2, 45)
    data.rainfall = 0.5
    data.visibility = 8000.0

    # Валидация
    assert data.validate_data() == True

    # Изменение качества данных
    data.data_quality = "verified"

    # Проверка всех полей
    assert data.data_id == "WD001"
    assert data.temperature == 15.5
    assert data.humidity == 70.0
    assert data.pressure == 1015.2
    assert data.wind_speed == 3.2
    assert data.wind_direction == 45
    assert data.rainfall == 0.5
    assert data.visibility == 8000.0
    assert data.data_quality == "verified"


def test_weather_data_data_quality():
    """Тест различных уровней качества данных"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)

    qualities = ["poor", "fair", "good", "excellent", "verified", "calibrated"]
    for quality in qualities:
        data.data_quality = quality
        assert data.data_quality == quality


def test_weather_data_complex_scenario():
    """Тест комплексного сценария сбора данных"""
    timestamp = datetime(2024, 1, 15, 12, 30)

    # Создание данных для летнего дня
    summer_data = WeatherData("SUMMER001", timestamp, 28.5, 45.0)
    summer_data.add_pressure(1012.8)
    summer_data.add_wind_data(2.1, 135)
    summer_data.rainfall = 0.0
    summer_data.visibility = 25000.0
    summer_data.data_quality = "good"

    # Создание данных для зимнего дня
    winter_data = WeatherData("WINTER001", timestamp, -15.2, 85.0)
    winter_data.add_pressure(1025.5)
    winter_data.add_wind_data(8.5, 315)
    winter_data.rainfall = 0.0
    winter_data.visibility = 5000.0
    winter_data.data_quality = "good"

    # Проверка обеих записей
    assert summer_data.validate_data() == True
    assert winter_data.validate_data() == True

    # Проверка характеристик сезонов
    assert summer_data.temperature > winter_data.temperature
    assert summer_data.humidity < winter_data.humidity
    assert summer_data.pressure < winter_data.pressure
    assert summer_data.visibility > winter_data.visibility


def test_weather_data_invalid_temperature():
    """Тест невалидной температуры"""
    timestamp = datetime.now()
    data = WeatherData("WD001", timestamp, 20.0, 60.0)
    data.temperature = 150.0
    with pytest.raises(DataValidationException):
        data.validate_data()


