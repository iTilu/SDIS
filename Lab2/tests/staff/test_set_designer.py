"""Тесты для класса SetDesigner"""
import pytest
from staff.set_designer import SetDesigner


def test_set_designer_creation():
    """Тест создания художника-декоратора"""
    designer = SetDesigner("Мария Смирнова", 32, 8, 60000.0)
    assert designer.name == "Мария Смирнова"
    assert designer.age == 32
    assert designer.experience_years == 8
    assert designer.salary == 60000.0
    assert designer.is_available is True
    assert designer.style == ""


def test_set_designer_invalid_name():
    """Тест с невалидным именем"""
    with pytest.raises(ValueError):
        SetDesigner("", 32, 8, 60000.0)


def test_set_designer_add_set():
    """Тест добавления декорации"""
    designer = SetDesigner("Мария Смирнова", 32, 8, 60000.0)
    designer.add_set("Замок")
    assert "Замок" in designer.sets


def test_set_designer_remove_set():
    """Тест удаления декорации"""
    designer = SetDesigner("Мария Смирнова", 32, 8, 60000.0)
    designer.add_set("Замок")
    designer.remove_set("Замок")
    assert "Замок" not in designer.sets


def test_set_designer_set_style():
    """Тест установки стиля"""
    designer = SetDesigner("Мария Смирнова", 32, 8, 60000.0)
    designer.set_style("Барокко")
    assert designer.style == "Барокко"


def test_set_designer_set_availability():
    """Тест установки доступности"""
    designer = SetDesigner("Мария Смирнова", 32, 8, 60000.0)
    designer.set_availability(False)
    assert designer.is_available is False

