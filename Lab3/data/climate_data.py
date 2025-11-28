"""Класс климатических данных"""
from typing import Optional, List, TYPE_CHECKING
from datetime import date
from exceptions.weather_exceptions import ClimateDataException

if TYPE_CHECKING:
    from locations.location import Location
    from data.historical_data import HistoricalData


class ClimateData:
    """Климатические данные"""
    
    def __init__(self, region_name: str, climate_zone: str, average_temp: float):
        if not isinstance(region_name, str) or not region_name:
            raise ValueError("Название региона должно быть непустой строкой")
        if not isinstance(climate_zone, str):
            raise TypeError("Климатическая зона должна быть строкой")
        if not isinstance(average_temp, (int, float)):
            raise TypeError("Средняя температура должна быть числом")
        
        self.region_name = region_name
        self.climate_zone = climate_zone
        self.average_temp = average_temp
        self.annual_precipitation: Optional[float] = None
        self.seasonal_variations: List[str] = []
        self.extreme_events: List[str] = []
        self.data_period_years = 0
    
    def add_precipitation(self, precipitation: float) -> None:
        """Добавить осадки"""
        if not isinstance(precipitation, (int, float)) or precipitation < 0:
            raise ValueError("Осадки должны быть неотрицательными")
        self.annual_precipitation = precipitation
    
    def add_seasonal_variation(self, season: str) -> None:
        """Добавить сезонное изменение"""
        if not isinstance(season, str):
            raise TypeError("Сезон должен быть строкой")
        if season not in self.seasonal_variations:
            self.seasonal_variations.append(season)
    
    def add_extreme_event(self, event: str) -> None:
        """Добавить экстремальное событие"""
        if not isinstance(event, str):
            raise TypeError("Событие должно быть строкой")
        if event not in self.extreme_events:
            self.extreme_events.append(event)
    
    def set_data_period(self, years: int) -> None:
        """Установить период данных"""
        if not isinstance(years, int) or years < 0:
            raise ValueError("Количество лет должно быть неотрицательным")
        self.data_period_years = years
    
    def from_location(self, location: 'Location') -> None:
        """От локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        if self.region_name != location.region:
            self.region_name = location.region
    
    def based_on_historical(self, historical_data: 'HistoricalData') -> None:
        """На основе исторических данных (ассоциация с HistoricalData)"""
        if historical_data is None:
            raise ValueError("Исторические данные не могут быть None")
        if historical_data.average_temperature is not None:
            self.average_temp = historical_data.average_temperature
    
    def get_climate_summary(self) -> str:
        """Получить сводку климата"""
        return f"{self.region_name}: {self.climate_zone}, Avg Temp: {self.average_temp}°C"


