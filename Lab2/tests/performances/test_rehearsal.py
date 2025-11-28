"""Тесты для класса Rehearsal"""
import pytest
from datetime import datetime
from performances.rehearsal import Rehearsal


def test_rehearsal_creation():
    """Тест создания репетиции"""
    rehearsal = Rehearsal("Гамлет", datetime.now(), 120)
    assert rehearsal.performance_name == "Гамлет"
    assert rehearsal.duration_minutes == 120

