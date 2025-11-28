"""Тесты для класса Ticket"""
import pytest
from datetime import datetime
from tickets.ticket import Ticket


def test_ticket_creation():
    """Тест создания билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    assert ticket.ticket_number == "T001"
    assert ticket.performance_name == "Гамлет"
    assert ticket.price == 1500.0
    assert ticket.seat_number == "A12"


def test_ticket_sell():
    """Тест продажи билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    date = datetime.now()
    ticket.sell(date)
    assert ticket.is_sold is True
    assert ticket.purchase_date == date


def test_ticket_use():
    """Тест использования билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    date = datetime.now()
    ticket.sell(date)
    ticket.use()
    assert ticket.is_used is True

