"""Класс дневного прогноза"""
from typing import Optional, TYPE_CHECKING
from datetime import date
from exceptions.weather_exceptions import InvalidForecastDataException

if TYPE_CHECKING:
    from forecasts.forecast import Forecast
    from forecasts.hourly_forecast import HourlyForecast
    from locations.location import Location


class DailyForecast:
    """Дневной прогноз"""
    
    def __init__(self, forecast_id: str, location_name: str, forecast_date: date, high_temp: float, low_temp: float):
        if not isinstance(forecast_id, str) or not forecast_id:
            raise ValueError("ID прогноза должен быть непустой строкой")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        if not isinstance(forecast_date, date):
            raise TypeError("Дата прогноза должна быть date")
        if not isinstance(high_temp, (int, float)) or not isinstance(low_temp, (int, float)):
            raise TypeError("Температуры должны быть числами")
        if high_temp < low_temp:
            raise InvalidForecastDataException("Максимальная температура должна быть выше минимальной")
        
        self.forecast_id = forecast_id
        self.location_name = location_name
        self.forecast_date = forecast_date
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.sunrise_time: Optional[str] = None
        self.sunset_time: Optional[str] = None
        self.day_condition: Optional[str] = None
        self.night_condition: Optional[str] = None
    
    def set_sun_times(self, sunrise: str, sunset: str) -> None:
        """Установить время восхода и заката"""
        if not isinstance(sunrise, str) or not isinstance(sunset, str):
            raise TypeError("Время должно быть строкой")
        self.sunrise_time = sunrise
        self.sunset_time = sunset
    
    def set_day_condition(self, condition: str) -> None:
        """Установить дневное условие"""
        if not isinstance(condition, str):
            raise TypeError("Условие должно быть строкой")
        self.day_condition = condition
    
    def set_night_condition(self, condition: str) -> None:
        """Установить ночное условие"""
        if not isinstance(condition, str):
            raise TypeError("Условие должно быть строкой")
        self.night_condition = condition
    
    def part_of_forecast(self, forecast: 'Forecast') -> None:
        """Часть прогноза (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        if forecast.location_name != self.location_name:
            self.location_name = forecast.location_name
    
    def contains_hourly(self, hourly_forecast: 'HourlyForecast') -> None:
        """Содержит почасовой прогноз (ассоциация с HourlyForecast)"""
        if hourly_forecast is None:
            raise ValueError("Почасовой прогноз не может быть None")
        if hourly_forecast.location_name != self.location_name:
            hourly_forecast.location_name = self.location_name
    
    def for_location(self, location: 'Location') -> None:
        """Для локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        self.location_name = location.name


