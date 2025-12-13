"""Тесты для Forecast"""
import pytest
import sys
import os
from datetime import date, datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from forecasts.forecast import Forecast
from exceptions.weather_exceptions import InvalidForecastDataException, ForecastNotFoundException


def test_forecast_creation_valid():
    """Тест создания прогноза с валидными данными"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.5)

    assert forecast.forecast_id == "F001"
    assert forecast.location_name == "Moscow"
    assert forecast.forecast_date == forecast_date
    assert forecast.temperature == 15.5
    assert forecast.humidity is None
    assert forecast.precipitation_probability is None
    assert forecast.wind_speed is None
    assert forecast.forecast_type == "general"
    assert forecast.accuracy_score is None
    assert isinstance(forecast.created_at, datetime)


def test_forecast_creation_invalid_id():
    """Тест создания прогноза с невалидным ID"""
    forecast_date = date(2024, 1, 15)

    with pytest.raises(ValueError, match="ID прогноза должен быть непустой строкой"):
        Forecast("", "Moscow", forecast_date, 15.0)

    with pytest.raises(ValueError, match="ID прогноза должен быть непустой строкой"):
        Forecast(None, "Moscow", forecast_date, 15.0)


def test_forecast_creation_invalid_location():
    """Тест создания прогноза с невалидной локацией"""
    forecast_date = date(2024, 1, 15)

    with pytest.raises(ValueError, match="Название локации должно быть непустой строкой"):
        Forecast("F001", "", forecast_date, 15.0)

    with pytest.raises(ValueError, match="Название локации должно быть непустой строкой"):
        Forecast("F001", None, forecast_date, 15.0)


def test_forecast_creation_invalid_date():
    """Тест создания прогноза с невалидной датой"""
    with pytest.raises(TypeError, match="Дата прогноза должна быть date"):
        Forecast("F001", "Moscow", "2024-01-15", 15.0)

    with pytest.raises(TypeError, match="Дата прогноза должна быть date"):
        Forecast("F001", "Moscow", None, 15.0)


def test_forecast_creation_invalid_temperature():
    """Тест создания прогноза с невалидной температурой"""
    forecast_date = date(2024, 1, 15)

    with pytest.raises(TypeError, match="Температура должна быть числом"):
        Forecast("F001", "Moscow", forecast_date, "15.0")

    with pytest.raises(TypeError, match="Температура должна быть числом"):
        Forecast("F001", "Moscow", forecast_date, None)


def test_forecast_add_humidity_valid():
    """Тест добавления валидной влажности"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    forecast.add_humidity(65.0)
    assert forecast.humidity == 65.0


def test_forecast_add_humidity_invalid():
    """Тест добавления невалидной влажности"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        forecast.add_humidity(-5.0)

    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        forecast.add_humidity(150.0)

    with pytest.raises(ValueError, match="Влажность должна быть от 0 до 100"):
        forecast.add_humidity("65.0")


def test_forecast_add_humidity_boundary():
    """Тест добавления влажности с граничными значениями"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    forecast.add_humidity(0.0)
    assert forecast.humidity == 0.0

    forecast.add_humidity(100.0)
    assert forecast.humidity == 100.0


def test_forecast_set_precipitation_probability_valid():
    """Тест установки валидной вероятности осадков"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    forecast.set_precipitation_probability(75.0)
    assert forecast.precipitation_probability == 75.0


def test_forecast_set_precipitation_probability_invalid():
    """Тест установки невалидной вероятности осадков"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    with pytest.raises(InvalidForecastDataException):
        forecast.set_precipitation_probability(-5.0)

    with pytest.raises(InvalidForecastDataException):
        forecast.set_precipitation_probability(150.0)

    with pytest.raises(InvalidForecastDataException):
        forecast.set_precipitation_probability("75.0")


def test_forecast_set_precipitation_probability_boundary():
    """Тест установки вероятности осадков с граничными значениями"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    forecast.set_precipitation_probability(0.0)
    assert forecast.precipitation_probability == 0.0

    forecast.set_precipitation_probability(100.0)
    assert forecast.precipitation_probability == 100.0


def test_forecast_add_wind_forecast_valid():
    """Тест добавления валидного прогноза ветра"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    forecast.add_wind_forecast(5.5)
    assert forecast.wind_speed == 5.5


def test_forecast_add_wind_forecast_invalid():
    """Тест добавления невалидного прогноза ветра"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    with pytest.raises(ValueError, match="Скорость ветра должна быть неотрицательной"):
        forecast.add_wind_forecast(-2.0)

    with pytest.raises(ValueError, match="Скорость ветра должна быть неотрицательной"):
        forecast.add_wind_forecast("5.5")


def test_forecast_set_forecast_type():
    """Тест установки типа прогноза"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    types = ["general", "detailed", "hourly", "daily", "weekly", "monthly"]
    for forecast_type in types:
        forecast.forecast_type = forecast_type
        assert forecast.forecast_type == forecast_type


def test_forecast_set_accuracy_score():
    """Тест установки оценки точности"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    forecast.set_accuracy(85.5)
    assert forecast.accuracy_score == 85.5

    forecast.accuracy_score = None
    assert forecast.accuracy_score is None


def test_forecast_basic_validation():
    """Тест базовой валидации прогноза"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    # Проверяем, что основные поля установлены корректно
    assert forecast.forecast_id == "F001"
    assert forecast.location_name == "Moscow"
    assert forecast.forecast_date == forecast_date
    assert forecast.temperature == 15.0


def test_forecast_missing_temperature_check():
    """Тест проверки прогноза без температуры"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    # Температура не может быть None из-за валидации в __init__
    # Но можем проверить, что она остается корректной
    assert forecast.temperature is not None
    assert isinstance(forecast.temperature, (int, float))


def test_forecast_missing_date_check():
    """Тест проверки прогноза без даты"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    # Дата не может быть None из-за валидации в __init__
    # Но можем проверить, что она остается корректной
    assert forecast.forecast_date is not None
    assert isinstance(forecast.forecast_date, date)


def test_forecast_field_types():
    """Тест типов полей прогноза"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.5)

    forecast.add_humidity(65.0)
    forecast.set_precipitation_probability(75.0)
    forecast.add_wind_forecast(5.5)
    forecast.set_accuracy(85.0)

    assert isinstance(forecast.forecast_id, str)
    assert isinstance(forecast.location_name, str)
    assert isinstance(forecast.forecast_date, date)
    assert isinstance(forecast.temperature, (int, float))
    assert forecast.humidity is None or isinstance(forecast.humidity, (int, float))
    assert forecast.precipitation_probability is None or isinstance(forecast.precipitation_probability, (int, float))
    assert forecast.wind_speed is None or isinstance(forecast.wind_speed, (int, float))
    assert isinstance(forecast.forecast_type, str)
    assert forecast.accuracy_score is None or isinstance(forecast.accuracy_score, (int, float))
    assert isinstance(forecast.created_at, datetime)


def test_forecast_data_integrity():
    """Тест целостности данных прогноза"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.5)

    # Изменяем поля
    forecast.add_humidity(65.0)
    forecast.set_precipitation_probability(75.0)
    forecast.add_wind_forecast(5.5)
    forecast.forecast_type = "detailed"
    forecast.accuracy_score = 85.0

    # Проверяем, что основные поля остались неизменными
    assert forecast.forecast_id == "F001"
    assert forecast.location_name == "Moscow"
    assert forecast.forecast_date == forecast_date
    assert forecast.temperature == 15.5

    # Проверяем измененные поля
    assert forecast.humidity == 65.0
    assert forecast.precipitation_probability == 75.0
    assert forecast.wind_speed == 5.5
    assert forecast.forecast_type == "detailed"
    assert forecast.accuracy_score == 85.0


def test_forecast_extreme_values():
    """Тест экстремальных значений прогноза"""
    forecast_date = date(2024, 1, 15)

    # Экстремальные температуры
    forecast1 = Forecast("F001", "Antarctica", forecast_date, -80.0)
    assert forecast1.temperature == -80.0

    forecast2 = Forecast("F002", "Desert", forecast_date, 55.0)
    assert forecast2.temperature == 55.0

    # Экстремальные значения других параметров
    forecast2.add_humidity(0.0)  # Сухой воздух
    forecast2.set_precipitation_probability(0.0)  # Без осадков
    forecast2.add_wind_forecast(200.0)  # Ураган
    forecast2.accuracy_score = 99.9

    assert forecast2.humidity == 0.0
    assert forecast2.precipitation_probability == 0.0
    assert forecast2.wind_speed == 200.0
    assert forecast2.accuracy_score == 99.9


def test_forecast_workflow():
    """Тест полного жизненного цикла прогноза"""
    forecast_date = date(2024, 1, 20)

    # Создание базового прогноза
    forecast = Forecast("F001", "Moscow", forecast_date, 18.0)

    # Добавление детальной информации
    forecast.add_humidity(72.0)
    forecast.set_precipitation_probability(30.0)
    forecast.add_wind_forecast(3.8)
    forecast.forecast_type = "detailed"
    forecast.accuracy_score = 88.5

    # Базовая проверка
    assert forecast.forecast_id == "F001"

    # Проверка всех полей
    assert forecast.forecast_id == "F001"
    assert forecast.location_name == "Moscow"
    assert forecast.temperature == 18.0
    assert forecast.humidity == 72.0
    assert forecast.precipitation_probability == 30.0
    assert forecast.wind_speed == 3.8
    assert forecast.forecast_type == "detailed"
    assert forecast.accuracy_score == 88.5


def test_forecast_multiple_updates():
    """Тест множественных обновлений прогноза"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    # Множественные обновления параметров
    humidities = [60.0, 65.0, 70.0, 75.0]
    for humidity in humidities:
        forecast.add_humidity(humidity)

    probabilities = [20.0, 40.0, 60.0]
    for prob in probabilities:
        forecast.set_precipitation_probability(prob)

        wind_speeds = [2.0, 4.0, 6.0, 8.0]
        for speed in wind_speeds:
            forecast.add_wind_forecast(speed)

    # Проверяем последние значения
    assert forecast.humidity == humidities[-1]
    assert forecast.precipitation_probability == probabilities[-1]
    assert forecast.wind_speed == wind_speeds[-1]


def test_forecast_different_types():
    """Тест различных типов прогнозов"""
    forecast_date = date(2024, 1, 15)

    types = ["general", "detailed", "hourly", "daily", "weekly", "monthly", "seasonal"]
    for forecast_type in types:
        forecast = Forecast(f"F{types.index(forecast_type)}", "Moscow", forecast_date, 20.0)
        forecast.forecast_type = forecast_type
        assert forecast.forecast_type == forecast_type


def test_forecast_accuracy_range():
    """Тест диапазона оценки точности"""
    forecast_date = date(2024, 1, 15)
    forecast = Forecast("F001", "Moscow", forecast_date, 15.0)

    accuracies = [0.0, 25.5, 50.0, 75.8, 100.0]
    for accuracy in accuracies:
        forecast.accuracy_score = accuracy
        assert forecast.accuracy_score == accuracy


def test_forecast_date_boundary():
    """Тест граничных дат прогноза"""
    # Прошлые даты
    past_date = date(2020, 1, 1)
    forecast1 = Forecast("F001", "Moscow", past_date, 15.0)
    assert forecast1.forecast_date == past_date

    # Будущие даты
    future_date = date(2030, 12, 31)
    forecast2 = Forecast("F002", "Moscow", future_date, 15.0)
    assert forecast2.forecast_date == future_date

    # Сегодняшняя дата
    today = date.today()
    forecast3 = Forecast("F003", "Moscow", today, 15.0)
    assert forecast3.forecast_date == today


