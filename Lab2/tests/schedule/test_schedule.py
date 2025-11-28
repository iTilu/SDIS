"""Тесты для класса Schedule"""
import pytest
from schedule.schedule import Schedule


def test_schedule_creation():
    """Тест создания расписания"""
    schedule = Schedule(1, 2024)
    assert schedule.month == 1
    assert schedule.year == 2024


def test_schedule_add_event():
    """Тест добавления события"""
    schedule = Schedule(1, 2024)
    schedule.add_event("Премьера")
    assert "Премьера" in schedule.events

