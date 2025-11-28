"""Тесты для Thermometer"""
from equipment.thermometer import Thermometer


def test_thermometer_init():
    thermo = Thermometer("TH001", -50.0, 50.0, "Celsius")
    assert thermo.device_id == "TH001"
    assert thermo.unit == "Celsius"


