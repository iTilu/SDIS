"""Тесты для класса Decoration"""
import pytest
from costumes.decoration import Decoration


def test_decoration_creation():
    """Тест создания декорации"""
    decoration = Decoration("Замок", 5.0, 3.0, 2.0)
    assert decoration.name == "Замок"
    assert decoration.width == 5.0


def test_decoration_calculate_volume():
    """Тест расчета объема"""
    decoration = Decoration("Замок", 5.0, 3.0, 2.0)
    assert decoration.calculate_volume() == 30.0

