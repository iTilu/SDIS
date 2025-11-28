"""Класс прогнозиста"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from forecasts.forecast import Forecast
    from forecasts.short_term_forecast import ShortTermForecast
    from models.weather_model import WeatherModel


class Forecaster:
    """Прогнозист погоды"""
    
    def __init__(self, employee_id: str, name: str, forecast_type: str, accuracy_rate: float):
        if not isinstance(employee_id, str) or not employee_id:
            raise ValueError("ID сотрудника должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(forecast_type, str):
            raise TypeError("Тип прогноза должен быть строкой")
        if not isinstance(accuracy_rate, (int, float)) or accuracy_rate < 0 or accuracy_rate > 100:
            raise ValueError("Точность должна быть от 0 до 100")
        
        self.employee_id = employee_id
        self.name = name
        self.forecast_type = forecast_type
        self.accuracy_rate = accuracy_rate
        self.__forecasts: List['Forecast'] = []
        self.forecast_count = 0
        self.shift = "day"
    
    def add_forecast(self, forecast: 'Forecast') -> None:
        """Добавить прогноз"""
        if forecast not in self.__forecasts:
            self.__forecasts.append(forecast)
            self.forecast_count = len(self.__forecasts)
    
    def get_forecasts(self) -> List['Forecast']:
        """Получить прогнозы"""
        return self.__forecasts.copy()
    
    def creates_forecast(self, forecast: 'Forecast') -> None:
        """Создает прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        self.add_forecast(forecast)
    
    def creates_short_term(self, short_term: 'ShortTermForecast') -> None:
        """Создает краткосрочный прогноз (ассоциация с ShortTermForecast)"""
        if short_term is None:
            raise ValueError("Краткосрочный прогноз не может быть None")
        # Прогнозист создает краткосрочный прогноз
    
    def uses_model(self, model: 'WeatherModel') -> None:
        """Использует модель (ассоциация с WeatherModel)"""
        if model is None:
            raise ValueError("Модель не может быть None")
        if not model.is_active:
            raise ValueError("Модель неактивна")
    
    forecasts = property(get_forecasts)


