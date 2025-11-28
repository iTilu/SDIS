"""Тесты для Administrator"""
from staff.administrator import Administrator


def test_administrator_init():
    admin = Administrator("A001", "Admin User", "IT", "Full")
    assert admin.employee_id == "A001"
    assert admin.access_level == "Full"


