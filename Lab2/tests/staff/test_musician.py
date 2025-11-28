"""Тесты для класса Musician"""
import pytest
from staff.musician import Musician


def test_musician_creation():
    """Тест создания музыканта"""
    musician = Musician("Дмитрий Волков", 32, 10, 55000.0)
    assert musician.name == "Дмитрий Волков"
    assert musician.age == 32

