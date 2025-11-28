"""Тесты для AIForecastModel"""
from models.ai_forecast_model import AIForecastModel


def test_ai_forecast_model_init():
    model = AIForecastModel("AI001", "LSTM", 100, 0.001)
    assert model.model_id == "AI001"
    assert model.training_epochs == 100


