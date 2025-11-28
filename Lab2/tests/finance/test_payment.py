"""Тесты для класса Payment"""
import pytest
from datetime import datetime
from finance.payment import Payment


def test_payment_creation():
    """Тест создания платежа"""
    payment = Payment("P001", 50000.0, datetime.now())
    assert payment.payment_number == "P001"
    assert payment.amount == 50000.0

