"""Тесты для DataPoint"""
from datetime import datetime
from data.data_point import DataPoint


def test_data_point_init():
    timestamp = datetime.now()
    point = DataPoint("DP001", timestamp, 20.5)
    assert point.point_id == "DP001"
    assert point.value == 20.5


