"""Тесты для класса Revenue"""
import pytest
from datetime import datetime
from finance.revenue import Revenue


def test_revenue_creation():
    """Тест создания дохода"""
    revenue = Revenue("Продажа билетов", 100000.0, datetime.now())
    assert revenue.description == "Продажа билетов"
    assert revenue.amount == 100000.0

