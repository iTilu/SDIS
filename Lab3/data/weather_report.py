"""Класс отчета о погоде"""
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import DataValidationException

if TYPE_CHECKING:
    from data.weather_data import WeatherData
    from forecasts.forecast import Forecast
    from locations.location import Location


class WeatherReport:
    """Отчет о погоде"""
    
    def __init__(self, report_id: str, title: str, created_at: datetime, author: str):
        if not isinstance(report_id, str) or not report_id:
            raise ValueError("ID отчета должен быть непустой строкой")
        if not isinstance(title, str) or not title:
            raise ValueError("Заголовок должен быть непустой строкой")
        if not isinstance(created_at, datetime):
            raise TypeError("Дата создания должна быть datetime")
        if not isinstance(author, str) or not author:
            raise ValueError("Автор должен быть непустой строкой")
        
        self.report_id = report_id
        self.title = title
        self.created_at = created_at
        self.author = author
        self.__weather_data_sources: List['WeatherData'] = []
        self.summary: Optional[str] = None
        self.report_type = "standard"
        self.page_count = 0
    
    def add_weather_data(self, weather_data: 'WeatherData') -> None:
        """Добавить данные о погоде"""
        if weather_data not in self.__weather_data_sources:
            self.__weather_data_sources.append(weather_data)
    
    def get_weather_data_sources(self) -> List['WeatherData']:
        """Получить источники данных"""
        return self.__weather_data_sources.copy()
    
    def set_summary(self, summary: str) -> None:
        """Установить сводку"""
        if not isinstance(summary, str):
            raise TypeError("Сводка должна быть строкой")
        self.summary = summary
    
    def includes_weather_data(self, weather_data: 'WeatherData') -> None:
        """Включает данные о погоде (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        self.add_weather_data(weather_data)
    
    def references_forecast(self, forecast: 'Forecast') -> None:
        """Ссылается на прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        if self.summary is None:
            self.summary = f"Отчет ссылается на прогноз для {forecast.location_name}"
    
    def for_location(self, location: 'Location') -> None:
        """Для локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        if self.summary is None:
            self.summary = f"Отчет для локации {location.name}"
    
    weather_data_sources = property(get_weather_data_sources)


