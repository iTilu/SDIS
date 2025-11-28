"""Тесты для класса SoundEngineer"""
import pytest
from staff.sound_engineer import SoundEngineer


def test_sound_engineer_creation():
    """Тест создания звукорежиссера"""
    engineer = SoundEngineer("Владимир Лебедев", 33, 8, 52000.0)
    assert engineer.name == "Владимир Лебедев"
    assert engineer.age == 33

