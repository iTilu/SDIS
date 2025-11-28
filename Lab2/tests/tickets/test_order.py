"""Тесты для класса Order"""
import pytest
from datetime import datetime
from tickets.order import Order


def test_order_creation():
    """Тест создания заказа"""
    order = Order("ORD001", "Иван Иванов", datetime.now())
    assert order.order_number == "ORD001"
    assert order.customer_name == "Иван Иванов"


def test_order_add_ticket():
    """Тест добавления билета"""
    order = Order("ORD001", "Иван Иванов", datetime.now())
    order.add_ticket("T001")
    assert "T001" in order.tickets

