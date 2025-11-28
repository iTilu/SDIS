"""Тесты для класса Wardrobe"""
import pytest
from venues.wardrobe import Wardrobe


def test_wardrobe_creation():
    """Тест создания гардероба"""
    wardrobe = Wardrobe("Гардероб 1", 200)
    assert wardrobe.name == "Гардероб 1"
    assert wardrobe.capacity == 200

