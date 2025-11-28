"""Тесты для класса Budget"""
import pytest
from finance.budget import Budget


def test_budget_creation():
    """Тест создания бюджета"""
    budget = Budget(2024, 1000000.0)
    assert budget.year == 2024
    assert budget.total_amount == 1000000.0


def test_budget_add_expense():
    """Тест добавления расхода"""
    budget = Budget(2024, 1000000.0)
    budget.add_expense(50000.0)
    assert budget.get_total_expenses() == 50000.0
    assert budget.remaining_amount == 950000.0

