"""Тесты для WeatherModel"""
from models.weather_model import WeatherModel


def test_weather_model_init():
    model = WeatherModel("WM001", "GFS", "Numerical", "v2.0")
    assert model.model_id == "WM001"
    assert model.model_name == "GFS"


