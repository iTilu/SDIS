"""Тесты для класса Expense"""
import pytest
from datetime import datetime
from finance.expense import Expense


def test_expense_creation():
    """Тест создания расхода"""
    expense = Expense("Закупка костюмов", 50000.0, datetime.now())
    assert expense.description == "Закупка костюмов"
    assert expense.amount == 50000.0

