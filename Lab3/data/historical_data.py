"""Класс исторических данных"""
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime, date
from exceptions.weather_exceptions import DataValidationException

if TYPE_CHECKING:
    from data.weather_data import WeatherData
    from locations.location import Location


class HistoricalData:
    """Исторические данные о погоде"""
    
    def __init__(self, location_name: str, start_date: date, end_date: date):
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        if not isinstance(start_date, date):
            raise TypeError("Дата начала должна быть date")
        if not isinstance(end_date, date):
            raise TypeError("Дата конца должна быть date")
        if start_date > end_date:
            raise ValueError("Дата начала должна быть раньше даты конца")
        
        self.location_name = location_name
        self.start_date = start_date
        self.end_date = end_date
        self.__data_points: List['WeatherData'] = []
        self.data_count = 0
        self.average_temperature: Optional[float] = None
        self.average_humidity: Optional[float] = None
    
    def add_data_point(self, weather_data: 'WeatherData') -> None:
        """Добавить точку данных"""
        if not isinstance(weather_data, type(self).__module__):
            raise TypeError("Данные должны быть WeatherData")
        self.__data_points.append(weather_data)
        self.data_count = len(self.__data_points)
    
    def calculate_averages(self) -> None:
        """Рассчитать средние значения"""
        if not self.__data_points:
            raise DataValidationException("Нет данных для расчета")
        temps = [d.temperature for d in self.__data_points if d.temperature is not None]
        hums = [d.humidity for d in self.__data_points if d.humidity is not None]
        if temps:
            self.average_temperature = sum(temps) / len(temps)
        if hums:
            self.average_humidity = sum(hums) / len(hums)
    
    def get_data_points(self) -> List['WeatherData']:
        """Получить точки данных"""
        return self.__data_points.copy()
    
    def from_location(self, location: 'Location') -> None:
        """От локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        if self.location_name != location.name:
            self.location_name = location.name
    
    def contains_weather_data(self, weather_data: 'WeatherData') -> None:
        """Содержит данные о погоде (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        if weather_data not in self.__data_points:
            self.add_data_point(weather_data)
    
    data_points = property(get_data_points)

