"""Тесты для Satellite"""
from equipment.satellite import Satellite


def test_satellite_init():
    sat = Satellite("SAT001", "WeatherSat-1", "Polar", 800.0)
    assert sat.satellite_id == "SAT001"
    assert sat.altitude == 800.0


