"""Тесты для класса Theater"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from venues.theater import Theater


def test_theater_creation_valid():
    """Тест создания театра с валидными данными"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    assert theater.name == "Большой театр"
    assert theater.address == "Театральная площадь, 1"
    assert theater.capacity == 2000
    assert theater.founded_year == 0
    assert theater.is_active == True
    assert theater.get_stages() == []
    assert theater.get_dressing_rooms() == []


def test_theater_creation_invalid_name():
    """Тест создания театра с невалидным названием"""
    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        Theater("", "Адрес", 100)

    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        Theater(None, "Адрес", 100)


def test_theater_creation_invalid_address():
    """Тест создания театра с невалидным адресом"""
    with pytest.raises(ValueError, match="Адрес должен быть непустой строкой"):
        Theater("Театр", "", 100)

    with pytest.raises(ValueError, match="Адрес должен быть непустой строкой"):
        Theater("Театр", None, 100)


def test_theater_creation_invalid_capacity():
    """Тест создания театра с невалидной вместимостью"""
    with pytest.raises(ValueError, match="Вместимость должна быть положительным целым числом"):
        Theater("Театр", "Адрес", 0)

    with pytest.raises(ValueError, match="Вместимость должна быть положительным целым числом"):
        Theater("Театр", "Адрес", -100)

    with pytest.raises(ValueError, match="Вместимость должна быть положительным целым числом"):
        Theater("Театр", "Адрес", "2000")


def test_theater_add_stage_valid():
    """Тест добавления валидной сцены"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_stage("Главная сцена")
    assert "Главная сцена" in theater.get_stages()
    assert len(theater.get_stages()) == 1


def test_theater_add_stage_invalid():
    """Тест добавления невалидной сцены"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)

    with pytest.raises(TypeError, match="Название сцены должно быть строкой"):
        theater.add_stage(123)

    with pytest.raises(TypeError, match="Название сцены должно быть строкой"):
        theater.add_stage(None)


def test_theater_add_duplicate_stage():
    """Тест добавления дублированной сцены"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_stage("Главная сцена")
    theater.add_stage("Главная сцена")  # Дубликат

    stages = theater.get_stages()
    assert stages.count("Главная сцена") == 1  # Должен быть только один экземпляр
    assert len(stages) == 1


def test_theater_get_stages():
    """Тест получения списка сцен"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_stage("Главная сцена")
    theater.add_stage("Малая сцена")

    stages = theater.get_stages()
    assert "Главная сцена" in stages
    assert "Малая сцена" in stages
    assert len(stages) == 2

    # Проверяем, что возвращается копия, а не оригинал
    stages.append("Новая сцена")
    assert "Новая сцена" not in theater.get_stages()  # Оригинал не должен измениться


def test_theater_get_stages_empty():
    """Тест получения пустого списка сцен"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    stages = theater.get_stages()
    assert stages == []
    assert len(stages) == 0


def test_theater_add_dressing_room_valid():
    """Тест добавления валидной гримерки"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_dressing_room("Гримерка №1")
    assert "Гримерка №1" in theater.get_dressing_rooms()
    assert len(theater.get_dressing_rooms()) == 1


def test_theater_add_dressing_room_invalid():
    """Тест добавления невалидной гримерки"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)

    with pytest.raises(TypeError, match="Название гримерки должно быть строкой"):
        theater.add_dressing_room(123)

    with pytest.raises(TypeError, match="Название гримерки должно быть строкой"):
        theater.add_dressing_room(None)


def test_theater_add_duplicate_dressing_room():
    """Тест добавления дублированной гримерки"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_dressing_room("Гримерка №1")
    theater.add_dressing_room("Гримерка №1")  # Дубликат

    rooms = theater.get_dressing_rooms()
    assert rooms.count("Гримерка №1") == 1  # Должен быть только один экземпляр
    assert len(rooms) == 1


def test_theater_get_dressing_rooms():
    """Тест получения списка гримерок"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_dressing_room("Гримерка №1")
    theater.add_dressing_room("Гримерка №2")

    rooms = theater.get_dressing_rooms()
    assert "Гримерка №1" in rooms
    assert "Гримерка №2" in rooms
    assert len(rooms) == 2

    # Проверяем, что возвращается копия, а не оригинал
    rooms.append("Гримерка №3")
    assert "Гримерка №3" not in theater.get_dressing_rooms()  # Оригинал не должен измениться


def test_theater_get_dressing_rooms_empty():
    """Тест получения пустого списка гримерок"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    rooms = theater.get_dressing_rooms()
    assert rooms == []
    assert len(rooms) == 0


def test_theater_set_founded_year_valid():
    """Тест установки валидного года основания"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.set_founded_year(1825)
    assert theater.founded_year == 1825


def test_theater_set_founded_year_invalid():
    """Тест установки невалидного года основания"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)

    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        theater.set_founded_year(-100)

    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        theater.set_founded_year("1825")


def test_theater_set_founded_year_zero():
    """Тест установки нулевого года основания"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.set_founded_year(0)
    assert theater.founded_year == 0


def test_theater_stages_property():
    """Тест свойства stages"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_stage("Главная сцена")

    # Проверяем, что stages - это свойство, возвращающее список
    assert hasattr(theater, 'stages')
    assert isinstance(theater.stages, list)
    assert "Главная сцена" in theater.stages


def test_theater_dressing_rooms_property():
    """Тест свойства dressing_rooms"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_dressing_room("Гримерка №1")

    # Проверяем, что dressing_rooms - это свойство, возвращающее список
    assert hasattr(theater, 'dressing_rooms')
    assert isinstance(theater.dressing_rooms, list)
    assert "Гримерка №1" in theater.dressing_rooms


def test_theater_field_types():
    """Тест типов полей театра"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.set_founded_year(1825)
    theater.add_stage("Главная сцена")
    theater.add_dressing_room("Гримерка №1")

    assert isinstance(theater.name, str)
    assert isinstance(theater.address, str)
    assert isinstance(theater.capacity, int)
    assert isinstance(theater.founded_year, int)
    assert isinstance(theater.is_active, bool)
    assert isinstance(theater.get_stages(), list)
    assert isinstance(theater.get_dressing_rooms(), list)


def test_theater_data_integrity():
    """Тест целостности данных театра"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)

    # Изменяем некоторые поля
    theater.set_founded_year(1825)
    theater.is_active = False
    theater.add_stage("Главная сцена")
    theater.add_stage("Малая сцена")
    theater.add_dressing_room("Гримерка №1")
    theater.add_dressing_room("Гримерка №2")

    # Проверяем, что основные поля остались неизменными
    assert theater.name == "Большой театр"
    assert theater.address == "Театральная площадь, 1"
    assert theater.capacity == 2000

    # Проверяем измененные поля
    assert theater.founded_year == 1825
    assert not theater.is_active
    assert len(theater.get_stages()) == 2
    assert len(theater.get_dressing_rooms()) == 2


def test_theater_boundary_values():
    """Тест граничных значений для театра"""
    # Минимальная вместимость
    theater1 = Theater("Маленький театр", "Улица 1", 1)
    assert theater1.capacity == 1

    # Нулевой год основания
    theater1.set_founded_year(0)
    assert theater1.founded_year == 0

    # Большая вместимость
    theater2 = Theater("Большой театр", "Площадь", 100000)
    assert theater2.capacity == 100000


def test_theater_stages_management():
    """Тест управления сценами театра"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)

    # Добавляем сцены
    stages_to_add = ["Главная сцена", "Малая сцена", "Экспериментальная сцена", "Летняя площадка"]
    for stage in stages_to_add:
        theater.add_stage(stage)

    assert len(theater.get_stages()) == 4
    for stage in stages_to_add:
        assert stage in theater.get_stages()


def test_theater_dressing_rooms_management():
    """Тест управления гримерками театра"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)

    # Добавляем гримерки
    rooms_to_add = ["Гримерка №1", "Гримерка №2", "Гримерка №3", "Гримерка №4"]
    for room in rooms_to_add:
        theater.add_dressing_room(room)

    assert len(theater.get_dressing_rooms()) == 4
    for room in rooms_to_add:
        assert room in theater.get_dressing_rooms()


def test_theater_very_old_founded_year():
    """Тест театра с очень старым годом основания"""
    theater = Theater("Древний театр", "Адрес", 100)
    theater.set_founded_year(500)  # Театр древней Греции
    assert theater.founded_year == 500


def test_theater_future_founded_year():
    """Тест театра с будущим годом основания (для планируемых театров)"""
    theater = Theater("Будущий театр", "Адрес", 100)
    theater.set_founded_year(2030)
    assert theater.founded_year == 2030

