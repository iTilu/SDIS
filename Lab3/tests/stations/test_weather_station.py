"""Тесты для WeatherStation"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from stations.weather_station import WeatherStation


def test_weather_station_init():
    """Тест инициализации метеостанции"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)
    assert station.station_id == "WS001"
    assert station.name == "Main Station"
    assert station.latitude == 55.7558
    assert station.longitude == 37.6173


def test_weather_station_invalid_latitude():
    """Тест невалидной широты"""
    with pytest.raises(ValueError):
        WeatherStation("WS001", "Main Station", 100.0, 37.6173)


def test_weather_station_set_elevation():
    """Тест установки высоты"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)
    station.set_elevation(150.0)
    assert station.elevation == 150.0


def test_weather_station_creation_valid():
    """Тест создания станции с валидными данными"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    assert station.station_id == "WS001"
    assert station.name == "Main Station"
    assert station.latitude == 55.7558
    assert station.longitude == 37.6173
    assert station.is_operational == True
    assert station.installation_date is None
    assert station.elevation is None
    assert len(station.get_temperature_sensors()) == 0
    # Другие сенсоры не имеют геттеров, проверяем только temperature sensors


def test_weather_station_creation_invalid_id():
    """Тест создания станции с невалидным ID"""
    with pytest.raises(ValueError, match="ID станции должен быть непустой строкой"):
        WeatherStation("", "Main Station", 55.7558, 37.6173)

    with pytest.raises(ValueError, match="ID станции должен быть непустой строкой"):
        WeatherStation(None, "Main Station", 55.7558, 37.6173)


def test_weather_station_creation_invalid_name():
    """Тест создания станции с невалидным названием"""
    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        WeatherStation("WS001", "", 55.7558, 37.6173)

    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        WeatherStation("WS001", None, 55.7558, 37.6173)


def test_weather_station_creation_invalid_latitude():
    """Тест создания станции с невалидной широтой"""
    with pytest.raises(ValueError, match="Широта должна быть от -90 до 90"):
        WeatherStation("WS001", "Main Station", 100.0, 37.6173)

    with pytest.raises(ValueError, match="Широта должна быть от -90 до 90"):
        WeatherStation("WS001", "Main Station", -100.0, 37.6173)

    with pytest.raises(ValueError, match="Широта должна быть от -90 до 90"):
        WeatherStation("WS001", "Main Station", "55.7558", 37.6173)


def test_weather_station_creation_invalid_longitude():
    """Тест создания станции с невалидной долготой"""
    with pytest.raises(ValueError, match="Долгота должна быть от -180 до 180"):
        WeatherStation("WS001", "Main Station", 55.7558, 200.0)

    with pytest.raises(ValueError, match="Долгота должна быть от -180 до 180"):
        WeatherStation("WS001", "Main Station", 55.7558, -200.0)

    with pytest.raises(ValueError, match="Долгота должна быть от -180 до 180"):
        WeatherStation("WS001", "Main Station", 55.7558, "37.6173")


def test_weather_station_boundary_coordinates():
    """Тест граничных значений координат"""
    # Максимальные значения
    station1 = WeatherStation("WS001", "North Pole", 90.0, 180.0)
    assert station1.latitude == 90.0
    assert station1.longitude == 180.0

    # Минимальные значения
    station2 = WeatherStation("WS002", "South Pole", -90.0, -180.0)
    assert station2.latitude == -90.0
    assert station2.longitude == -180.0

    # Нулевые значения
    station3 = WeatherStation("WS003", "Equator", 0.0, 0.0)
    assert station3.latitude == 0.0
    assert station3.longitude == 0.0


def test_add_temperature_sensor_valid():
    """Тест добавления валидного сенсора температуры"""
    from unittest.mock import Mock
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    sensor = Mock()
    sensor.id = "TS001"

    station.add_temperature_sensor(sensor)
    sensors = station.get_temperature_sensors()
    assert len(sensors) == 1
    assert sensor in sensors


def test_add_temperature_sensor_duplicate():
    """Тест добавления дублированного сенсора температуры"""
    from unittest.mock import Mock
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    sensor = Mock()
    sensor.id = "TS001"

    station.add_temperature_sensor(sensor)
    station.add_temperature_sensor(sensor)  # Дубликат

    sensors = station.get_temperature_sensors()
    assert len(sensors) == 1  # Должен быть только один экземпляр


def test_add_humidity_sensor_valid():
    """Тест добавления валидного сенсора влажности"""
    from unittest.mock import Mock
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    sensor = Mock()
    sensor.id = "HS001"

    station.add_humidity_sensor(sensor)
    # Проверяем, что сенсор добавлен (нет публичного метода для получения)


def test_add_pressure_sensor_valid():
    """Тест добавления валидного сенсора давления"""
    from unittest.mock import Mock
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    sensor = Mock()
    sensor.id = "PS001"

    station.add_pressure_sensor(sensor)
    # Проверяем, что сенсор добавлен (нет публичного метода для получения)


def test_get_temperature_sensors_empty():
    """Тест получения пустого списка сенсоров температуры"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)
    sensors = station.get_temperature_sensors()
    assert sensors == []


def test_get_temperature_sensors_copy():
    """Тест получения копии списка сенсоров температуры"""
    from unittest.mock import Mock
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    sensor = Mock()
    sensor.id = "TS001"
    station.add_temperature_sensor(sensor)

    sensors = station.get_temperature_sensors()
    sensors.append(Mock())  # Попытка изменить копию

    # Оригинальный список не должен измениться
    assert len(station.get_temperature_sensors()) == 1


def test_set_elevation_valid():
    """Тест установки валидной высоты"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)
    station.set_elevation(150.0)
    assert station.elevation == 150.0


def test_set_elevation_invalid():
    """Тест установки невалидной высоты"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    with pytest.raises(ValueError, match="Высота должна быть неотрицательной"):
        station.set_elevation(-100.0)

    with pytest.raises(ValueError, match="Высота должна быть неотрицательной"):
        station.set_elevation("150.0")


def test_set_elevation_zero():
    """Тест установки нулевой высоты"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)
    station.set_elevation(0.0)
    assert station.elevation == 0.0


def test_weather_station_field_types():
    """Тест типов полей станции"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)
    station.set_elevation(150.0)
    station.installation_date = "2024-01-15"

    assert isinstance(station.station_id, str)
    assert isinstance(station.name, str)
    assert isinstance(station.latitude, (int, float))
    assert isinstance(station.longitude, (int, float))
    assert isinstance(station.is_operational, bool)
    assert station.installation_date is None or isinstance(station.installation_date, str)
    assert station.elevation is None or isinstance(station.elevation, (int, float))
    assert isinstance(station.get_temperature_sensors(), list)


def test_weather_station_data_integrity():
    """Тест целостности данных станции"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    # Изменяем некоторые поля
    station.set_elevation(150.0)
    station.installation_date = "2024-01-15"
    station.is_operational = False

    # Проверяем, что основные поля остались неизменными
    assert station.station_id == "WS001"
    assert station.name == "Main Station"
    assert station.latitude == 55.7558
    assert station.longitude == 37.6173

    # Проверяем измененные поля
    assert station.elevation == 150.0
    assert station.installation_date == "2024-01-15"
    assert station.is_operational == False


def test_weather_station_multiple_sensors():
    """Тест работы с множественными сенсорами"""
    from unittest.mock import Mock
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    # Добавляем несколько сенсоров разных типов
    temp_sensor1 = Mock()
    temp_sensor1.id = "TS001"
    temp_sensor2 = Mock()
    temp_sensor2.id = "TS002"

    hum_sensor = Mock()
    hum_sensor.id = "HS001"

    press_sensor = Mock()
    press_sensor.id = "PS001"

    station.add_temperature_sensor(temp_sensor1)
    station.add_temperature_sensor(temp_sensor2)
    station.add_humidity_sensor(hum_sensor)
    station.add_pressure_sensor(press_sensor)

    # Проверяем только temperature sensors (единственные с публичным геттером)
    temp_sensors = station.get_temperature_sensors()
    assert len(temp_sensors) == 2
    assert temp_sensor1 in temp_sensors
    assert temp_sensor2 in temp_sensors


def test_weather_station_boundary_elevation():
    """Тест граничных значений высоты"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    # Очень большая высота
    station.set_elevation(10000.0)
    assert station.elevation == 10000.0

    # Очень маленькая высота (близкая к нулю)
    station.set_elevation(0.001)
    assert station.elevation == 0.001


def test_weather_station_sensor_management():
    """Тест управления сенсорами станции"""
    from unittest.mock import Mock
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    # Добавляем сенсоры
    sensors = []
    for i in range(5):
        sensor = Mock()
        sensor.id = f"TS00{i}"
        sensors.append(sensor)
        station.add_temperature_sensor(sensor)

    # Проверяем, что все сенсоры добавлены
    temp_sensors = station.get_temperature_sensors()
    assert len(temp_sensors) == 5
    for sensor in sensors:
        assert sensor in temp_sensors


def test_weather_station_associations():
    """Тест ассоциаций станции"""
    station = WeatherStation("WS001", "Main Station", 55.7558, 37.6173)

    # Проверяем, что методы ассоциаций существуют
    assert hasattr(station, 'add_temperature_sensor')
    assert hasattr(station, 'add_humidity_sensor')
    assert hasattr(station, 'add_pressure_sensor')
    assert hasattr(station, 'get_temperature_sensors')
    assert hasattr(station, 'set_elevation')

    # Проверяем, что это callable методы
    assert callable(station.add_temperature_sensor)
    assert callable(station.add_humidity_sensor)
    assert callable(station.add_pressure_sensor)
    assert callable(station.get_temperature_sensors)
    assert callable(station.set_elevation)


