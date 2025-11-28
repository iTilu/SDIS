"""Класс краткосрочного прогноза"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime, date
from exceptions.weather_exceptions import InvalidForecastDataException

if TYPE_CHECKING:
    from forecasts.forecast import Forecast
    from locations.location import Location
    from models.weather_model import WeatherModel


class ShortTermForecast:
    """Краткосрочный прогноз (до 48 часов)"""
    
    def __init__(self, forecast_id: str, location_name: str, hours_ahead: int, temperature: float):
        if not isinstance(forecast_id, str) or not forecast_id:
            raise ValueError("ID прогноза должен быть непустой строкой")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        if not isinstance(hours_ahead, int) or hours_ahead < 0 or hours_ahead > 48:
            raise ValueError("Часов вперед должно быть от 0 до 48")
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")
        
        self.forecast_id = forecast_id
        self.location_name = location_name
        self.hours_ahead = hours_ahead
        self.temperature = temperature
        self.weather_condition: Optional[str] = None
        self.cloud_cover: Optional[float] = None
        self.visibility: Optional[float] = None
        self.update_frequency = "hourly"
    
    def set_weather_condition(self, condition: str) -> None:
        """Установить погодное условие"""
        if not isinstance(condition, str):
            raise TypeError("Условие должно быть строкой")
        self.weather_condition = condition
    
    def set_cloud_cover(self, cover: float) -> None:
        """Установить облачность"""
        if not isinstance(cover, (int, float)) or cover < 0 or cover > 100:
            raise InvalidForecastDataException("Облачность должна быть от 0 до 100")
        self.cloud_cover = cover
    
    def extends_forecast(self, forecast: 'Forecast') -> None:
        """Расширяет прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        if forecast.location_name != self.location_name:
            self.location_name = forecast.location_name
        if forecast.temperature is not None:
            self.temperature = forecast.temperature
    
    def for_location(self, location: 'Location') -> None:
        """Для локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        self.location_name = location.name
    
    def generated_by_model(self, model: 'WeatherModel') -> None:
        """Сгенерирован моделью (ассоциация с WeatherModel)"""
        if model is None:
            raise ValueError("Модель не может быть None")
        if not model.is_active:
            raise ValueError("Модель неактивна")


