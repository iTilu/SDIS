"""Тесты для Forecaster"""
from staff.forecaster import Forecaster


def test_forecaster_init():
    forecaster = Forecaster("F001", "Jane Doe", "Short-term", 85.5)
    assert forecaster.employee_id == "F001"
    assert forecaster.accuracy_rate == 85.5


