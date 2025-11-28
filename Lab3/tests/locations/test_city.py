"""Тесты для City"""
from locations.city import City


def test_city_init():
    city = City("C001", "Moscow", "Russia", 12000000)
    assert city.city_id == "C001"
    assert city.population == 12000000


