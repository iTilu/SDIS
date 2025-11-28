"""Тесты для Meteorologist"""
from staff.meteorologist import Meteorologist


def test_meteorologist_init():
    met = Meteorologist("M001", "John Smith", "Forecasting", 5)
    assert met.employee_id == "M001"
    assert met.specialization == "Forecasting"


