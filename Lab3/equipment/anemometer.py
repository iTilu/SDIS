"""Класс анемометра"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from sensors.wind_sensor import WindSensor
    from stations.weather_station import WeatherStation


class Anemometer:
    """Анемометр для измерения ветра"""
    
    def __init__(self, device_id: str, measurement_range: float, accuracy: float, sensor_type: str):
        if not isinstance(device_id, str) or not device_id:
            raise ValueError("ID устройства должен быть непустой строкой")
        if not isinstance(measurement_range, (int, float)) or measurement_range < 0:
            raise ValueError("Диапазон измерения должен быть неотрицательным")
        if not isinstance(accuracy, (int, float)) or accuracy < 0:
            raise ValueError("Точность должна быть неотрицательной")
        if not isinstance(sensor_type, str):
            raise TypeError("Тип сенсора должен быть строкой")
        
        self.device_id = device_id
        self.measurement_range = measurement_range
        self.accuracy = accuracy
        self.sensor_type = sensor_type
        self.current_reading: Optional[float] = None
        self.is_calibrated = True
        self.calibration_date: Optional[str] = None
    
    def set_reading(self, reading: float) -> None:
        """Установить показание"""
        if not isinstance(reading, (int, float)) or reading < 0:
            raise ValueError("Показание должно быть неотрицательным")
        self.current_reading = reading
    
    def used_by_sensor(self, sensor: 'WindSensor') -> None:
        """Используется сенсором (ассоциация с WindSensor)"""
        if sensor is None:
            raise ValueError("Сенсор не может быть None")
        if not self.is_calibrated:
            raise ValueError("Анемометр не откалиброван")
        if sensor.current_speed is not None:
            self.set_reading(sensor.current_speed)
    
    def installed_at_station(self, station: 'WeatherStation') -> None:
        """Установлен на станции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if not self.is_calibrated:
            raise ValueError("Анемометр не откалиброван")


