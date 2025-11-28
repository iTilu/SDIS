"""Тесты для класса MakeupArtist"""
import pytest
from staff.makeup_artist import MakeupArtist


def test_makeup_artist_creation():
    """Тест создания гримера"""
    artist = MakeupArtist("Мария Петрова", 28, 5, 45000.0)
    assert artist.name == "Мария Петрова"
    assert artist.age == 28

