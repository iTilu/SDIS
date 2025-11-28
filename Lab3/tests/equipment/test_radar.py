"""Тесты для Radar"""
from equipment.radar import Radar


def test_radar_init():
    radar = Radar("RAD001", "Moscow", 250.0, 5.6)
    assert radar.radar_id == "RAD001"
    assert radar.range_km == 250.0


