"""Тесты для NumericalModel"""
from models.numerical_model import NumericalModel


def test_numerical_model_init():
    model = NumericalModel("NM001", 0.25, 1000, 0.1)
    assert model.model_id == "NM001"
    assert model.resolution == 0.25


