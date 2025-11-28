"""Тесты для класса Manager"""
import pytest
from staff.manager import Manager


def test_manager_creation():
    """Тест создания менеджера"""
    manager = Manager("Алексей Новиков", 35, 8, 75000.0)
    assert manager.name == "Алексей Новиков"
    assert manager.age == 35

