"""Класс оповещения о шторме"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import AlertException

if TYPE_CHECKING:
    from alerts.weather_alert import WeatherAlert
    from locations.location import Location


class StormAlert:
    """Оповещение о шторме"""
    
    def __init__(self, alert_id: str, storm_type: str, wind_speed: float, location_name: str):
        if not isinstance(alert_id, str) or not alert_id:
            raise ValueError("ID оповещения должен быть непустой строкой")
        if not isinstance(storm_type, str):
            raise TypeError("Тип шторма должен быть строкой")
        if not isinstance(wind_speed, (int, float)) or wind_speed < 0:
            raise ValueError("Скорость ветра должна быть неотрицательной")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        
        self.alert_id = alert_id
        self.storm_type = storm_type
        self.wind_speed = wind_speed
        self.location_name = location_name
        self.expected_duration: Optional[int] = None
        self.affected_area: Optional[float] = None
        self.issued_at = datetime.now()
    
    def set_duration(self, hours: int) -> None:
        """Установить продолжительность"""
        if not isinstance(hours, int) or hours < 0:
            raise ValueError("Продолжительность должна быть неотрицательной")
        self.expected_duration = hours
    
    def set_affected_area(self, area: float) -> None:
        """Установить затронутую площадь"""
        if not isinstance(area, (int, float)) or area < 0:
            raise ValueError("Площадь должна быть неотрицательной")
        self.affected_area = area
    
    def extends_weather_alert(self, alert: 'WeatherAlert') -> None:
        """Расширяет оповещение о погоде (ассоциация с WeatherAlert)"""
        if alert is None:
            raise ValueError("Оповещение не может быть None")
        if alert.location_name != self.location_name:
            self.location_name = alert.location_name
    
    def for_location(self, location: 'Location') -> None:
        """Для локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        self.location_name = location.name


