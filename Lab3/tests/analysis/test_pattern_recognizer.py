"""Тесты для PatternRecognizer"""
from analysis.pattern_recognizer import PatternRecognizer


def test_pattern_recognizer_init():
    recognizer = PatternRecognizer("PR001", ["Cyclical", "Seasonal"], 90.0)
    assert recognizer.recognizer_id == "PR001"
    assert recognizer.recognition_accuracy == 90.0


