"""Тесты для класса Session"""
import pytest
from datetime import datetime
from schedule.session import Session


def test_session_creation():
    """Тест создания сеанса"""
    session = Session("Гамлет", datetime.now(), "Главная сцена")
    assert session.performance_name == "Гамлет"
    assert session.venue_name == "Главная сцена"

