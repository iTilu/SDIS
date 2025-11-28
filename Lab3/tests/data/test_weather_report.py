"""Тесты для WeatherReport"""
from datetime import datetime
from data.weather_report import WeatherReport


def test_weather_report_init():
    timestamp = datetime.now()
    report = WeatherReport("R001", "Monthly Report", timestamp, "John Doe")
    assert report.report_id == "R001"
    assert report.title == "Monthly Report"


