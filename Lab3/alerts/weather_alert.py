"""Класс оповещения о погоде"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import AlertException

if TYPE_CHECKING:
    from locations.location import Location
    from forecasts.forecast import Forecast


class WeatherAlert:
    """Оповещение о погоде"""
    
    def __init__(self, alert_id: str, alert_type: str, severity: str, location_name: str):
        if not isinstance(alert_id, str) or not alert_id:
            raise ValueError("ID оповещения должен быть непустой строкой")
        if not isinstance(alert_type, str):
            raise TypeError("Тип оповещения должен быть строкой")
        if not isinstance(severity, str):
            raise TypeError("Серьезность должна быть строкой")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.severity = severity
        self.location_name = location_name
        self.issued_at = datetime.now()
        self.expires_at: Optional[datetime] = None
        self.message: Optional[str] = None
        self.is_active = True
    
    def set_expiration(self, expires_at: datetime) -> None:
        """Установить срок действия"""
        if not isinstance(expires_at, datetime):
            raise TypeError("Срок действия должен быть datetime")
        self.expires_at = expires_at
    
    def set_message(self, message: str) -> None:
        """Установить сообщение"""
        if not isinstance(message, str):
            raise TypeError("Сообщение должно быть строкой")
        self.message = message
    
    def for_location(self, location: 'Location') -> None:
        """Для локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        self.location_name = location.name
    
    def based_on_forecast(self, forecast: 'Forecast') -> None:
        """На основе прогноза (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        if forecast.location_name != self.location_name:
            self.location_name = forecast.location_name
        if self.message is None:
            self.message = f"Оповещение на основе прогноза для {forecast.location_name}"


