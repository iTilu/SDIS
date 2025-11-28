"""Тесты для Region"""
from locations.region import Region


def test_region_init():
    region = Region("R001", "Central", "Russia", 650000.0)
    assert region.region_id == "R001"
    assert region.area_km2 == 650000.0


