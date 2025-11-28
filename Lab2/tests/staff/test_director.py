"""Тесты для класса Director"""
import pytest
from staff.director import Director


def test_director_creation():
    """Тест создания режиссера"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    assert director.name == "Петр Петров"
    assert director.age == 45
    assert director.experience_years == 15
    assert director.salary == 80000.0


def test_director_add_performance():
    """Тест добавления спектакля"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_performance("Гамлет")
    assert "Гамлет" in director.performances


def test_director_add_award():
    """Тест добавления награды"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_award("Золотая маска")
    assert "Золотая маска" in director.awards

