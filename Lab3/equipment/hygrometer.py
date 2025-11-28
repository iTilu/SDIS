"""Класс гигрометра"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from sensors.humidity_sensor import HumiditySensor
    from stations.weather_station import WeatherStation


class Hygrometer:
    """Гигрометр для измерения влажности"""
    
    def __init__(self, device_id: str, humidity_range: float, sensitivity: float, technology: str):
        if not isinstance(device_id, str) or not device_id:
            raise ValueError("ID устройства должен быть непустой строкой")
        if not isinstance(humidity_range, (int, float)) or humidity_range < 0 or humidity_range > 100:
            raise ValueError("Диапазон влажности должен быть от 0 до 100")
        if not isinstance(sensitivity, (int, float)) or sensitivity < 0:
            raise ValueError("Чувствительность должна быть неотрицательной")
        if not isinstance(technology, str):
            raise TypeError("Технология должна быть строкой")
        
        self.device_id = device_id
        self.humidity_range = humidity_range
        self.sensitivity = sensitivity
        self.technology = technology
        self.current_humidity: Optional[float] = None
        self.is_functional = True
        self.response_time: Optional[float] = None
    
    def set_humidity(self, humidity: float) -> None:
        """Установить влажность"""
        if not isinstance(humidity, (int, float)) or humidity < 0 or humidity > 100:
            raise ValueError("Влажность должна быть от 0 до 100")
        self.current_humidity = humidity
    
    def set_response_time(self, time: float) -> None:
        """Установить время отклика"""
        if not isinstance(time, (int, float)) or time < 0:
            raise ValueError("Время должно быть неотрицательным")
        self.response_time = time
    
    def used_by_sensor(self, sensor: 'HumiditySensor') -> None:
        """Используется сенсором (ассоциация с HumiditySensor)"""
        if sensor is None:
            raise ValueError("Сенсор не может быть None")
        if not self.is_functional:
            raise ValueError("Гигрометр не работает")
        if sensor.current_humidity is not None:
            self.set_humidity(sensor.current_humidity)
    
    def installed_at_station(self, station: 'WeatherStation') -> None:
        """Установлен на станции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if not self.is_functional:
            raise ValueError("Гигрометр не работает")


