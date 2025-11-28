"""Тесты для класса Refund"""
import pytest
from datetime import datetime
from tickets.refund import Refund


def test_refund_creation():
    """Тест создания возврата"""
    refund = Refund("R001", "T001", 1500.0)
    assert refund.refund_number == "R001"
    assert refund.amount == 1500.0

