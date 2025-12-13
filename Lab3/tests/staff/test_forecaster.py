"""Тесты для Forecaster"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from staff.forecaster import Forecaster


def test_forecaster_creation_valid():
    """Тест создания прогнозиста с валидными данными"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)
    assert forecaster.employee_id == "F001"
    assert forecaster.name == "Jane Doe"
    assert forecaster.forecast_type == "Short-term"
    assert forecaster.accuracy_rate == 85.5
    assert forecaster.forecast_count == 0
    assert forecaster.shift == "day"
    assert forecaster.get_forecasts() == []


def test_forecaster_creation_invalid_employee_id():
    """Тест создания прогнозиста с невалидным ID сотрудника"""
    with pytest.raises(ValueError, match="ID сотрудника должен быть непустой строкой"):
        Forecaster("", "Jane Doe", "Short-term", 85.5)

    with pytest.raises(ValueError, match="ID сотрудника должен быть непустой строкой"):
        Forecaster(None, "Jane Doe", "Short-term", 85.5)


def test_forecaster_creation_invalid_name():
    """Тест создания прогнозиста с невалидным именем"""
    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Forecaster("F001", "", "Short-term", 85.5)

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Forecaster("F001", None, "Short-term", 85.5)


def test_forecaster_creation_invalid_forecast_type():
    """Тест создания прогнозиста с невалидным типом прогноза"""
    with pytest.raises(TypeError, match="Тип прогноза должен быть строкой"):
        Forecaster("F001", "Jane Doe", 123, 85.5)


def test_forecaster_creation_invalid_accuracy():
    """Тест создания прогнозиста с невалидной точностью"""
    with pytest.raises(ValueError, match="Точность должна быть от 0 до 100"):
        Forecaster("F001", "Jane Doe", "Short-term", -5.0)

    with pytest.raises(ValueError, match="Точность должна быть от 0 до 100"):
        Forecaster("F001", "Jane Doe", "Short-term", 150.0)

    with pytest.raises(ValueError, match="Точность должна быть от 0 до 100"):
        Forecaster("F001", "Jane Doe", "Short-term", "85.5")


def test_forecaster_add_forecast_valid():
    """Тест добавления валидного прогноза"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)
    mock_forecast = type('MockForecast', (), {'forecast_id': 'FC001'})()
    forecaster.add_forecast(mock_forecast)
    assert len(forecaster.get_forecasts()) == 1
    assert forecaster.forecast_count == 1


def test_forecaster_add_forecast_invalid():
    """Тест добавления невалидного прогноза"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)

    with pytest.raises(ValueError, match="Прогноз не может быть None"):
        forecaster.add_forecast(None)


def test_forecaster_get_forecasts():
    """Тест получения списка прогнозов"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)
    mock_forecast1 = type('MockForecast', (), {'forecast_id': 'FC001'})()
    mock_forecast2 = type('MockForecast', (), {'forecast_id': 'FC002'})()

    forecaster.add_forecast(mock_forecast1)
    forecaster.add_forecast(mock_forecast2)

    forecasts = forecaster.get_forecasts()
    assert len(forecasts) == 2
    assert forecasts[0].forecast_id == 'FC001'
    assert forecasts[1].forecast_id == 'FC002'
    assert forecaster.forecast_count == 2


def test_forecaster_update_accuracy_valid():
    """Тест обновления валидной точности"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)
    forecaster.update_accuracy(92.3)
    assert forecaster.accuracy_rate == 92.3


def test_forecaster_update_accuracy_invalid():
    """Тест обновления невалидной точности"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)

    with pytest.raises(ValueError, match="Точность должна быть от 0 до 100"):
        forecaster.update_accuracy(-10.0)

    with pytest.raises(ValueError, match="Точность должна быть от 0 до 100"):
        forecaster.update_accuracy(110.0)


def test_forecaster_set_shift_valid():
    """Тест установки валидной смены"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)
    forecaster.set_shift("night")
    assert forecaster.shift == "night"


def test_forecaster_set_shift_invalid():
    """Тест установки невалидной смены"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)

    with pytest.raises(TypeError, match="Смена должна быть строкой"):
        forecaster.set_shift(123)


def test_forecaster_field_types():
    """Тест типов полей прогнозиста"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)
    mock_forecast = type('MockForecast', (), {'forecast_id': 'FC001'})()
    forecaster.add_forecast(mock_forecast)
    forecaster.update_accuracy(90.0)
    forecaster.set_shift("night")

    assert isinstance(forecaster.employee_id, str)
    assert isinstance(forecaster.name, str)
    assert isinstance(forecaster.forecast_type, str)
    assert isinstance(forecaster.accuracy_rate, float)
    assert isinstance(forecaster.forecast_count, int)
    assert isinstance(forecaster.shift, str)
    assert isinstance(forecaster.get_forecasts(), list)


def test_forecaster_data_integrity():
    """Тест целостности данных прогнозиста"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)

    # Изменяем поля
    mock_forecast1 = type('MockForecast', (), {'forecast_id': 'FC001'})()
    mock_forecast2 = type('MockForecast', (), {'forecast_id': 'FC002'})()
    forecaster.add_forecast(mock_forecast1)
    forecaster.add_forecast(mock_forecast2)
    forecaster.update_accuracy(90.0)
    forecaster.set_shift("night")

    # Проверяем, что основные поля остались неизменными
    assert forecaster.employee_id == "F001"
    assert forecaster.name == "Jane Doe"
    assert forecaster.forecast_type == "Short-term"

    # Проверяем измененные поля
    assert len(forecaster.get_forecasts()) == 2
    assert forecaster.accuracy_rate == 90.0
    assert forecaster.forecast_count == 2
    assert forecaster.shift == "night"


def test_forecaster_forecast_types():
    """Тест различных типов прогнозов"""
    forecast_types = [
        "Short-term",
        "Medium-term",
        "Long-term",
        "Nowcast",
        "Extended",
        "Seasonal"
    ]

    for f_type in forecast_types:
        forecaster = Forecaster("TEST", "Test Forecaster", f_type, 85.0)
        assert forecaster.forecast_type == f_type


def test_forecaster_accuracy_ranges():
    """Тест различных диапазонов точности"""
    accuracy_values = [0.0, 25.5, 50.0, 75.8, 90.2, 95.7, 99.9, 100.0]

    for accuracy in accuracy_values:
        forecaster = Forecaster("TEST", "Test Forecaster", "Short-term", accuracy)
        assert forecaster.accuracy_rate == accuracy


def test_forecaster_shift_types():
    """Тест различных типов смен"""
    shifts = ["day", "night", "morning", "evening", "weekend", "holiday"]

    for shift in shifts:
        forecaster = Forecaster("TEST", "Test Forecaster", "Short-term", 85.0)
        forecaster.set_shift(shift)
        assert forecaster.shift == shift


def test_forecaster_multiple_forecasts():
    """Тест работы с множественными прогнозами"""
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)

    # Добавляем несколько прогнозов
    for i in range(10):
        mock_forecast = type('MockForecast', (), {'forecast_id': f'FC{i+1:03d}'})()
        forecaster.add_forecast(mock_forecast)

    assert len(forecaster.get_forecasts()) == 10
    assert forecaster.forecast_count == 10


def test_forecaster_workflow():
    """Тест полного жизненного цикла прогнозиста"""
    # Создание прогнозиста
    forecaster = Forecaster("FORECASTER001", "Mike Johnson", "Medium-term", 88.5)

    # Добавление прогнозов
    mock_forecast1 = type('MockForecast', (), {'forecast_id': 'MT001'})()
    mock_forecast2 = type('MockForecast', (), {'forecast_id': 'MT002'})()
    forecaster.add_forecast(mock_forecast1)
    forecaster.add_forecast(mock_forecast2)

    # Обновление точности
    forecaster.update_accuracy(91.2)

    # Установка смены
    forecaster.set_shift("night")

    # Проверки
    assert forecaster.employee_id == "FORECASTER001"
    assert forecaster.name == "Mike Johnson"
    assert forecaster.forecast_type == "Medium-term"
    assert forecaster.accuracy_rate == 91.2
    assert len(forecaster.get_forecasts()) == 2
    assert forecaster.forecast_count == 2
    assert forecaster.shift == "night"


def test_forecaster_performance_metrics():
    """Тест метрик производительности прогнозиста"""
    forecaster = Forecaster("PERF001", "Performance Forecaster", "Short-term", 80.0)

    # Симуляция работы за период
    initial_accuracy = forecaster.accuracy_rate
    initial_count = forecaster.forecast_count

    # Добавляем прогнозы
    for i in range(50):
        mock_forecast = type('MockForecast', (), {'forecast_id': f'PERF{i+1:03d}'})()
        forecaster.add_forecast(mock_forecast)

    # Обновляем точность после анализа
    forecaster.update_accuracy(87.3)

    # Проверки
    assert len(forecaster.get_forecasts()) == 50
    assert forecaster.forecast_count == 50
    assert forecaster.accuracy_rate == 87.3


def test_forecaster_error_handling():
    """Тест обработки ошибок"""
    forecaster = Forecaster("TEST", "Test Forecaster", "Test", 85.0)

    # Попытка добавления None прогноза
    with pytest.raises(ValueError):
        forecaster.add_forecast(None)

    # Попытка обновления неправильной точности
    with pytest.raises(ValueError):
        forecaster.update_accuracy(150.0)

    # Попытка установки неправильной смены
    with pytest.raises(TypeError):
        forecaster.set_shift(12345)


def test_forecaster_boundary_values():
    """Тест граничных значений"""
    # Минимальная и максимальная точность
    forecaster1 = Forecaster("MIN", "Min Accuracy", "Test", 0.0)
    assert forecaster1.accuracy_rate == 0.0

    forecaster2 = Forecaster("MAX", "Max Accuracy", "Test", 100.0)
    assert forecaster2.accuracy_rate == 100.0

    # Обновление до граничных значений
    forecaster1.update_accuracy(100.0)
    assert forecaster1.accuracy_rate == 100.0

    forecaster2.update_accuracy(0.0)
    assert forecaster2.accuracy_rate == 0.0


def test_forecaster_state_consistency():
    """Тест согласованности состояний"""
    forecaster = Forecaster("STATE", "State Forecaster", "Short-term", 85.0)

    # Начальное состояние
    assert len(forecaster.get_forecasts()) == 0
    assert forecaster.forecast_count == 0
    assert forecaster.accuracy_rate == 85.0
    assert forecaster.shift == "day"

    # После добавления прогноза
    mock_forecast = type('MockForecast', (), {'forecast_id': 'STATE001'})()
    forecaster.add_forecast(mock_forecast)
    assert len(forecaster.get_forecasts()) == 1
    assert forecaster.forecast_count == 1

    # После обновления точности
    forecaster.update_accuracy(90.0)
    assert forecaster.accuracy_rate == 90.0

    # После изменения смены
    forecaster.set_shift("night")
    assert forecaster.shift == "night"


