"""Класс координат"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from locations.location import Location
    from locations.city import City


class Coordinates:
    """Географические координаты"""
    
    def __init__(self, latitude: float, longitude: float):
        if not isinstance(latitude, (int, float)) or latitude < -90 or latitude > 90:
            raise ValueError("Широта должна быть от -90 до 90")
        if not isinstance(longitude, (int, float)) or longitude < -180 or longitude > 180:
            raise ValueError("Долгота должна быть от -180 до 180")
        
        self.latitude = latitude
        self.longitude = longitude
        self.altitude: Optional[float] = None
    
    def set_altitude(self, altitude: float) -> None:
        """Установить высоту"""
        if not isinstance(altitude, (int, float)):
            raise TypeError("Высота должна быть числом")
        self.altitude = altitude
    
    def for_location(self, location: 'Location') -> None:
        """Для локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        # Координаты для локации
    
    def for_city(self, city: 'City') -> None:
        """Для города (ассоциация с City)"""
        if city is None:
            raise ValueError("Город не может быть None")
        # Координаты для города

