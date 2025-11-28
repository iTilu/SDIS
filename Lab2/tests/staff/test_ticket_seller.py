"""Тесты для класса TicketSeller"""
import pytest
from staff.ticket_seller import TicketSeller


def test_ticket_seller_creation():
    """Тест создания билетера"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    assert seller.name == "Ольга Сидорова"
    assert seller.age == 25

