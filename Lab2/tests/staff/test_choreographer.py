"""Тесты для класса Choreographer"""
import pytest
from staff.choreographer import Choreographer


def test_choreographer_creation():
    """Тест создания хореографа"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)
    assert choreographer.name == "Елена Соколова"
    assert choreographer.age == 38

