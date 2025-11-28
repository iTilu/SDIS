"""Тесты для класса BoxOffice"""
import pytest
from venues.box_office import BoxOffice


def test_box_office_creation():
    """Тест создания кассы"""
    box_office = BoxOffice(1, "Вход")
    assert box_office.number == 1
    assert box_office.location == "Вход"

