"""Класс спутника"""
from typing import Optional, List, TYPE_CHECKING
from exceptions.weather_exceptions import SatelliteException

if TYPE_CHECKING:
    from locations.location import Location
    from data.weather_data import WeatherData
    from stations.weather_station import WeatherStation


class Satellite:
    """Спутник для наблюдения за погодой"""
    
    def __init__(self, satellite_id: str, name: str, orbit_type: str, altitude: float):
        if not isinstance(satellite_id, str) or not satellite_id:
            raise ValueError("ID спутника должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(orbit_type, str):
            raise TypeError("Тип орбиты должен быть строкой")
        if not isinstance(altitude, (int, float)) or altitude < 0:
            raise ValueError("Высота должна быть неотрицательной")
        
        self.satellite_id = satellite_id
        self.name = name
        self.orbit_type = orbit_type
        self.altitude = altitude
        self.__covered_locations: List['Location'] = []
        self.instrument_types: List[str] = []
        self.is_operational = True
        self.launch_date: Optional[str] = None
    
    def add_location(self, location: 'Location') -> None:
        """Добавить локацию покрытия"""
        if location not in self.__covered_locations:
            self.__covered_locations.append(location)
    
    def add_instrument(self, instrument: str) -> None:
        """Добавить инструмент"""
        if not isinstance(instrument, str):
            raise TypeError("Инструмент должен быть строкой")
        if instrument not in self.instrument_types:
            self.instrument_types.append(instrument)
    
    def get_locations(self) -> List['Location']:
        """Получить локации"""
        return self.__covered_locations.copy()
    
    def provides_data_for(self, weather_data: 'WeatherData') -> None:
        """Предоставляет данные для (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        if not self.is_operational:
            raise ValueError("Спутник не работает")
        # Спутник предоставляет данные
    
    def supports_station(self, station: 'WeatherStation') -> None:
        """Поддерживает станцию (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if not self.is_operational:
            raise ValueError("Спутник не работает")
        # Спутник поддерживает станцию
    
    def covers_location(self, location: 'Location') -> None:
        """Покрывает локацию (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        self.add_location(location)
    
    locations = property(get_locations)


