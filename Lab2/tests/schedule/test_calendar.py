"""Тесты для класса Calendar"""
import pytest
from datetime import datetime
from schedule.calendar import Calendar


def test_calendar_creation():
    """Тест создания календаря"""
    calendar = Calendar(2024)
    assert calendar.year == 2024

