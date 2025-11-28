"""Класс AI модели прогноза"""
from typing import Optional, List, TYPE_CHECKING
from exceptions.weather_exceptions import ModelException

if TYPE_CHECKING:
    from models.weather_model import WeatherModel
    from forecasts.forecast import Forecast
    from data.weather_data import WeatherData


class AIForecastModel:
    """AI модель прогноза погоды"""
    
    def __init__(self, model_id: str, model_architecture: str, training_epochs: int, learning_rate: float):
        if not isinstance(model_id, str) or not model_id:
            raise ValueError("ID модели должен быть непустой строкой")
        if not isinstance(model_architecture, str):
            raise TypeError("Архитектура должна быть строкой")
        if not isinstance(training_epochs, int) or training_epochs < 0:
            raise ValueError("Эпохи обучения должны быть неотрицательными")
        if not isinstance(learning_rate, (int, float)) or learning_rate < 0:
            raise ValueError("Скорость обучения должна быть неотрицательной")
        
        self.model_id = model_id
        self.model_architecture = model_architecture
        self.training_epochs = training_epochs
        self.learning_rate = learning_rate
        self.training_loss: Optional[float] = None
        self.validation_accuracy: Optional[float] = None
        self.feature_importance: List[str] = []
    
    def set_training_loss(self, loss: float) -> None:
        """Установить потери обучения"""
        if not isinstance(loss, (int, float)) or loss < 0:
            raise ValueError("Потери должны быть неотрицательными")
        self.training_loss = loss
    
    def set_validation_accuracy(self, accuracy: float) -> None:
        """Установить точность валидации"""
        if not isinstance(accuracy, (int, float)) or accuracy < 0 or accuracy > 100:
            raise ModelException("Точность должна быть от 0 до 100")
        self.validation_accuracy = accuracy
    
    def add_feature_importance(self, feature: str) -> None:
        """Добавить важность признака"""
        if not isinstance(feature, str):
            raise TypeError("Признак должен быть строкой")
        if feature not in self.feature_importance:
            self.feature_importance.append(feature)
    
    def extends_weather_model(self, model: 'WeatherModel') -> None:
        """Расширяет модель погоды (ассоциация с WeatherModel)"""
        if model is None:
            raise ValueError("Модель погоды не может быть None")
        if not model.is_active:
            raise ValueError("Модель неактивна")
        # AI модель расширяет базовую модель
    
    def generates_forecast(self, forecast: 'Forecast') -> None:
        """Генерирует прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        if self.validation_accuracy is None or self.validation_accuracy < 70:
            raise ValueError("Модель недостаточно обучена")
        # AI модель генерирует прогноз
    
    def trained_on_data(self, weather_data: 'WeatherData') -> None:
        """Обучается на данных (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        weather_data.validate_data()
        # Модель обучается на данных


