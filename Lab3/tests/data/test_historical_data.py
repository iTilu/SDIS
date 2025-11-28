"""Тесты для HistoricalData"""
from datetime import date
from data.historical_data import HistoricalData


def test_historical_data_init():
    start = date(2024, 1, 1)
    end = date(2024, 1, 31)
    hist = HistoricalData("Moscow", start, end)
    assert hist.location_name == "Moscow"
    assert hist.start_date == start


