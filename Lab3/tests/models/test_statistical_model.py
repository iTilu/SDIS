"""Тесты для StatisticalModel"""
from models.statistical_model import StatisticalModel


def test_statistical_model_init():
    model = StatisticalModel("SM001", "ARIMA", 95.0, 1000)
    assert model.model_id == "SM001"
    assert model.algorithm == "ARIMA"


