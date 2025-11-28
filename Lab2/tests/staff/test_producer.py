"""Тесты для класса Producer"""
import pytest
from staff.producer import Producer


def test_producer_creation():
    """Тест создания продюсера"""
    producer = Producer("Петр Петров", 40, 10, 80000.0)
    assert producer.name == "Петр Петров"
    assert producer.age == 40
    assert producer.experience_years == 10
    assert producer.salary == 80000.0
    assert producer.is_available is True
    assert producer.budget_managed == 0.0


def test_producer_invalid_name():
    """Тест с невалидным именем"""
    with pytest.raises(ValueError):
        Producer("", 40, 10, 80000.0)


def test_producer_add_show():
    """Тест добавления шоу"""
    producer = Producer("Петр Петров", 40, 10, 80000.0)
    producer.add_show("Гамлет")
    assert "Гамлет" in producer.shows


def test_producer_remove_show():
    """Тест удаления шоу"""
    producer = Producer("Петр Петров", 40, 10, 80000.0)
    producer.add_show("Гамлет")
    producer.remove_show("Гамлет")
    assert "Гамлет" not in producer.shows


def test_producer_set_budget():
    """Тест установки бюджета"""
    producer = Producer("Петр Петров", 40, 10, 80000.0)
    producer.set_budget_managed(1000000.0)
    assert producer.budget_managed == 1000000.0


def test_producer_set_availability():
    """Тест установки доступности"""
    producer = Producer("Петр Петров", 40, 10, 80000.0)
    producer.set_availability(False)
    assert producer.is_available is False

