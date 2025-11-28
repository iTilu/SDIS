"""Класс почасового прогноза"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import InvalidForecastDataException

if TYPE_CHECKING:
    from forecasts.forecast import Forecast
    from locations.location import Location


class HourlyForecast:
    """Почасовой прогноз"""
    
    def __init__(self, forecast_id: str, location_name: str, hour: int, temperature: float):
        if not isinstance(forecast_id, str) or not forecast_id:
            raise ValueError("ID прогноза должен быть непустой строкой")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        if not isinstance(hour, int) or hour < 0 or hour > 23:
            raise ValueError("Час должен быть от 0 до 23")
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")
        
        self.forecast_id = forecast_id
        self.location_name = location_name
        self.hour = hour
        self.temperature = temperature
        self.feels_like: Optional[float] = None
        self.humidity: Optional[float] = None
        self.precipitation_chance: Optional[float] = None
        self.wind_gust: Optional[float] = None
    
    def set_feels_like(self, feels_like: float) -> None:
        """Установить ощущаемую температуру"""
        if not isinstance(feels_like, (int, float)):
            raise TypeError("Ощущаемая температура должна быть числом")
        self.feels_like = feels_like
    
    def set_humidity(self, humidity: float) -> None:
        """Установить влажность"""
        if not isinstance(humidity, (int, float)) or humidity < 0 or humidity > 100:
            raise InvalidForecastDataException("Влажность должна быть от 0 до 100")
        self.humidity = humidity
    
    def set_precipitation_chance(self, chance: float) -> None:
        """Установить вероятность осадков"""
        if not isinstance(chance, (int, float)) or chance < 0 or chance > 100:
            raise InvalidForecastDataException("Вероятность должна быть от 0 до 100")
        self.precipitation_chance = chance
    
    def part_of_forecast(self, forecast: 'Forecast') -> None:
        """Часть прогноза (ассоциация с Forecast)"""
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


