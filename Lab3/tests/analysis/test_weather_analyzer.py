"""Тесты для WeatherAnalyzer"""
from analysis.weather_analyzer import WeatherAnalyzer


def test_weather_analyzer_init():
    analyzer = WeatherAnalyzer("WA001", "Statistical", ["Mean", "Std"])
    assert analyzer.analyzer_id == "WA001"
    assert analyzer.analysis_type == "Statistical"


