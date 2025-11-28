"""Класс региона"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from locations.location import Location
    from locations.city import City
    from data.climate_data import ClimateData


class Region:
    """Регион"""
    
    def __init__(self, region_id: str, name: str, country: str, area_km2: float):
        if not isinstance(region_id, str) or not region_id:
            raise ValueError("ID региона должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(country, str):
            raise TypeError("Страна должна быть строкой")
        if not isinstance(area_km2, (int, float)) or area_km2 < 0:
            raise ValueError("Площадь должна быть неотрицательной")
        
        self.region_id = region_id
        self.name = name
        self.country = country
        self.area_km2 = area_km2
        self.__cities: List['City'] = []
        self.climate_zone: Optional[str] = None
        self.average_elevation: Optional[float] = None
    
    def add_city(self, city: 'City') -> None:
        """Добавить город"""
        if city not in self.__cities:
            self.__cities.append(city)
    
    def get_cities(self) -> List['City']:
        """Получить города"""
        return self.__cities.copy()
    
    def contains_location(self, location: 'Location') -> None:
        """Содержит локацию (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        if location.region != self.name:
            raise ValueError("Локация не принадлежит региону")
    
    def contains_city(self, city: 'City') -> None:
        """Содержит город (ассоциация с City)"""
        if city is None:
            raise ValueError("Город не может быть None")
        if city.country != self.country:
            raise ValueError("Город не принадлежит стране региона")
        self.add_city(city)
    
    def has_climate_data(self, climate_data: 'ClimateData') -> None:
        """Имеет климатические данные (ассоциация с ClimateData)"""
        if climate_data is None:
            raise ValueError("Климатические данные не могут быть None")
        if climate_data.region_name != self.name:
            climate_data.region_name = self.name
    
    cities = property(get_cities)


