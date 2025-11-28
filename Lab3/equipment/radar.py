"""Класс радара"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import RadarException

if TYPE_CHECKING:
    from locations.location import Location
    from data.weather_data import WeatherData
    from stations.weather_station import WeatherStation


class Radar:
    """Радар для наблюдения за погодой"""
    
    def __init__(self, radar_id: str, location_name: str, range_km: float, frequency: float):
        if not isinstance(radar_id, str) or not radar_id:
            raise ValueError("ID радара должен быть непустой строкой")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        if not isinstance(range_km, (int, float)) or range_km < 0:
            raise ValueError("Дальность должна быть неотрицательной")
        if not isinstance(frequency, (int, float)) or frequency < 0:
            raise ValueError("Частота должна быть неотрицательной")
        
        self.radar_id = radar_id
        self.location_name = location_name
        self.range_km = range_km
        self.frequency = frequency
        self.scan_angle: Optional[float] = None
        self.is_operational = True
        self.last_maintenance: Optional[str] = None
        self.power_level = 100.0
    
    def set_scan_angle(self, angle: float) -> None:
        """Установить угол сканирования"""
        if not isinstance(angle, (int, float)) or angle < 0 or angle > 360:
            raise ValueError("Угол должен быть от 0 до 360")
        self.scan_angle = angle
    
    def get_power_level(self) -> float:
        """Получить уровень мощности"""
        return self.power_level
    
    def located_at(self, location: 'Location') -> None:
        """Расположен в (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        self.location_name = location.name
    
    def generates_data(self, weather_data: 'WeatherData') -> None:
        """Генерирует данные (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        if not self.is_operational:
            raise ValueError("Радар не работает")
        # Радар генерирует данные
    
    def supports_station(self, station: 'WeatherStation') -> None:
        """Поддерживает станцию (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if not self.is_operational:
            raise ValueError("Радар не работает")


