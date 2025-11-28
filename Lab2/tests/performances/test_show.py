"""Тесты для класса Show"""
import pytest
from datetime import datetime
from performances.show import Show


def test_show_creation():
    """Тест создания показа"""
    show = Show("Гамлет", datetime.now(), "Главная сцена")
    assert show.performance_name == "Гамлет"
    assert show.venue_name == "Главная сцена"

