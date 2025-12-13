"""Тесты для класса Actor"""
import pytest
import sys
import os
from datetime import date
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from staff.actor import Actor


def test_actor_creation_valid():
    """Тест создания актера с валидными данными"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    assert actor.name == "Иван Иванов"
    assert actor.age == 30
    assert actor.experience_years == 5
    assert actor.salary == 50000.0
    assert actor.is_available is True
    assert actor.contract_end_date is None
    assert actor.roles == []  # Пустой список ролей


def test_actor_creation_invalid_name():
    """Тест создания актера с невалидным именем"""
    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Actor("", 30, 5, 50000.0)

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Actor(None, 30, 5, 50000.0)

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Actor(123, 30, 5, 50000.0)


def test_actor_creation_invalid_age():
    """Тест создания актера с невалидным возрастом"""
    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Actor("Иван", -5, 5, 50000.0)

    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Actor("Иван", "30", 5, 50000.0)

    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Actor("Иван", 30.5, 5, 50000.0)


def test_actor_creation_zero_age():
    """Тест создания актера с нулевым возрастом"""
    actor = Actor("Младенец", 0, 0, 0.0)
    assert actor.age == 0
    assert actor.experience_years == 0
    assert actor.salary == 0.0


def test_actor_creation_invalid_experience():
    """Тест создания актера с невалидным опытом"""
    with pytest.raises(ValueError, match="Опыт должен быть неотрицательным целым числом"):
        Actor("Иван", 30, -1, 50000.0)

    with pytest.raises(ValueError, match="Опыт должен быть неотрицательным целым числом"):
        Actor("Иван", 30, "5", 50000.0)


def test_actor_add_role_valid():
    """Тест добавления валидной роли"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.add_role("Гамлет")
    assert "Гамлет" in actor.roles
    assert len(actor.roles) == 1


def test_actor_add_role_invalid():
    """Тест добавления невалидной роли"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)

    with pytest.raises(TypeError, match="Роль должна быть строкой"):
        actor.add_role(123)

    with pytest.raises(TypeError, match="Роль должна быть строкой"):
        actor.add_role(None)


def test_actor_add_duplicate_role():
    """Тест добавления дублированной роли"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.add_role("Гамлет")
    actor.add_role("Гамлет")  # Дубликат

    assert actor.roles.count("Гамлет") == 1  # Должен быть только один экземпляр
    assert len(actor.roles) == 1


def test_actor_remove_role_existing():
    """Тест удаления существующей роли"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.add_role("Гамлет")
    actor.add_role("Отелло")

    actor.remove_role("Гамлет")
    assert "Гамлет" not in actor.roles
    assert "Отелло" in actor.roles
    assert len(actor.roles) == 1


def test_actor_remove_role_nonexistent():
    """Тест удаления несуществующей роли"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.add_role("Гамлет")

    actor.remove_role("Отелло")  # Несуществующая роль
    assert "Гамлет" in actor.roles  # Существующая роль должна остаться
    assert len(actor.roles) == 1


def test_actor_get_roles():
    """Тест получения списка ролей"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.add_role("Гамлет")
    actor.add_role("Отелло")

    roles = actor.get_roles()
    assert "Гамлет" in roles
    assert "Отелло" in roles
    assert len(roles) == 2

    # Проверяем, что возвращается копия, а не оригинал
    roles.append("Макбет")
    assert "Макбет" not in actor.roles  # Оригинал не должен измениться


def test_actor_get_roles_empty():
    """Тест получения пустого списка ролей"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    roles = actor.get_roles()
    assert roles == []
    assert len(roles) == 0


def test_actor_set_availability_valid():
    """Тест установки валидной доступности"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)

    actor.set_availability(False)
    assert actor.is_available is False

    actor.set_availability(True)
    assert actor.is_available is True


def test_actor_set_availability_invalid():
    """Тест установки невалидной доступности"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)

    with pytest.raises(TypeError, match="Доступность должна быть булевым значением"):
        actor.set_availability("true")

    with pytest.raises(TypeError, match="Доступность должна быть булевым значением"):
        actor.set_availability(1)

    with pytest.raises(TypeError, match="Доступность должна быть булевым значением"):
        actor.set_availability(None)


def test_actor_calculate_total_earnings_valid():
    """Тест расчета общего заработка с валидными данными"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)

    earnings = actor.calculate_total_earnings(12)
    assert earnings == 600000.0

    earnings = actor.calculate_total_earnings(1)
    assert earnings == 50000.0

    earnings = actor.calculate_total_earnings(0)
    assert earnings == 0.0


def test_actor_calculate_total_earnings_invalid():
    """Тест расчета общего заработка с невалидными данными"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)

    with pytest.raises(ValueError, match="Количество месяцев должно быть неотрицательным"):
        actor.calculate_total_earnings(-1)

    with pytest.raises(ValueError, match="Количество месяцев должно быть неотрицательным"):
        actor.calculate_total_earnings("12")


def test_actor_calculate_total_earnings_zero_salary():
    """Тест расчета заработка с нулевой зарплатой"""
    actor = Actor("Бедный актер", 25, 2, 0.0)
    earnings = actor.calculate_total_earnings(12)
    assert earnings == 0.0


def test_actor_calculate_total_earnings_float_months():
    """Тест расчета заработка с дробным количеством месяцев"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)

    with pytest.raises(ValueError, match="Количество месяцев должно быть неотрицательным"):
        actor.calculate_total_earnings(6.5)  # float не принимается


def test_actor_roles_property():
    """Тест свойства roles"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.add_role("Гамлет")

    # Проверяем, что roles - это свойство, возвращающее список
    assert hasattr(actor, 'roles')
    assert isinstance(actor.roles, list)
    assert "Гамлет" in actor.roles


def test_actor_field_types():
    """Тест типов полей актера"""
    test_date = date(2025, 12, 31)
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.contract_end_date = test_date

    assert isinstance(actor.name, str)
    assert isinstance(actor.age, int)
    assert isinstance(actor.experience_years, int)
    assert isinstance(actor.salary, float)
    assert isinstance(actor.is_available, bool)
    assert isinstance(actor.contract_end_date, date) or actor.contract_end_date is None
    assert isinstance(actor.roles, list)


def test_actor_data_integrity():
    """Тест целостности данных актера"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)

    # Изменяем некоторые поля
    actor.add_role("Гамлет")
    actor.add_role("Отелло")
    actor.set_availability(False)

    # Проверяем, что основные поля остались неизменными
    assert actor.name == "Иван Иванов"
    assert actor.age == 30
    assert actor.experience_years == 5
    assert actor.salary == 50000.0

    # Проверяем измененные поля
    assert not actor.is_available
    assert "Гамлет" in actor.roles
    assert "Отелло" in actor.roles
    assert len(actor.roles) == 2


def test_actor_boundary_values():
    """Тест граничных значений для актера"""
    # Максимально возможный возраст
    actor1 = Actor("Старый актер", 150, 70, 1000000.0)
    assert actor1.age == 150

    # Нулевые значения
    actor2 = Actor("Начинающий", 0, 0, 0.0)
    assert actor2.calculate_total_earnings(12) == 0.0

    # Очень большая зарплата
    actor3 = Actor("Звезда", 40, 20, 10000000.0)
    assert actor3.calculate_total_earnings(1) == 10000000.0


def test_actor_roles_manipulation():
    """Тест манипуляции ролями"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)

    # Добавляем роли
    roles_to_add = ["Гамлет", "Отелло", "Король Лир", "Макбет"]
    for role in roles_to_add:
        actor.add_role(role)

    assert len(actor.roles) == 4
    for role in roles_to_add:
        assert role in actor.roles

    # Удаляем некоторые роли
    actor.remove_role("Отелло")
    actor.remove_role("Макбет")

    assert len(actor.roles) == 2
    assert "Гамлет" in actor.roles
    assert "Король Лир" in actor.roles
    assert "Отелло" not in actor.roles
    assert "Макбет" not in actor.roles

