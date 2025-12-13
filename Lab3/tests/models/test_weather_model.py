"""Тесты для WeatherModel"""
import pytest
import sys
import os
from unittest.mock import Mock
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from models.weather_model import WeatherModel
from exceptions.weather_exceptions import ModelException


def test_weather_model_creation_valid():
    """Тест создания модели погоды с валидными данными"""
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")
    assert model.model_id == "WM001"
    assert model.model_name == "GFS"
    assert model.model_type == "Numerical"
    assert model.version == "v2.0"
    assert model.accuracy is None
    assert model.is_active == True
    assert model.training_data_size == 0
    assert model.get_forecasts() == []


def test_weather_model_creation_invalid_id():
    """Тест создания модели с невалидным ID"""
    with pytest.raises(ValueError, match="ID модели должен быть непустой строкой"):
        WeatherModel("", "GFS", "Numerical", "v2.0")

    with pytest.raises(ValueError, match="ID модели должен быть непустой строкой"):
        WeatherModel(None, "GFS", "Numerical", "v2.0")


def test_weather_model_creation_invalid_name():
    """Тест создания модели с невалидным названием"""
    with pytest.raises(ValueError, match="Название модели должно быть непустой строкой"):
        WeatherModel("WM001", "", "Numerical", "v2.0")

    with pytest.raises(ValueError, match="Название модели должно быть непустой строкой"):
        WeatherModel("WM001", None, "Numerical", "v2.0")


def test_weather_model_creation_invalid_type():
    """Тест создания модели с невалидным типом"""
    with pytest.raises(TypeError, match="Тип модели должен быть строкой"):
        WeatherModel("WM001", "GFS", 123, "v2.0")


def test_weather_model_creation_invalid_version():
    """Тест создания модели с невалидной версией"""
    with pytest.raises(TypeError, match="Версия должна быть строкой"):
        WeatherModel("WM001", "GFS", "Numerical", 2.0)


def test_weather_model_creation_empty_strings():
    """Тест создания модели с пустыми строками"""
    # Пустые строки для model_type и version допустимы
    model = WeatherModel("WM001", "GFS", "", "")
    assert model.model_type == ""
    assert model.version == ""


def test_weather_model_generate_forecast():
    """Тест генерации прогноза"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    forecast1 = Mock()
    forecast2 = Mock()

    model.generate_forecast(forecast1)
    assert forecast1 in model.get_forecasts()
    assert len(model.get_forecasts()) == 1

    model.generate_forecast(forecast2)
    assert forecast2 in model.get_forecasts()
    assert len(model.get_forecasts()) == 2


def test_weather_model_generate_forecast_duplicate():
    """Тест генерации дублированного прогноза"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    forecast = Mock()

    model.generate_forecast(forecast)
    model.generate_forecast(forecast)  # Дубликат

    forecasts = model.get_forecasts()
    assert forecasts.count(forecast) == 1  # Должен быть только один экземпляр
    assert len(forecasts) == 1


def test_weather_model_get_forecasts():
    """Тест получения списка прогнозов"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    forecast1 = Mock()
    forecast2 = Mock()

    model.generate_forecast(forecast1)
    model.generate_forecast(forecast2)

    forecasts = model.get_forecasts()
    assert forecast1 in forecasts
    assert forecast2 in forecasts
    assert len(forecasts) == 2

    # Проверяем, что возвращается копия
    forecasts.append(Mock())
    assert len(model.get_forecasts()) == 2


def test_weather_model_get_forecasts_empty():
    """Тест получения пустого списка прогнозов"""
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")
    forecasts = model.get_forecasts()
    assert forecasts == []
    assert len(forecasts) == 0


def test_weather_model_set_accuracy_valid():
    """Тест установки валидной точности"""
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    model.set_accuracy(85.5)
    assert model.accuracy == 85.5

    model.set_accuracy(0.0)
    assert model.accuracy == 0.0

    model.set_accuracy(100.0)
    assert model.accuracy == 100.0


def test_weather_model_set_accuracy_invalid():
    """Тест установки невалидной точности"""
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    with pytest.raises(ModelException, match="Точность должна быть от 0 до 100"):
        model.set_accuracy(-5.0)

    with pytest.raises(ModelException, match="Точность должна быть от 0 до 100"):
        model.set_accuracy(150.0)

    with pytest.raises(ModelException, match="Точность должна быть от 0 до 100"):
        model.set_accuracy("85")


def test_weather_model_set_accuracy_boundary_values():
    """Тест установки граничных значений точности"""
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    model.set_accuracy(0.0)
    assert model.accuracy == 0.0

    model.set_accuracy(100.0)
    assert model.accuracy == 100.0


def test_weather_model_uses_data_valid():
    """Тест использования валидных данных погоды"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    weather_data = Mock()
    weather_data.validate_data = Mock()

    initial_size = model.training_data_size
    model.uses_data(weather_data)

    weather_data.validate_data.assert_called_once()
    assert model.training_data_size == initial_size + 1


def test_weather_model_uses_data_invalid():
    """Тест использования невалидных данных погоды"""
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    with pytest.raises(ValueError, match="Данные о погоде не могут быть None"):
        model.uses_data(None)


def test_weather_model_uses_data_multiple():
    """Тест использования нескольких наборов данных"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    data1 = Mock()
    data1.validate_data = Mock()

    data2 = Mock()
    data2.validate_data = Mock()

    data3 = Mock()
    data3.validate_data = Mock()

    model.uses_data(data1)
    assert model.training_data_size == 1

    model.uses_data(data2)
    assert model.training_data_size == 2

    model.uses_data(data3)
    assert model.training_data_size == 3


def test_weather_model_generates_forecast():
    """Тест генерации прогноза через метод generates_forecast"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    forecast = Mock()

    model.generates_forecast(forecast)
    assert forecast in model.get_forecasts()
    assert len(model.get_forecasts()) == 1


def test_weather_model_generates_forecast_invalid():
    """Тест генерации невалидного прогноза"""
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    with pytest.raises(ValueError, match="Прогноз не может быть None"):
        model.generates_forecast(None)


def test_weather_model_used_by_meteorologist_valid():
    """Тест использования модели валидным метеорологом"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    meteorologist = Mock()
    meteorologist.is_available = True

    # Метод не должен выбрасывать исключение
    model.used_by_meteorologist(meteorologist)


def test_weather_model_used_by_meteorologist_invalid():
    """Тест использования модели невалидным метеорологом"""
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    with pytest.raises(ValueError, match="Метеоролог не может быть None"):
        model.used_by_meteorologist(None)


def test_weather_model_used_by_meteorologist_unavailable():
    """Тест использования модели недоступным метеорологом"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    meteorologist = Mock()
    meteorologist.is_available = False

    with pytest.raises(ValueError, match="Метеоролог недоступен"):
        model.used_by_meteorologist(meteorologist)


def test_weather_model_forecasts_property():
    """Тест свойства forecasts"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    forecast = Mock()
    model.generate_forecast(forecast)

    # Проверяем, что forecasts - это свойство, возвращающее список
    assert hasattr(model, 'forecasts')
    assert isinstance(model.forecasts, list)
    assert forecast in model.forecasts


def test_weather_model_field_types():
    """Тест типов полей модели погоды"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")
    model.set_accuracy(85.5)

    forecast = Mock()
    model.generate_forecast(forecast)

    assert isinstance(model.model_id, str)
    assert isinstance(model.model_name, str)
    assert isinstance(model.model_type, str)
    assert isinstance(model.version, str)
    assert isinstance(model.get_forecasts(), list)
    assert model.accuracy is None or isinstance(model.accuracy, (int, float))
    assert isinstance(model.is_active, bool)
    assert isinstance(model.training_data_size, int)


def test_weather_model_data_integrity():
    """Тест целостности данных модели погоды"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")

    # Изменяем поля через различные операции
    model.set_accuracy(90.0)

    forecast1 = Mock()
    forecast2 = Mock()
    model.generate_forecast(forecast1)
    model.generate_forecast(forecast2)

    data = Mock()
    data.validate_data = Mock()
    model.uses_data(data)

    # Проверяем, что основные поля остались неизменными
    assert model.model_id == "WM001"
    assert model.model_name == "GFS"
    assert model.model_type == "Numerical"
    assert model.version == "v2.0"
    assert model.is_active == True

    # Проверяем измененные поля
    assert model.accuracy == 90.0
    assert len(model.get_forecasts()) == 2
    assert model.training_data_size == 1


def test_weather_model_boundary_values():
    """Тест граничных значений для модели погоды"""
    # Пустые строки для типов
    model1 = WeatherModel("WM001", "Test", "", "")
    assert model1.model_type == ""
    assert model1.version == ""

    # Нулевая точность
    model2 = WeatherModel("WM002", "Test", "Type", "v1.0")
    model2.set_accuracy(0.0)
    assert model2.accuracy == 0.0

    # Максимальная точность
    model2.set_accuracy(100.0)
    assert model2.accuracy == 100.0

    # Большое количество прогнозов
    model3 = WeatherModel("WM003", "Test", "Type", "v1.0")
    forecasts = [Mock() for _ in range(10)]
    for forecast in forecasts:
        model3.generate_forecast(forecast)

    assert len(model3.get_forecasts()) == 10

    # Большой размер обучающих данных
    data_list = [Mock() for _ in range(100)]
    for data in data_list:
        data.validate_data = Mock()

    for data in data_list:
        model3.uses_data(data)

    assert model3.training_data_size == 100


def test_weather_model_workflow():
    """Тест полного жизненного цикла модели погоды"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "Advanced Model", "AI", "v3.0")

    # Начальное состояние
    assert model.accuracy is None
    assert model.training_data_size == 0
    assert len(model.get_forecasts()) == 0
    assert model.is_active == True

    # Обучение модели
    for i in range(5):
        data = Mock()
        data.validate_data = Mock()
        model.uses_data(data)

    assert model.training_data_size == 5

    # Установка точности
    model.set_accuracy(92.5)
    assert model.accuracy == 92.5

    # Генерация прогнозов
    forecasts = []
    for i in range(3):
        forecast = Mock()
        model.generates_forecast(forecast)
        forecasts.append(forecast)

    assert len(model.get_forecasts()) == 3

    # Использование метеорологом
    meteorologist = Mock()
    meteorologist.is_available = True
    model.used_by_meteorologist(meteorologist)

    # Деактивация модели
    model.is_active = False
    # Модель может продолжать генерировать прогнозы, даже если неактивна

    # Финальное состояние
    assert model.training_data_size == 5
    assert model.accuracy == 92.5
    assert len(model.get_forecasts()) == 3


def test_weather_model_edge_cases():
    """Тест крайних случаев для модели погоды"""
    from unittest.mock import Mock
    model = WeatherModel("WM001", "Test", "Type", "v1.0")

    # Тип int вместо float для точности
    model.set_accuracy(85)  # int
    assert model.accuracy == 85.0  # должно работать

    # Добавление одного и того же прогноза несколько раз
    forecast = Mock()
    for _ in range(5):
        model.generate_forecast(forecast)

    assert len(model.get_forecasts()) == 1

    # Использование данных с исключением в validate_data
    data = Mock()
    data.validate_data = Mock(side_effect=Exception("Validation failed"))

    with pytest.raises(Exception, match="Validation failed"):
        model.uses_data(data)

    # Но размер все равно увеличился
    assert model.training_data_size == 1


