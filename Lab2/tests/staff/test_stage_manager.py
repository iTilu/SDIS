"""Тесты для класса StageManager"""
import pytest
from staff.stage_manager import StageManager


def test_stage_manager_creation():
    """Тест создания постановщика"""
    manager = StageManager("Николай Орлов", 42, 15, 70000.0)
    assert manager.name == "Николай Орлов"
    assert manager.age == 42

