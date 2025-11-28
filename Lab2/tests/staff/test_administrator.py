"""Тесты для класса Administrator"""
import pytest
from staff.administrator import Administrator


def test_administrator_creation():
    """Тест создания администратора"""
    admin = Administrator("Сергей Козлов", 40, 10, 70000.0)
    assert admin.name == "Сергей Козлов"
    assert admin.age == 40

