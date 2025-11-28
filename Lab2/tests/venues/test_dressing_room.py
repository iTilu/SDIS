"""Тесты для класса DressingRoom"""
import pytest
from venues.dressing_room import DressingRoom


def test_dressing_room_creation():
    """Тест создания гримерки"""
    room = DressingRoom(1, 4)
    assert room.number == 1
    assert room.capacity == 4

