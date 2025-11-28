"""Тесты для класса Tour"""
import pytest
from datetime import datetime
from performances.tour import Tour


def test_tour_creation():
    """Тест создания гастролей"""
    start = datetime(2024, 1, 1)
    end = datetime(2024, 1, 31)
    tour = Tour("Гастроли", start, end)
    assert tour.name == "Гастроли"
    assert tour.start_date == start

