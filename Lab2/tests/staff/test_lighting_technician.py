"""Тесты для класса LightingTechnician"""
import pytest
from staff.lighting_technician import LightingTechnician


def test_lighting_technician_creation():
    """Тест создания осветителя"""
    technician = LightingTechnician("Андрей Морозов", 30, 7, 50000.0)
    assert technician.name == "Андрей Морозов"
    assert technician.age == 30

