"""Тесты для Hygrometer"""
from equipment.hygrometer import Hygrometer


def test_hygrometer_init():
    hygro = Hygrometer("HY001", 100.0, 0.5, "capacitive")
    assert hygro.device_id == "HY001"
    assert hygro.technology == "capacitive"


