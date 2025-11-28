"""Тесты для класса Sale"""
import pytest
from datetime import datetime
from tickets.sale import Sale


def test_sale_creation():
    """Тест создания продажи"""
    sale = Sale("S001", "T001", 1500.0)
    assert sale.sale_number == "S001"
    assert sale.amount == 1500.0

