"""Тесты для DataProcessor"""
from analysis.data_processor import DataProcessor


def test_data_processor_init():
    processor = DataProcessor("DP001", "Filtering", "JSON")
    assert processor.processor_id == "DP001"
    assert processor.output_format == "JSON"


