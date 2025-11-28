"""Тесты для класса Address"""
import pytest
from venues.address import Address


def test_address_creation():
    """Тест создания адреса"""
    address = Address("Театральная площадь", "Москва", "Россия")
    assert address.street == "Театральная площадь"
    assert address.city == "Москва"

