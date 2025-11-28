"""Класс точки данных"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import DataValidationException

if TYPE_CHECKING:
    from data.weather_data import WeatherData
    from data.historical_data import HistoricalData


class DataPoint:
    """Точка данных"""
    
    def __init__(self, point_id: str, timestamp: datetime, value: float):
        if not isinstance(point_id, str) or not point_id:
            raise ValueError("ID точки должен быть непустой строкой")
        if not isinstance(timestamp, datetime):
            raise TypeError("Временная метка должна быть datetime")
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        
        self.point_id = point_id
        self.timestamp = timestamp
        self.value = value
        self.parameter_name: Optional[str] = None
        self.unit: Optional[str] = None
        self.is_outlier = False
    
    def set_parameter(self, name: str, unit: str) -> None:
        """Установить параметр"""
        if not isinstance(name, str):
            raise TypeError("Название параметра должно быть строкой")
        if not isinstance(unit, str):
            raise TypeError("Единица измерения должна быть строкой")
        self.parameter_name = name
        self.unit = unit
    
    def mark_as_outlier(self) -> None:
        """Пометить как выброс"""
        self.is_outlier = True
    
    def validate(self) -> bool:
        """Валидировать точку данных"""
        if self.value is None:
            raise DataValidationException("Значение точки данных отсутствует")
        return True
    
    def part_of_weather_data(self, weather_data: 'WeatherData') -> None:
        """Часть данных о погоде (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        if self.parameter_name == "temperature":
            weather_data.temperature = self.value
        elif self.parameter_name == "humidity":
            weather_data.humidity = self.value
    
    def part_of_historical(self, historical_data: 'HistoricalData') -> None:
        """Часть исторических данных (ассоциация с HistoricalData)"""
        if historical_data is None:
            raise ValueError("Исторические данные не могут быть None")
        # Точка данных может быть частью исторических данных


