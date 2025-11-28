"""Класс статистической модели"""
from typing import Optional, List, TYPE_CHECKING
from exceptions.weather_exceptions import ModelException

if TYPE_CHECKING:
    from models.weather_model import WeatherModel
    from data.historical_data import HistoricalData


class StatisticalModel:
    """Статистическая модель прогноза"""
    
    def __init__(self, model_id: str, algorithm: str, confidence_level: float, sample_size: int):
        if not isinstance(model_id, str) or not model_id:
            raise ValueError("ID модели должен быть непустой строкой")
        if not isinstance(algorithm, str):
            raise TypeError("Алгоритм должен быть строкой")
        if not isinstance(confidence_level, (int, float)) or confidence_level < 0 or confidence_level > 100:
            raise ValueError("Уровень уверенности должен быть от 0 до 100")
        if not isinstance(sample_size, int) or sample_size < 0:
            raise ValueError("Размер выборки должен быть неотрицательным")
        
        self.model_id = model_id
        self.algorithm = algorithm
        self.confidence_level = confidence_level
        self.sample_size = sample_size
        self.statistical_measures: List[str] = []
        self.correlation_coefficient: Optional[float] = None
        self.p_value: Optional[float] = None
    
    def add_statistical_measure(self, measure: str) -> None:
        """Добавить статистическую меру"""
        if not isinstance(measure, str):
            raise TypeError("Мера должна быть строкой")
        if measure not in self.statistical_measures:
            self.statistical_measures.append(measure)
    
    def set_correlation(self, coefficient: float) -> None:
        """Установить коэффициент корреляции"""
        if not isinstance(coefficient, (int, float)) or coefficient < -1 or coefficient > 1:
            raise ModelException("Коэффициент корреляции должен быть от -1 до 1")
        self.correlation_coefficient = coefficient
    
    def extends_weather_model(self, model: 'WeatherModel') -> None:
        """Расширяет модель погоды (ассоциация с WeatherModel)"""
        if model is None:
            raise ValueError("Модель погоды не может быть None")
        if not model.is_active:
            raise ValueError("Модель неактивна")
        # Статистическая модель расширяет базовую модель
    
    def uses_historical_data(self, historical_data: 'HistoricalData') -> None:
        """Использует исторические данные (ассоциация с HistoricalData)"""
        if historical_data is None:
            raise ValueError("Исторические данные не могут быть None")
        if historical_data.data_count < self.sample_size:
            raise ValueError("Недостаточно данных для статистической модели")
        historical_data.calculate_averages()


