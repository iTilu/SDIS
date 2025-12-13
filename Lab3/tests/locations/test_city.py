"""Тесты для City"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from locations.city import City


def test_city_creation_valid():
    """Тест создания города с валидными данными"""
    city = City("C001", "Moscow", "Russia", 12000000)
    assert city.city_id == "C001"
    assert city.name == "Moscow"
    assert city.country == "Russia"
    assert city.population == 12000000
    assert city.area_km2 is None
    assert city.elevation is None
    assert city.climate_type is None


def test_city_creation_invalid_id():
    """Тест создания города с невалидным ID"""
    with pytest.raises(ValueError, match="ID города должен быть непустой строкой"):
        City("", "Moscow", "Russia", 12000000)

    with pytest.raises(ValueError, match="ID города должен быть непустой строкой"):
        City(None, "Moscow", "Russia", 12000000)


def test_city_creation_invalid_name():
    """Тест создания города с невалидным названием"""
    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        City("C001", "", "Russia", 12000000)

    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        City("C001", None, "Russia", 12000000)


def test_city_creation_invalid_country():
    """Тест создания города с невалидной страной"""
    with pytest.raises(TypeError, match="Страна должна быть строкой"):
        City("C001", "Moscow", 123, 12000000)


def test_city_creation_invalid_population():
    """Тест создания города с невалидным населением"""
    with pytest.raises(ValueError, match="Население должно быть неотрицательным"):
        City("C001", "Moscow", "Russia", -1000)

    with pytest.raises(ValueError, match="Население должно быть неотрицательным"):
        City("C001", "Moscow", "Russia", "12000000")


def test_city_set_area_valid():
    """Тест установки валидной площади"""
    city = City("C001", "Moscow", "Russia", 12000000)
    city.set_area(2561.5)
    assert city.area_km2 == 2561.5


def test_city_set_area_invalid():
    """Тест установки невалидной площади"""
    city = City("C001", "Moscow", "Russia", 12000000)

    with pytest.raises(ValueError, match="Площадь должна быть неотрицательной"):
        city.set_area(-100.0)

    # Нулевая площадь допустима (неотрицательная)
    city.set_area(0.0)  # Это должно работать

    with pytest.raises(ValueError, match="Площадь должна быть неотрицательной"):
        city.set_area("2561.5")


def test_city_set_elevation_valid():
    """Тест установки валидной высоты"""
    city = City("C001", "Moscow", "Russia", 12000000)
    city.set_elevation(156.0)
    assert city.elevation == 156.0


def test_city_set_elevation_invalid():
    """Тест установки невалидной высоты"""
    city = City("C001", "Moscow", "Russia", 12000000)

    with pytest.raises(TypeError, match="Высота должна быть числом"):
        city.set_elevation("156.0")


def test_city_set_climate_type_valid():
    """Тест установки валидного типа климата"""
    city = City("C001", "Moscow", "Russia", 12000000)
    city.set_climate_type("continental")
    assert city.climate_type == "continental"


def test_city_set_climate_type_invalid():
    """Тест установки невалидного типа климата"""
    city = City("C001", "Moscow", "Russia", 12000000)

    with pytest.raises(TypeError, match="Тип климата должен быть строкой"):
        city.set_climate_type(123)

    with pytest.raises(TypeError, match="Тип климата должен быть строкой"):
        city.set_climate_type(None)


def test_city_get_density():
    """Тест получения плотности населения"""
    city = City("C001", "Moscow", "Russia", 12000000)
    city.set_area(2561.5)

    density = city.get_density()
    expected_density = 12000000 / 2561.5
    assert density == pytest.approx(expected_density, rel=1e-2)


def test_city_get_density_no_area():
    """Тест получения плотности без установленной площади"""
    city = City("C001", "Moscow", "Russia", 12000000)

    with pytest.raises(ValueError, match="Площадь города не установлена"):
        city.get_density()


def test_city_field_types():
    """Тест типов полей города"""
    city = City("C001", "Moscow", "Russia", 12000000)
    city.set_area(2561.5)
    city.set_elevation(156.0)
    city.set_climate_type("continental")

    assert isinstance(city.city_id, str)
    assert isinstance(city.name, str)
    assert isinstance(city.country, str)
    assert isinstance(city.population, int)
    assert isinstance(city.area_km2, float)
    assert isinstance(city.elevation, float)
    assert isinstance(city.climate_type, str)


def test_city_data_integrity():
    """Тест целостности данных города"""
    city = City("C001", "Moscow", "Russia", 12000000)

    # Изменяем поля
    city.set_area(2561.5)
    city.set_elevation(156.0)
    city.set_climate_type("humid continental")

    # Проверяем, что основные поля остались неизменными
    assert city.city_id == "C001"
    assert city.name == "Moscow"
    assert city.country == "Russia"
    assert city.population == 12000000

    # Проверяем измененные поля
    assert city.area_km2 == 2561.5
    assert city.elevation == 156.0
    assert city.climate_type == "humid continental"


def test_city_boundary_values():
    """Тест граничных значений для города"""
    # Нулевое население
    city1 = City("C001", "Ghost Town", "Nowhere", 0)
    assert city1.population == 0

    # Очень большое население
    city2 = City("C002", "Mega City", "Future", 50000000)
    assert city2.population == 50000000

    # Очень маленькая площадь
    city3 = City("C003", "Tiny Town", "Small", 100)
    city3.set_area(0.1)
    assert city3.area_km2 == 0.1

    # Очень большая высота
    city4 = City("C004", "High City", "Mountains", 1000)
    city4.set_elevation(8848.0)  # Высота Эвереста
    assert city4.elevation == 8848.0


def test_city_extreme_values():
    """Тест экстремальных значений"""
    # Самый большой город в мире
    tokyo = City("TOKYO", "Tokyo", "Japan", 37400000)
    tokyo.set_area(2191.0)

    # Самый маленький город
    smallest_city = City("SMALL", "Smallville", "Nowhere", 1)
    smallest_city.set_area(0.01)

    # Город на большой высоте
    la_paz = City("LAPAZ", "La Paz", "Bolivia", 2900000)
    la_paz.set_elevation(3640.0)

    # Проверки
    assert tokyo.population == 37400000
    assert smallest_city.population == 1
    assert la_paz.elevation == 3640.0


def test_city_population_ranges():
    """Тест различных диапазонов населения"""
    population_ranges = [
        ("Small Village", 500),
        ("Town", 5000),
        ("Small City", 50000),
        ("Medium City", 500000),
        ("Large City", 2000000),
        ("Mega City", 10000000)
    ]

    for name, pop in population_ranges:
        city = City(f"C{len(name)}", name, "Test Country", pop)
        assert city.population == pop


def test_city_climate_types():
    """Тест различных типов климата"""
    climate_types = [
        "tropical",
        "arid",
        "temperate",
        "continental",
        "polar",
        "mediterranean",
        "oceanic",
        "subarctic",
        "subtropical",
        "semiarid"
    ]

    for climate in climate_types:
        city = City("TEST", "Test City", "Test Country", 100000)
        city.set_climate_type(climate)
        assert city.climate_type == climate


def test_city_area_calculations():
    """Тест расчетов с площадью"""
    city = City("CALC", "Calc City", "Math Land", 100000)
    city.set_area(100.0)  # 100 km²

    # Плотность населения: 100000 / 100 = 1000 чел/км²
    density = city.get_density()
    assert density == 1000.0

    # Изменение площади
    city.set_area(200.0)
    density = city.get_density()
    assert density == 500.0


def test_city_workflow():
    """Тест полного жизненного цикла города"""
    # Создание города
    city = City("MOSCOW", "Moscow", "Russia", 12000000)

    # Настройка географических данных
    city.set_area(2561.5)
    city.set_elevation(156.0)
    city.set_climate_type("humid continental")

    # Расчеты
    density = city.get_density()

    # Проверки
    assert city.city_id == "MOSCOW"
    assert city.name == "Moscow"
    assert city.country == "Russia"
    assert city.population == 12000000
    assert city.area_km2 == 2561.5
    assert city.elevation == 156.0
    assert city.climate_type == "humid continental"
    assert density == pytest.approx(12000000 / 2561.5, rel=1e-2)


def test_city_geographical_features():
    """Тест географических особенностей городов"""
    # Город на равнине
    plain_city = City("PLAIN", "Plain City", "Flatland", 50000)
    plain_city.set_elevation(50.0)
    plain_city.set_climate_type("temperate")

    # Город в горах
    mountain_city = City("MOUNTAIN", "Mountain City", "Highlands", 10000)
    mountain_city.set_elevation(2000.0)
    mountain_city.set_climate_type("alpine")

    # Город у моря
    coastal_city = City("COASTAL", "Coastal City", "Sealand", 150000)
    coastal_city.set_elevation(5.0)
    coastal_city.set_climate_type("maritime")

    # Проверки
    assert plain_city.elevation == 50.0
    assert mountain_city.elevation == 2000.0
    assert coastal_city.elevation == 5.0


def test_city_population_growth():
    """Тест моделирования роста населения"""
    city = City("GROWTH", "Growth City", "Future", 100000)

    # Симуляция роста населения (в реальности это было бы сложнее)
    # Здесь просто проверяем, что можем устанавливать разные значения
    populations = [100000, 110000, 121000, 133100, 146410]

    for pop in populations:
        city.population = pop  # В реальности это должно быть через метод
        assert city.population == pop


def test_city_international_cities():
    """Тест городов из разных стран"""
    cities_data = [
        ("NYC", "New York City", "USA", 8419000),
        ("LONDON", "London", "UK", 8982000),
        ("TOKYO", "Tokyo", "Japan", 37400000),
        ("PARIS", "Paris", "France", 2141000),
        ("SYDNEY", "Sydney", "Australia", 5312000)
    ]

    for city_id, name, country, pop in cities_data:
        city = City(city_id, name, country, pop)
        assert city.city_id == city_id
        assert city.name == name
        assert city.country == country
        assert city.population == pop


def test_city_error_handling():
    """Тест обработки ошибок"""
    city = City("TEST", "Test City", "Test Country", 100000)

    # Попытка установки отрицательной площади
    with pytest.raises(ValueError):
        city.set_area(-50.0)

    # Попытка установки неправильного типа площади
    with pytest.raises(ValueError):
        city.set_area("large")

    # Попытка установки неправильного типа для высоты
    with pytest.raises(TypeError):
        city.set_elevation("high")

    # Попытка установки неправильного типа для климата
    with pytest.raises(TypeError):
        city.set_climate_type(42)

    # Попытка расчета плотности без площади
    with pytest.raises(ValueError):
        city.get_density()


def test_city_state_consistency():
    """Тест согласованности состояний"""
    city = City("CONSISTENT", "Consistent City", "Consistency", 50000)

    # Начальное состояние
    assert city.area_km2 is None
    assert city.elevation is None
    assert city.climate_type is None

    # После установки данных
    city.set_area(100.0)
    city.set_elevation(200.0)
    city.set_climate_type("temperate")

    assert city.area_km2 == 100.0
    assert city.elevation == 200.0
    assert city.climate_type == "temperate"

    # Плотность должна рассчитываться
    density = city.get_density()
    assert density == 500.0


