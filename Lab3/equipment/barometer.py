"""Класс барометра"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from sensors.pressure_sensor import PressureSensor
    from stations.weather_station import WeatherStation


class Barometer:
    """Барометр для измерения давления"""
    
    def __init__(self, device_id: str, pressure_range: float, precision: float, type: str):
        if not isinstance(device_id, str) or not device_id:
            raise ValueError("ID устройства должен быть непустой строкой")
        if not isinstance(pressure_range, (int, float)) or pressure_range < 0:
            raise ValueError("Диапазон давления должен быть неотрицательным")
        if not isinstance(precision, (int, float)) or precision < 0:
            raise ValueError("Точность должна быть неотрицательной")
        if not isinstance(type, str):
            raise TypeError("Тип должен быть строкой")
        
        self.device_id = device_id
        self.pressure_range = pressure_range
        self.precision = precision
        self.type = type
        self.current_pressure: Optional[float] = None
        self.is_calibrated = True
        self.last_calibration: Optional[str] = None
    
    def set_pressure(self, pressure: float) -> None:
        """Установить давление"""
        if not isinstance(pressure, (int, float)) or pressure < 0:
            raise ValueError("Давление должно быть неотрицательным")
        self.current_pressure = pressure
    
    def used_by_sensor(self, sensor: 'PressureSensor') -> None:
        """Используется сенсором (ассоциация с PressureSensor)"""
        if sensor is None:
            raise ValueError("Сенсор не может быть None")
        if not self.is_calibrated:
            raise ValueError("Барометр не откалиброван")
        if sensor.current_pressure is not None:
            self.set_pressure(sensor.current_pressure)
    
    def installed_at_station(self, station: 'WeatherStation') -> None:
        """Установлен на станции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if not self.is_calibrated:
            raise ValueError("Барометр не откалиброван")


