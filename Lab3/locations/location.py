"""Класс локации"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from locations.coordinates import Coordinates
    from stations.weather_station import WeatherStation
    from forecasts.forecast import Forecast
    from data.weather_data import WeatherData


class Location:
    """Локация для прогноза погоды"""
    
    def __init__(self, location_id: str, name: str, country: str, region: str):
        if not isinstance(location_id, str) or not location_id:
            raise ValueError("ID локации должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(country, str):
            raise TypeError("Страна должна быть строкой")
        if not isinstance(region, str):
            raise TypeError("Регион должен быть строкой")
        
        self.location_id = location_id
        self.name = name
        self.country = country
        self.region = region
        self.timezone: Optional[str] = None
        self.population: Optional[int] = None
        self.area_km2: Optional[float] = None
    
    def set_timezone(self, timezone: str) -> None:
        """Установить часовой пояс"""
        if not isinstance(timezone, str):
            raise TypeError("Часовой пояс должен быть строкой")
        self.timezone = timezone
    
    def set_population(self, population: int) -> None:
        """Установить население"""
        if not isinstance(population, int) or population < 0:
            raise ValueError("Население должно быть неотрицательным")
        self.population = population
    
    def has_coordinates(self, coordinates: 'Coordinates') -> None:
        """Имеет координаты (ассоциация с Coordinates)"""
        if coordinates is None:
            raise ValueError("Координаты не могут быть None")
        # Локация имеет координаты
    
    def contains_station(self, station: 'WeatherStation') -> None:
        """Содержит станцию (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if station.name != self.name:
            raise ValueError("Станция не соответствует локации")
    
    def has_forecast(self, forecast: 'Forecast') -> None:
        """Имеет прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        if forecast.location_name != self.name:
            forecast.location_name = self.name
    
    def receives_data(self, weather_data: 'WeatherData') -> None:
        """Получает данные (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        # Локация получает данные


