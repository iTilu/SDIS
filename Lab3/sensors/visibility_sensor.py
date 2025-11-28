"""Класс сенсора видимости"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.measurement import Measurement


class VisibilitySensor:
    """Сенсор видимости"""
    
    def __init__(self, sensor_id: str, max_range: float, min_range: float, measurement_unit: str):
        if not isinstance(sensor_id, str) or not sensor_id:
            raise ValueError("ID сенсора должен быть непустой строкой")
        if not isinstance(max_range, (int, float)) or max_range < 0:
            raise ValueError("Максимальная дальность должна быть неотрицательной")
        if not isinstance(min_range, (int, float)) or min_range < 0:
            raise ValueError("Минимальная дальность должна быть неотрицательной")
        if not isinstance(measurement_unit, str):
            raise TypeError("Единица измерения должна быть строкой")
        
        self.sensor_id = sensor_id
        self.max_range = max_range
        self.min_range = min_range
        self.measurement_unit = measurement_unit
        self.__current_visibility: Optional[float] = None
        self.is_active = True
        self.sensor_technology = "scattering"
    
    def read_visibility(self) -> float:
        """Прочитать видимость"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__current_visibility is None:
            raise InvalidSensorDataException("Видимость не измерена")
        return self.__current_visibility
    
    def set_visibility(self, visibility: float) -> None:
        """Установить видимость"""
        if not isinstance(visibility, (int, float)) or visibility < 0:
            raise ValueError("Видимость должна быть неотрицательной")
        if visibility < self.min_range or visibility > self.max_range:
            raise InvalidSensorDataException("Видимость вне допустимого диапазона")
        self.__current_visibility = visibility
    
    def attach_to_station(self, station: 'WeatherStation') -> None:
        """Присоединить к метеостанции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Метеостанция не может быть None")
        if not self.is_active:
            raise ValueError("Сенсор неактивен и не может быть присоединен")
    
    def create_measurement(self, measurement: 'Measurement') -> None:
        """Создать измерение (ассоциация с Measurement)"""
        if measurement is None:
            raise ValueError("Измерение не может быть None")
        if self.__current_visibility is not None:
            measurement.value = self.__current_visibility
            measurement.set_parameter_type("visibility")
    
    def get_current_visibility(self) -> Optional[float]:
        """Получить текущую видимость"""
        return self.__current_visibility
    
    current_visibility = property(get_current_visibility)


