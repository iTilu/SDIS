"""Тесты для класса Actor"""
import pytest
from datetime import date
from staff.actor import Actor


def test_actor_creation():
    """Тест создания актера"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    assert actor.name == "Иван Иванов"
    assert actor.age == 30
    assert actor.experience_years == 5
    assert actor.salary == 50000.0
    assert actor.is_available is True


def test_actor_invalid_name():
    """Тест с невалидным именем"""
    with pytest.raises(ValueError):
        Actor("", 30, 5, 50000.0)


def test_actor_add_role():
    """Тест добавления роли"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.add_role("Гамлет")
    assert "Гамлет" in actor.roles


def test_actor_remove_role():
    """Тест удаления роли"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.add_role("Гамлет")
    actor.remove_role("Гамлет")
    assert "Гамлет" not in actor.roles


def test_actor_calculate_earnings():
    """Тест расчета заработка"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    assert actor.calculate_total_earnings(12) == 600000.0


def test_actor_set_availability():
    """Тест установки доступности"""
    actor = Actor("Иван Иванов", 30, 5, 50000.0)
    actor.set_availability(False)
    assert actor.is_available is False

