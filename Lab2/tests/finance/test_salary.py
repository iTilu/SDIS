"""Тесты для класса Salary"""
import pytest
from datetime import datetime
from finance.salary import Salary


def test_salary_creation():
    """Тест создания зарплаты"""
    salary = Salary("Иван Иванов", 50000.0, datetime.now())
    assert salary.employee_name == "Иван Иванов"
    assert salary.base_salary == 50000.0


def test_salary_calculate_net():
    """Тест расчета чистой зарплаты"""
    salary = Salary("Иван Иванов", 50000.0, datetime.now())
    net = salary.calculate_net_salary()
    assert net < salary.base_salary

