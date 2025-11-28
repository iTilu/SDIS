"""Тесты для Coordinates"""
from locations.coordinates import Coordinates


def test_coordinates_init():
    coords = Coordinates(55.7558, 37.6173)
    assert coords.latitude == 55.7558
    assert coords.longitude == 37.6173


