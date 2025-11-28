"""Тесты для Location"""
from locations.location import Location


def test_location_init():
    loc = Location("L001", "Moscow", "Russia", "Central")
    assert loc.location_id == "L001"
    assert loc.country == "Russia"


