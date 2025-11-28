"""Тесты для класса CostumeDesigner"""
import pytest
from staff.costume_designer import CostumeDesigner


def test_costume_designer_creation():
    """Тест создания костюмера"""
    designer = CostumeDesigner("Анна Смирнова", 35, 10, 60000.0)
    assert designer.name == "Анна Смирнова"
    assert designer.age == 35


def test_costume_designer_add_costume():
    """Тест добавления костюма"""
    designer = CostumeDesigner("Анна Смирнова", 35, 10, 60000.0)
    designer.add_costume("Королевский наряд")
    assert "Королевский наряд" in designer.costumes

