"""Тесты для StationManager"""
from stations.station_manager import StationManager


def test_station_manager_init():
    manager = StationManager("SM001", "Ivan Petrov", 10)
    assert manager.manager_id == "SM001"
    assert manager.experience_years == 10


