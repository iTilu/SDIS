"""Класс долгосрочного прогноза"""
from typing import Optional, List, TYPE_CHECKING
from datetime import date
from exceptions.weather_exceptions import InvalidForecastDataException

if TYPE_CHECKING:
    from forecasts.forecast import Forecast
    from locations.location import Location
    from models.weather_model import WeatherModel


class LongTermForecast:
    """Долгосрочный прогноз (более 48 часов)"""
    
    def __init__(self, forecast_id: str, location_name: str, days_ahead: int, avg_temperature: float):
        if not isinstance(forecast_id, str) or not forecast_id:
            raise ValueError("ID прогноза должен быть непустой строкой")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        if not isinstance(days_ahead, int) or days_ahead < 3:
            raise ValueError("Дней вперед должно быть не менее 3")
        if not isinstance(avg_temperature, (int, float)):
            raise TypeError("Средняя температура должна быть числом")
        
        self.forecast_id = forecast_id
        self.location_name = location_name
        self.days_ahead = days_ahead
        self.avg_temperature = avg_temperature
        self.temperature_range: Optional[str] = None
        self.precipitation_outlook: Optional[str] = None
        self.trend_indicators: List[str] = []
        self.confidence_level: Optional[float] = None
    
    def set_temperature_range(self, min_temp: float, max_temp: float) -> None:
        """Установить диапазон температур"""
        if not isinstance(min_temp, (int, float)) or not isinstance(max_temp, (int, float)):
            raise TypeError("Температуры должны быть числами")
        self.temperature_range = f"{min_temp}-{max_temp}"
    
    def set_precipitation_outlook(self, outlook: str) -> None:
        """Установить прогноз осадков"""
        if not isinstance(outlook, str):
            raise TypeError("Прогноз должен быть строкой")
        self.precipitation_outlook = outlook
    
    def add_trend_indicator(self, indicator: str) -> None:
        """Добавить индикатор тренда"""
        if not isinstance(indicator, str):
            raise TypeError("Индикатор должен быть строкой")
        if indicator not in self.trend_indicators:
            self.trend_indicators.append(indicator)
    
    def set_confidence(self, level: float) -> None:
        """Установить уровень уверенности"""
        if not isinstance(level, (int, float)) or level < 0 or level > 100:
            raise InvalidForecastDataException("Уровень уверенности должен быть от 0 до 100")
        self.confidence_level = level
    
    def extends_forecast(self, forecast: 'Forecast') -> None:
        """Расширяет прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        if forecast.location_name != self.location_name:
            self.location_name = forecast.location_name
        if forecast.temperature is not None:
            self.avg_temperature = forecast.temperature
    
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


