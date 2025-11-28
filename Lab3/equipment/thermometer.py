"""Класс термометра"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from sensors.temperature_sensor import TemperatureSensor
    from stations.weather_station import WeatherStation


class Thermometer:
    """Термометр для измерения температуры"""
    
    def __init__(self, device_id: str, temp_range_min: float, temp_range_max: float, unit: str):
        if not isinstance(device_id, str) or not device_id:
            raise ValueError("ID устройства должен быть непустой строкой")
        if not isinstance(temp_range_min, (int, float)):
            raise TypeError("Минимальная температура должна быть числом")
        if not isinstance(temp_range_max, (int, float)):
            raise TypeError("Максимальная температура должна быть числом")
        if not isinstance(unit, str):
            raise TypeError("Единица измерения должна быть строкой")
        
        self.device_id = device_id
        self.temp_range_min = temp_range_min
        self.temp_range_max = temp_range_max
        self.unit = unit
        self.current_temperature: Optional[float] = None
        self.is_functional = True
        self.measurement_count = 0
    
    def set_temperature(self, temperature: float) -> None:
        """Установить температуру"""
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")
        if temperature < self.temp_range_min or temperature > self.temp_range_max:
            raise ValueError("Температура вне допустимого диапазона")
        self.current_temperature = temperature
        self.measurement_count += 1
    
    def used_by_sensor(self, sensor: 'TemperatureSensor') -> None:
        """Используется сенсором (ассоциация с TemperatureSensor)"""
        if sensor is None:
            raise ValueError("Сенсор не может быть None")
        if not self.is_functional:
            raise ValueError("Термометр не работает")
        if sensor.current_temperature is not None:
            self.set_temperature(sensor.current_temperature)
    
    def installed_at_station(self, station: 'WeatherStation') -> None:
        """Установлен на станции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if not self.is_functional:
            raise ValueError("Термометр не работает")


