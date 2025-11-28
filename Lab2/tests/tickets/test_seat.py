"""Тесты для класса Seat"""
import pytest
from tickets.seat import Seat


def test_seat_creation():
    """Тест создания места"""
    seat = Seat("A12", 1, "Партер")
    assert seat.seat_number == "A12"
    assert seat.row == 1


def test_seat_calculate_price():
    """Тест расчета цены"""
    seat = Seat("A12", 1, "Партер")
    seat.set_price_multiplier(1.5)
    assert seat.calculate_price(1000.0) == 1500.0

