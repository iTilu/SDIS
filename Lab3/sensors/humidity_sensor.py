"""Класс сенсора влажности"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.measurement import Measurement


class HumiditySensor:
    """Сенсор влажности"""
    
    def __init__(self, sensor_id: str, min_humidity: float, max_humidity: float, precision: float):
        if not isinstance(sensor_id, str) or not sensor_id:
            raise ValueError("ID сенсора должен быть непустой строкой")
        if not isinstance(min_humidity, (int, float)) or min_humidity < 0 or min_humidity > 100:
            raise ValueError("Влажность должна быть от 0 до 100")
        if not isinstance(max_humidity, (int, float)) or max_humidity < 0 or max_humidity > 100:
            raise ValueError("Влажность должна быть от 0 до 100")
        if not isinstance(precision, (int, float)) or precision < 0:
            raise ValueError("Точность должна быть неотрицательным числом")
        
        self.sensor_id = sensor_id
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity
        self.precision = precision
        self.__current_humidity: Optional[float] = None
        self.is_active = True
        self.last_maintenance: Optional[str] = None
        self.sensor_type = "capacitive"
    
    def read_humidity(self) -> float:
        """Прочитать влажность"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__current_humidity is None:
            raise InvalidSensorDataException("Влажность не измерена")
        return self.__current_humidity
    
    def set_humidity(self, humidity: float) -> None:
        """Установить влажность"""
        if not isinstance(humidity, (int, float)):
            raise TypeError("Влажность должна быть числом")
        if humidity < 0 or humidity > 100:
            raise InvalidSensorDataException("Влажность должна быть от 0 до 100")
        self.__current_humidity = humidity
    
    def perform_maintenance(self) -> None:
        """Выполнить обслуживание"""
        self.last_maintenance = "2024-01-01"
        self.is_active = True
    
    def attach_to_station(self, station: 'WeatherStation') -> None:
        """Присоединить к метеостанции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Метеостанция не может быть None")
        if not self.is_active:
            raise ValueError("Сенсор неактивен и не может быть присоединен")
        station.add_humidity_sensor(self)
    
    def create_measurement(self, measurement: 'Measurement') -> None:
        """Создать измерение (ассоциация с Measurement)"""
        if measurement is None:
            raise ValueError("Измерение не может быть None")
        if self.__current_humidity is not None:
            measurement.value = self.__current_humidity
            measurement.set_parameter_type("humidity")
            measurement.set_accuracy(self.precision)
    
    def get_current_humidity(self) -> Optional[float]:
        """Получить текущую влажность"""
        return self.__current_humidity
    
    current_humidity = property(get_current_humidity)


