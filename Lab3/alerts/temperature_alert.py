"""Класс оповещения о температуре"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import AlertException

if TYPE_CHECKING:
    from alerts.weather_alert import WeatherAlert
    from locations.location import Location


class TemperatureAlert:
    """Оповещение о температуре"""
    
    def __init__(self, alert_id: str, alert_reason: str, temperature: float, threshold: float):
        if not isinstance(alert_id, str) or not alert_id:
            raise ValueError("ID оповещения должен быть непустой строкой")
        if not isinstance(alert_reason, str):
            raise TypeError("Причина должна быть строкой")
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")
        if not isinstance(threshold, (int, float)):
            raise TypeError("Порог должен быть числом")
        
        self.alert_id = alert_id
        self.alert_reason = alert_reason
        self.temperature = temperature
        self.threshold = threshold
        self.duration_hours: Optional[int] = None
        self.issued_at = datetime.now()
        self.alert_level = "moderate"
    
    def set_duration(self, hours: int) -> None:
        """Установить продолжительность"""
        if not isinstance(hours, int) or hours < 0:
            raise ValueError("Продолжительность должна быть неотрицательной")
        self.duration_hours = hours
    
    def update_alert_level(self) -> None:
        """Обновить уровень оповещения"""
        diff = abs(self.temperature - self.threshold)
        if diff < 5:
            self.alert_level = "moderate"
        elif diff < 10:
            self.alert_level = "high"
        else:
            self.alert_level = "extreme"
    
    def extends_weather_alert(self, alert: 'WeatherAlert') -> None:
        """Расширяет оповещение о погоде (ассоциация с WeatherAlert)"""
        if alert is None:
            raise ValueError("Оповещение не может быть None")
        if alert.alert_type != "temperature":
            raise ValueError("Тип оповещения не соответствует")
    
    def for_location(self, location: 'Location') -> None:
        """Для локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        # Оповещение для локации


