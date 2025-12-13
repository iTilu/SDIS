"""Класс оповещения о ветре"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import AlertException

if TYPE_CHECKING:
    from alerts.weather_alert import WeatherAlert
    from locations.location import Location


class WindAlert:
    """Оповещение о ветре"""
    
    def __init__(self, alert_id: str, wind_speed: float, wind_direction: int, location_name: str):
        if not isinstance(alert_id, str) or not alert_id:
            raise ValueError("ID оповещения должен быть непустой строкой")
        if not isinstance(wind_speed, (int, float)) or wind_speed < 0:
            raise ValueError("Скорость ветра должна быть неотрицательной")
        if not isinstance(wind_direction, int) or wind_direction < 0 or wind_direction > 360:
            raise ValueError("Направление должно быть от 0 до 360")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        
        self.alert_id = alert_id
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.location_name = location_name
        self.gust_speed: Optional[float] = None
        self.issued_at = datetime.now()
        self.warning_level = "advisory"
        self._update_warning_level()
    
    def set_gust_speed(self, gust: float) -> None:
        """Установить скорость порывов"""
        if not isinstance(gust, (int, float)) or gust < 0:
            raise ValueError("Скорость порывов должна быть неотрицательной")
        self.gust_speed = gust
        self._update_warning_level()
    
    def _update_warning_level(self) -> None:
        """Обновить уровень предупреждения"""
        if self.wind_speed < 25:
            self.warning_level = "advisory"
        elif self.wind_speed < 40:
            self.warning_level = "watch"
        else:
            self.warning_level = "warning"
    
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


