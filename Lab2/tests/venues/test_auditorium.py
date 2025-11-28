"""Тесты для класса Auditorium"""
import pytest
from venues.auditorium import Auditorium


def test_auditorium_creation():
    """Тест создания зрительного зала"""
    auditorium = Auditorium("Главный зал", 1000)
    assert auditorium.name == "Главный зал"
    assert auditorium.capacity == 1000

