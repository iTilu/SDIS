"""Тесты для класса Theater"""
import pytest
from venues.theater import Theater


def test_theater_creation():
    """Тест создания театра"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    assert theater.name == "Большой театр"
    assert theater.capacity == 2000


def test_theater_add_stage():
    """Тест добавления сцены"""
    theater = Theater("Большой театр", "Театральная площадь, 1", 2000)
    theater.add_stage("Главная сцена")
    assert "Главная сцена" in theater.stages

