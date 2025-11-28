"""Тесты для ClimateData"""
from data.climate_data import ClimateData


def test_climate_data_init():
    climate = ClimateData("Siberia", "Continental", -5.0)
    assert climate.region_name == "Siberia"
    assert climate.average_temp == -5.0


