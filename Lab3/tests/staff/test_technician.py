"""Тесты для Technician"""
from staff.technician import Technician


def test_technician_init():
    tech = Technician("T001", "Mike Wilson", "Electronics", "Level 2")
    assert tech.employee_id == "T001"
    assert tech.certification == "Level 2"


