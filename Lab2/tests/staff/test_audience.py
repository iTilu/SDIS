"""Тесты для класса Audience"""
import pytest
from staff.audience import Audience


def test_audience_creation():
    """Тест создания зрителя"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    assert audience.name == "Анна Иванова"
    assert audience.age == 25
    assert audience.email == "anna@example.com"
    assert audience.loyalty_points == 0
    assert audience.is_member is False


def test_audience_invalid_name():
    """Тест с невалидным именем"""
    with pytest.raises(ValueError):
        Audience("", 25, "anna@example.com")


def test_audience_purchase_ticket():
    """Тест покупки билета"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.purchase_ticket("T001")
    assert "T001" in audience.tickets_purchased
    assert audience.loyalty_points == 10


def test_audience_add_loyalty_points():
    """Тест добавления баллов лояльности"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.add_loyalty_points(50)
    assert audience.loyalty_points == 50


def test_audience_become_member():
    """Тест становления членом"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.become_member("Gold")
    assert audience.is_member is True
    assert audience.membership_type == "Gold"

