"""Тесты для класса Premiere"""
import pytest
from datetime import datetime
from performances.premiere import Premiere


def test_premiere_creation():
    """Тест создания премьеры"""
    premiere = Premiere("Гамлет", datetime.now(), "Главная сцена")
    assert premiere.performance_name == "Гамлет"
    assert premiere.venue_name == "Главная сцена"

