"""Тесты для TrendAnalyzer"""
from analysis.trend_analyzer import TrendAnalyzer


def test_trend_analyzer_init():
    analyzer = TrendAnalyzer("TA001", 30, 0.5)
    assert analyzer.analyzer_id == "TA001"
    assert analyzer.trend_period_days == 30


