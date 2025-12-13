"""Тесты для WindAlert"""
import pytest
import sys
import os
from datetime import datetime
from unittest.mock import Mock
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from alerts.wind_alert import WindAlert
from exceptions.weather_exceptions import AlertException


def test_wind_alert_creation_valid():
    """Тест создания оповещения о ветре с валидными данными"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")
    assert alert.alert_id == "WA001"
    assert alert.wind_speed == 30.0
    assert alert.wind_direction == 270
    assert alert.location_name == "Moscow"
    assert alert.gust_speed is None
    assert alert.warning_level == "watch"  # 30.0 -> watch (25-40)
    assert isinstance(alert.issued_at, datetime)


def test_wind_alert_creation_invalid_id():
    """Тест создания оповещения с невалидным ID"""
    with pytest.raises(ValueError, match="ID оповещения должен быть непустой строкой"):
        WindAlert("", 30.0, 270, "Moscow")

    with pytest.raises(ValueError, match="ID оповещения должен быть непустой строкой"):
        WindAlert(None, 30.0, 270, "Moscow")


def test_wind_alert_creation_invalid_wind_speed():
    """Тест создания оповещения с невалидной скоростью ветра"""
    with pytest.raises(ValueError, match="Скорость ветра должна быть неотрицательной"):
        WindAlert("WA001", -10.0, 270, "Moscow")

    with pytest.raises(ValueError, match="Скорость ветра должна быть неотрицательной"):
        WindAlert("WA001", "30", 270, "Moscow")


def test_wind_alert_creation_invalid_direction():
    """Тест создания оповещения с невалидным направлением ветра"""
    with pytest.raises(ValueError, match="Направление должно быть от 0 до 360"):
        WindAlert("WA001", 30.0, -10, "Moscow")

    with pytest.raises(ValueError, match="Направление должно быть от 0 до 360"):
        WindAlert("WA001", 30.0, 400, "Moscow")

    with pytest.raises(ValueError, match="Направление должно быть от 0 до 360"):
        WindAlert("WA001", 30.0, "270", "Moscow")


def test_wind_alert_creation_invalid_location():
    """Тест создания оповещения с невалидным названием локации"""
    with pytest.raises(ValueError, match="Название локации должно быть непустой строкой"):
        WindAlert("WA001", 30.0, 270, "")

    with pytest.raises(ValueError, match="Название локации должно быть непустой строкой"):
        WindAlert("WA001", 30.0, 270, None)


def test_wind_alert_set_gust_speed_valid():
    """Тест установки валидной скорости порывов"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")
    alert.set_gust_speed(35.0)
    assert alert.gust_speed == 35.0


def test_wind_alert_set_gust_speed_invalid():
    """Тест установки невалидной скорости порывов"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")

    with pytest.raises(ValueError, match="Скорость порывов должна быть неотрицательной"):
        alert.set_gust_speed(-5.0)

    with pytest.raises(ValueError, match="Скорость порывов должна быть неотрицательной"):
        alert.set_gust_speed("35")


def test_wind_alert_warning_levels():
    """Тест уровней предупреждения в зависимости от скорости ветра"""
    # Advisory (ветер < 25)
    alert1 = WindAlert("WA001", 20.0, 180, "Moscow")
    assert alert1.warning_level == "advisory"

    # Watch (25 <= ветер < 40)
    alert2 = WindAlert("WA002", 30.0, 180, "Moscow")
    assert alert2.warning_level == "watch"

    # Warning (ветер >= 40)
    alert3 = WindAlert("WA003", 50.0, 180, "Moscow")
    assert alert3.warning_level == "warning"


def test_wind_alert_warning_level_update():
    """Тест обновления уровня предупреждения при установке порывов"""
    alert = WindAlert("WA001", 20.0, 180, "Moscow")
    assert alert.warning_level == "advisory"

    # Установка порывов не должна менять уровень предупреждения
    alert.set_gust_speed(50.0)
    assert alert.warning_level == "advisory"  # Остается advisory


def test_wind_alert_extends_weather_alert():
    """Тест расширения оповещения о погоде"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")
    mock_weather_alert = Mock()
    mock_weather_alert.location_name = "Saint Petersburg"

    alert.extends_weather_alert(mock_weather_alert)
    # Проверяем, что location_name изменился
    assert alert.location_name == "Saint Petersburg"


def test_wind_alert_extends_weather_alert_invalid():
    """Тест расширения оповещения с невалидным параметром"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")

    with pytest.raises(ValueError, match="Оповещение не может быть None"):
        alert.extends_weather_alert(None)


def test_wind_alert_field_types():
    """Тест типов полей оповещения о ветре"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")
    alert.set_gust_speed(35.0)

    assert isinstance(alert.alert_id, str)
    assert isinstance(alert.wind_speed, float)
    assert isinstance(alert.wind_direction, int)
    assert isinstance(alert.location_name, str)
    assert isinstance(alert.gust_speed, float)
    assert isinstance(alert.issued_at, datetime)
    assert isinstance(alert.warning_level, str)


def test_wind_alert_data_integrity():
    """Тест целостности данных оповещения"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")

    # Изменяем поля
    alert.set_gust_speed(35.0)

    # Проверяем, что основные поля остались неизменными
    assert alert.alert_id == "WA001"
    assert alert.wind_speed == 30.0
    assert alert.wind_direction == 270
    assert alert.location_name == "Moscow"
    assert alert.warning_level == "watch"

    # Проверяем измененные поля
    assert alert.gust_speed == 35.0


def test_wind_alert_boundary_values():
    """Тест граничных значений для оповещения о ветре"""
    # Граничные значения скорости ветра
    alert1 = WindAlert("WA001", 0.0, 0, "Moscow")
    assert alert1.wind_speed == 0.0
    assert alert1.warning_level == "advisory"

    # Граничные значения направления
    alert2 = WindAlert("WA002", 30.0, 0, "Moscow")
    assert alert2.wind_direction == 0

    alert3 = WindAlert("WA003", 30.0, 360, "Moscow")
    assert alert3.wind_direction == 360

    # Граничные значения для уровней предупреждения
    alert4 = WindAlert("WA004", 24.9, 180, "Moscow")
    assert alert4.warning_level == "advisory"

    alert5 = WindAlert("WA005", 25.0, 180, "Moscow")
    assert alert5.warning_level == "watch"

    alert6 = WindAlert("WA006", 39.9, 180, "Moscow")
    assert alert6.warning_level == "watch"

    alert7 = WindAlert("WA007", 40.0, 180, "Moscow")
    assert alert7.warning_level == "warning"


def test_wind_alert_extreme_values():
    """Тест экстремальных значений"""
    # Очень сильный ветер
    alert1 = WindAlert("WA001", 200.0, 180, "Moscow")
    assert alert1.wind_speed == 200.0
    assert alert1.warning_level == "warning"

    # Очень сильные порывы
    alert1.set_gust_speed(250.0)
    assert alert1.gust_speed == 250.0


def test_wind_alert_directions():
    """Тест различных направлений ветра"""
    directions = [0, 90, 180, 270, 360]

    for i, direction in enumerate(directions):
        alert = WindAlert(f"WA{i+1:03d}", 30.0, direction, "Moscow")
        assert alert.wind_direction == direction


def test_wind_alert_multiple_operations():
    """Тест множественных операций с оповещением"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")

    # Множественные установки порывов
    gust_speeds = [35.0, 40.0, 50.0, 30.0]
    for gust in gust_speeds:
        alert.set_gust_speed(gust)
        assert alert.gust_speed == gust
        # Уровень предупреждения остается watch, так как зависит от основной скорости ветра


def test_wind_alert_workflow():
    """Тест полного жизненного цикла оповещения о ветре"""
    # Создание оповещения
    alert = WindAlert("WA001", 45.0, 315, "Saint Petersburg")
    assert alert.warning_level == "warning"

    # Установка порывов
    alert.set_gust_speed(55.0)
    assert alert.gust_speed == 55.0

    # Расширение оповещения о погоде
    mock_weather_alert = Mock()
    mock_weather_alert.location_name = "Saint Petersburg"  # Тот же город
    alert.extends_weather_alert(mock_weather_alert)

    # Проверки
    assert alert.alert_id == "WA001"
    assert alert.wind_speed == 45.0
    assert alert.wind_direction == 315
    assert alert.location_name == "Saint Petersburg"  # Не изменилось, так как совпадает
    assert alert.warning_level == "warning"
    assert isinstance(alert.issued_at, datetime)


def test_wind_alert_seasonal_scenarios():
    """Тест сезонных сценариев ветровых оповещений"""
    # Весенний ветер
    spring_alert = WindAlert("SPRING", 25.0, 180, "Moscow")
    assert spring_alert.warning_level == "watch"

    # Штормовой ветер
    storm_alert = WindAlert("STORM", 60.0, 270, "Novosibirsk")
    assert storm_alert.warning_level == "warning"

    # Тихий ветер
    calm_alert = WindAlert("CALM", 5.0, 90, "Krasnodar")
    assert calm_alert.warning_level == "advisory"


def test_wind_alert_compass_directions():
    """Тест направлений ветра по компасу"""
    compass_data = [
        (0, "North"),
        (90, "East"),
        (180, "South"),
        (270, "West"),
        (45, "Northeast"),
        (135, "Southeast"),
        (225, "Southwest"),
        (315, "Northwest"),
    ]

    for direction, name in compass_data:
        alert = WindAlert(f"COMPASS_{name}", 30.0, direction, "Test City")
        assert alert.wind_direction == direction


def test_wind_alert_error_handling():
    """Тест обработки ошибок"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")

    # Попытка установки отрицательной скорости порывов
    with pytest.raises(ValueError):
        alert.set_gust_speed(-10.0)

    # Попытка расширения с None
    with pytest.raises(ValueError):
        alert.extends_weather_alert(None)


def test_wind_alert_state_consistency():
    """Тест согласованности состояний"""
    alert = WindAlert("WA001", 30.0, 270, "Moscow")

    # Начальное состояние
    assert alert.warning_level == "watch"
    assert alert.gust_speed is None

    # После установки порывов
    alert.set_gust_speed(35.0)
    assert alert.gust_speed == 35.0
    # Уровень предупреждения не меняется, так как зависит от основной скорости


