"""Тесты для класса Stage"""
import pytest
from venues.stage import Stage


def test_stage_creation():
    """Тест создания сцены"""
    stage = Stage("Главная сцена", 10.0, 8.0, 5.0)
    assert stage.name == "Главная сцена"
    assert stage.width == 10.0


def test_stage_calculate_area():
    """Тест расчета площади"""
    stage = Stage("Главная сцена", 10.0, 8.0, 5.0)
    assert stage.calculate_area() == 80.0

