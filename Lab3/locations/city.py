"""Класс города"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from locations.location import Location
    from locations.coordinates import Coordinates
    from forecasts.forecast import Forecast


class City:
    """Город"""
    
    def __init__(self, city_id: str, name: str, country: str, population: int):
        if not isinstance(city_id, str) or not city_id:
            raise ValueError("ID города должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(country, str):
            raise TypeError("Страна должна быть строкой")
        if not isinstance(population, int) or population < 0:
            raise ValueError("Население должно быть неотрицательным")
        
        self.city_id = city_id
        self.name = name
        self.country = country
        self.population = population
        self.area_km2: Optional[float] = None
        self.elevation: Optional[float] = None
        self.climate_type: Optional[str] = None
    
    def set_area(self, area: float) -> None:
        """Установить площадь"""
        if not isinstance(area, (int, float)) or area < 0:
            raise ValueError("Площадь должна быть неотрицательной")
        self.area_km2 = area
    
    def set_elevation(self, elevation: float) -> None:
        """Установить высоту"""
        if not isinstance(elevation, (int, float)):
            raise TypeError("Высота должна быть числом")
        self.elevation = elevation
    
    def extends_location(self, location: 'Location') -> None:
        """Расширяет локацию (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        if location.name != self.name:
            self.name = location.name
        if location.country != self.country:
            self.country = location.country
    
    def has_coordinates(self, coordinates: 'Coordinates') -> None:
        """Имеет координаты (ассоциация с Coordinates)"""
        if coordinates is None:
            raise ValueError("Координаты не могут быть None")
        # Город имеет координаты
    
    def has_forecast(self, forecast: 'Forecast') -> None:
        """Имеет прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        if forecast.location_name != self.name:
            forecast.location_name = self.name


