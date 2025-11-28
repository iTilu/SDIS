"""Тесты для Observer"""
from staff.observer import Observer


def test_observer_init():
    observer = Observer("O001", "Alice Brown", ["Weather", "Clouds"], 8)
    assert observer.employee_id == "O001"
    assert observer.shift_hours == 8


