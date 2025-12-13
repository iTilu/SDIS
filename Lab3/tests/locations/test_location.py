"""Тесты для Location"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from locations.location import Location


def test_location_init():
    loc = Location("L001", "Moscow", "Russia", "Central")
    assert loc.location_id == "L001"
    assert loc.country == "Russia"


def test_location_creation_valid():
    """Тест создания локации с валидными данными"""
    location = Location("LOC001", "Moscow", "Russia", "Central")
    assert location.location_id == "LOC001"
    assert location.name == "Moscow"
    assert location.country == "Russia"
    assert location.region == "Central"
    assert location.timezone is None
    assert location.population is None
    assert location.area_km2 is None


def test_location_creation_invalid_location_id():
    """Тест создания локации с невалидным ID"""
    with pytest.raises(ValueError, match="ID локации должен быть непустой строкой"):
        Location("", "Moscow", "Russia", "Central")

    with pytest.raises(ValueError, match="ID локации должен быть непустой строкой"):
        Location(None, "Moscow", "Russia", "Central")

    with pytest.raises(ValueError, match="ID локации должен быть непустой строкой"):
        Location(123, "Moscow", "Russia", "Central")


def test_location_creation_invalid_name():
    """Тест создания локации с невалидным названием"""
    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        Location("LOC001", "", "Russia", "Central")

    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        Location("LOC001", None, "Russia", "Central")


def test_location_creation_invalid_country():
    """Тест создания локации с невалидной страной"""
    with pytest.raises(TypeError, match="Страна должна быть строкой"):
        Location("LOC001", "Moscow", 123, "Central")

    with pytest.raises(TypeError, match="Страна должна быть строкой"):
        Location("LOC001", "Moscow", None, "Central")


def test_location_creation_invalid_region():
    """Тест создания локации с невалидным регионом"""
    with pytest.raises(TypeError, match="Регион должен быть строкой"):
        Location("LOC001", "Moscow", "Russia", 123)

    with pytest.raises(TypeError, match="Регион должен быть строкой"):
        Location("LOC001", "Moscow", "Russia", None)


def test_set_timezone_valid():
    """Тест установки валидного часового пояса"""
    location = Location("LOC001", "Moscow", "Russia", "Central")
    location.set_timezone("Europe/Moscow")
    assert location.timezone == "Europe/Moscow"


def test_set_timezone_invalid():
    """Тест установки невалидного часового пояса"""
    location = Location("LOC001", "Moscow", "Russia", "Central")

    with pytest.raises(TypeError, match="Часовой пояс должен быть строкой"):
        location.set_timezone(123)

    with pytest.raises(TypeError, match="Часовой пояс должен быть строкой"):
        location.set_timezone(None)


def test_set_population_valid():
    """Тест установки валидного населения"""
    location = Location("LOC001", "Moscow", "Russia", "Central")
    location.set_population(12655050)
    assert location.population == 12655050


def test_set_population_invalid():
    """Тест установки невалидного населения"""
    location = Location("LOC001", "Moscow", "Russia", "Central")

    with pytest.raises(ValueError, match="Население должно быть неотрицательным"):
        location.set_population(-100)

    with pytest.raises(ValueError, match="Население должно быть неотрицательным"):
        location.set_population("12655050")

    with pytest.raises(ValueError, match="Население должно быть неотрицательным"):
        location.set_population(-1)


def test_set_population_zero():
    """Тест установки нулевого населения"""
    location = Location("LOC001", "Moscow", "Russia", "Central")
    location.set_population(0)
    assert location.population == 0


def test_location_field_types():
    """Тест типов полей локации"""
    location = Location("LOC001", "Moscow", "Russia", "Central")
    location.set_timezone("Europe/Moscow")
    location.set_population(12655050)

    assert isinstance(location.location_id, str)
    assert isinstance(location.name, str)
    assert isinstance(location.country, str)
    assert isinstance(location.region, str)
    assert location.timezone is None or isinstance(location.timezone, str)
    assert location.population is None or isinstance(location.population, int)
    assert location.area_km2 is None or isinstance(location.area_km2, float)


def test_location_data_integrity():
    """Тест целостности данных локации"""
    location = Location("LOC001", "Moscow", "Russia", "Central")

    # Изменяем некоторые поля
    location.set_timezone("Europe/Moscow")
    location.set_population(12655050)

    # Проверяем, что основные поля остались неизменными
    assert location.location_id == "LOC001"
    assert location.name == "Moscow"
    assert location.country == "Russia"
    assert location.region == "Central"

    # Проверяем измененные поля
    assert location.timezone == "Europe/Moscow"
    assert location.population == 12655050


def test_location_has_coordinates_valid():
    """Тест установки валидных координат"""
    from unittest.mock import Mock
    location = Location("LOC001", "Moscow", "Russia", "Central")

    # Создаем mock объект для Coordinates
    coordinates = Mock()
    coordinates.latitude = 55.7558
    coordinates.longitude = 37.6173

    # Метод has_coordinates не должен выбрасывать исключение для валидных координат
    location.has_coordinates(coordinates)


def test_location_has_coordinates_invalid():
    """Тест установки невалидных координат"""
    location = Location("LOC001", "Moscow", "Russia", "Central")

    with pytest.raises(ValueError, match="Координаты не могут быть None"):
        location.has_coordinates(None)


def test_location_contains_station_valid():
    """Тест добавления валидной станции"""
    from unittest.mock import Mock
    location = Location("LOC001", "Moscow", "Russia", "Central")

    # Создаем mock объект для WeatherStation
    station = Mock()
    station.name = "Moscow"  # Совпадает с именем локации

    # Метод contains_station не должен выбрасывать исключение для валидной станции
    location.contains_station(station)


def test_location_contains_station_invalid():
    """Тест добавления невалидной станции"""
    from unittest.mock import Mock
    location = Location("LOC001", "Moscow", "Russia", "Central")

    with pytest.raises(ValueError, match="Станция не может быть None"):
        location.contains_station(None)

    # Станция с другим именем
    station = Mock()
    station.name = "St. Petersburg"
    with pytest.raises(ValueError, match="Станция не соответствует локации"):
        location.contains_station(station)


def test_location_has_forecast_valid():
    """Тест установки валидного прогноза"""
    from unittest.mock import Mock
    location = Location("LOC001", "Moscow", "Russia", "Central")

    # Создаем mock объект для Forecast
    forecast = Mock()
    forecast.location_name = "Different City"

    # Метод has_forecast должен изменить location_name на имя локации
    location.has_forecast(forecast)
    assert forecast.location_name == "Moscow"


def test_location_has_forecast_invalid():
    """Тест установки невалидного прогноза"""
    location = Location("LOC001", "Moscow", "Russia", "Central")

    with pytest.raises(ValueError, match="Прогноз не может быть None"):
        location.has_forecast(None)


def test_location_receives_data_valid():
    """Тест получения валидных данных о погоде"""
    from unittest.mock import Mock
    location = Location("LOC001", "Moscow", "Russia", "Central")

    # Создаем mock объект для WeatherData
    weather_data = Mock()
    weather_data.temperature = 20.5
    weather_data.humidity = 65

    # Метод receives_data не должен выбрасывать исключение для валидных данных
    location.receives_data(weather_data)


def test_location_receives_data_invalid():
    """Тест получения невалидных данных о погоде"""
    location = Location("LOC001", "Moscow", "Russia", "Central")

    with pytest.raises(ValueError, match="Данные о погоде не могут быть None"):
        location.receives_data(None)


def test_location_boundary_values():
    """Тест граничных значений для локации"""
    # Пустые строки для опциональных полей
    location = Location("LOC001", "Moscow", "Russia", "Central")
    location.country = ""  # Пустая строка разрешена
    location.region = ""   # Пустая строка разрешена

    assert location.country == ""
    assert location.region == ""

    # Большое население
    location.set_population(1000000000)
    assert location.population == 1000000000


def test_location_associations():
    """Тест ассоциаций локации"""
    location = Location("LOC001", "Moscow", "Russia", "Central")

    # Проверяем, что методы ассоциаций существуют и вызываются
    assert hasattr(location, 'has_coordinates')
    assert hasattr(location, 'contains_station')
    assert hasattr(location, 'has_forecast')
    assert hasattr(location, 'receives_data')

    # Проверяем, что это callable методы
    assert callable(location.has_coordinates)
    assert callable(location.contains_station)
    assert callable(location.has_forecast)
    assert callable(location.receives_data)


