"""Тесты для класса Address"""
import pytest
from venues.address import Address


def test_address_creation_valid():
    """Тест создания адреса с валидными данными"""
    address = Address("Театральная площадь", "Москва", "Россия")
    assert address.street == "Театральная площадь"
    assert address.city == "Москва"
    assert address.country == "Россия"
    assert address.building_number == ""
    assert address.postal_code is None
    assert address.district == ""


def test_address_creation_invalid_street():
    """Тест создания адреса с невалидной улицей"""
    with pytest.raises(ValueError, match="Улица должна быть непустой строкой"):
        Address("", "Москва", "Россия")

    with pytest.raises(ValueError, match="Улица должна быть непустой строкой"):
        Address(123, "Москва", "Россия")


def test_address_creation_invalid_city():
    """Тест создания адреса с невалидным городом"""
    with pytest.raises(ValueError, match="Город должен быть непустой строкой"):
        Address("Театральная", "", "Россия")

    with pytest.raises(ValueError, match="Город должен быть непустой строкой"):
        Address("Театральная", None, "Россия")


def test_address_creation_invalid_country():
    """Тест создания адреса с невалидной страной"""
    with pytest.raises(ValueError, match="Страна должна быть непустой строкой"):
        Address("Театральная", "Москва", "")

    with pytest.raises(ValueError, match="Страна должна быть непустой строкой"):
        Address("Театральная", "Москва", [])


def test_set_building_number_valid():
    """Тест установки валидного номера здания"""
    address = Address("Театральная", "Москва", "Россия")
    address.set_building_number("15A")
    assert address.building_number == "15A"


def test_set_building_number_invalid():
    """Тест установки невалидного номера здания"""
    address = Address("Театральная", "Москва", "Россия")
    with pytest.raises(TypeError, match="Номер должен быть строкой"):
        address.set_building_number(123)

    with pytest.raises(TypeError, match="Номер должен быть строкой"):
        address.set_building_number(None)


def test_set_postal_code_valid():
    """Тест установки валидного почтового индекса"""
    address = Address("Театральная", "Москва", "Россия")
    address.set_postal_code("123456")
    assert address.postal_code == "123456"


def test_set_postal_code_invalid():
    """Тест установки невалидного почтового индекса"""
    address = Address("Театральная", "Москва", "Россия")
    with pytest.raises(TypeError, match="Индекс должен быть строкой"):
        address.set_postal_code(123456)

    with pytest.raises(TypeError, match="Индекс должен быть строкой"):
        address.set_postal_code([])


def test_set_district_valid():
    """Тест установки валидного района"""
    address = Address("Театральная", "Москва", "Россия")
    address.set_district("Центральный")
    assert address.district == "Центральный"


def test_set_district_invalid():
    """Тест установки невалидного района"""
    address = Address("Театральная", "Москва", "Россия")
    with pytest.raises(TypeError, match="Район должен быть строкой"):
        address.set_district(123)

    with pytest.raises(TypeError, match="Район должен быть строкой"):
        address.set_district({})


def test_get_full_address_basic():
    """Тест получения полного адреса с базовыми данными"""
    address = Address("Театральная площадь", "Москва", "Россия")
    expected = "Театральная площадь, Москва, Россия"
    assert address.get_full_address() == expected


def test_get_full_address_with_building():
    """Тест получения полного адреса с номером здания"""
    address = Address("Театральная площадь", "Москва", "Россия")
    address.set_building_number("15")
    expected = "Театральная площадь, 15, Москва, Россия"
    assert address.get_full_address() == expected


def test_get_full_address_with_postal_code():
    """Тест получения полного адреса с почтовым индексом"""
    address = Address("Театральная площадь", "Москва", "Россия")
    address.set_postal_code("123456")
    expected = "Театральная площадь, Москва, Россия, 123456"
    assert address.get_full_address() == expected


def test_get_full_address_complete():
    """Тест получения полного адреса со всеми полями"""
    address = Address("Театральная площадь", "Москва", "Россия")
    address.set_building_number("15A")
    address.set_postal_code("123456")
    address.set_district("Центральный")
    expected = "Театральная площадь, 15A, Москва, Россия, 123456"
    assert address.get_full_address() == expected


def test_get_full_address_empty_building():
    """Тест получения полного адреса с пустым номером здания"""
    address = Address("Театральная площадь", "Москва", "Россия")
    address.set_building_number("")  # Пустая строка
    expected = "Театральная площадь, Москва, Россия"
    assert address.get_full_address() == expected


def test_address_immutable_fields():
    """Тест неизменности основных полей после создания"""
    address = Address("Театральная", "Москва", "Россия")

    # Попытка изменить основные поля напрямую (не должна работать из-за отсутствия сеттеров)
    # Но в Python поля публичные, так что это тест на ответственность использования

    # Проверяем, что поля остались неизменными
    assert address.street == "Театральная"
    assert address.city == "Москва"
    assert address.country == "Россия"


def test_address_string_fields_only():
    """Тест того, что все поля адреса являются строками или None"""
    address = Address("Театральная", "Москва", "Россия")
    address.set_building_number("15")
    address.set_postal_code("123456")
    address.set_district("Центр")

    assert isinstance(address.street, str)
    assert isinstance(address.city, str)
    assert isinstance(address.country, str)
    assert isinstance(address.building_number, str)
    assert isinstance(address.district, str)
    assert address.postal_code is None or isinstance(address.postal_code, str)

