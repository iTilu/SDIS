"""Тесты для DataAnalyst"""
from staff.data_analyst import DataAnalyst


def test_data_analyst_init():
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", ["Python", "R"])
    assert analyst.employee_id == "DA001"
    assert len(analyst.tools) == 2


