"""Тесты для класса CostumeRental"""
import pytest
from datetime import datetime, timedelta
from costumes.costume_rental import CostumeRental


def test_costume_rental_creation():
    """Тест создания проката"""
    rental = CostumeRental("Костюм", "Иван Иванов", datetime.now())
    assert rental.costume_name == "Костюм"
    assert rental.actor_name == "Иван Иванов"

