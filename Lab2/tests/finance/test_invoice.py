"""Тесты для класса Invoice"""
import pytest
from datetime import datetime
from finance.invoice import Invoice


def test_invoice_creation():
    """Тест создания счета"""
    invoice = Invoice("INV001", 50000.0, datetime.now())
    assert invoice.invoice_number == "INV001"
    assert invoice.amount == 50000.0

