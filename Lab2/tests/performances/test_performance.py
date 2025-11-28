"""Тесты для класса Performance"""
import pytest
from datetime import datetime
from performances.performance import Performance


def test_performance_creation():
    """Тест создания спектакля"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    assert perf.name == "Гамлет"
    assert perf.duration_minutes == 180
    assert perf.genre == "Драма"
    assert perf.ticket_price == 1500.0


def test_performance_add_actor():
    """Тест добавления актера"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.add_actor("Иван Иванов")
    assert "Иван Иванов" in perf.actors


def test_performance_set_premiere_date():
    """Тест установки даты премьеры"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    date = datetime(2024, 1, 15)
    perf.set_premiere_date(date)
    assert perf.premiere_date == date


def test_performance_increment_shows():
    """Тест увеличения счетчика показов"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.increment_shows()
    assert perf.total_shows == 1

