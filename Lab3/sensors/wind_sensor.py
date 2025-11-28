"""Класс сенсора ветра"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.measurement import Measurement


class WindSensor:
    """Сенсор скорости и направления ветра"""
    
    def __init__(self, sensor_id: str, max_speed: float, min_speed: float, direction_range: int):
        if not isinstance(sensor_id, str) or not sensor_id:
            raise ValueError("ID сенсора должен быть непустой строкой")
        if not isinstance(max_speed, (int, float)) or max_speed < 0:
            raise ValueError("Максимальная скорость должна быть неотрицательной")
        if not isinstance(min_speed, (int, float)) or min_speed < 0:
            raise ValueError("Минимальная скорость должна быть неотрицательной")
        if not isinstance(direction_range, int) or direction_range < 0 or direction_range > 360:
            raise ValueError("Диапазон направления должен быть от 0 до 360")
        
        self.sensor_id = sensor_id
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.direction_range = direction_range
        self.__current_speed: Optional[float] = None
        self.__current_direction: Optional[int] = None
        self.is_active = True
        self.anemometer_type = "cup"
    
    def read_wind_speed(self) -> float:
        """Прочитать скорость ветра"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__current_speed is None:
            raise InvalidSensorDataException("Скорость ветра не измерена")
        return self.__current_speed
    
    def read_wind_direction(self) -> int:
        """Прочитать направление ветра"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__current_direction is None:
            raise InvalidSensorDataException("Направление ветра не измерено")
        return self.__current_direction
    
    def set_wind_data(self, speed: float, direction: int) -> None:
        """Установить данные ветра"""
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError("Скорость должна быть неотрицательной")
        if not isinstance(direction, int) or direction < 0 or direction > 360:
            raise ValueError("Направление должно быть от 0 до 360")
        self.__current_speed = speed
        self.__current_direction = direction
    
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
        if self.__current_speed is not None:
            measurement.value = self.__current_speed
            measurement.set_parameter_type("wind_speed")
    
    def get_current_speed(self) -> Optional[float]:
        """Получить текущую скорость"""
        return self.__current_speed
    
    def get_current_direction(self) -> Optional[int]:
        """Получить текущее направление"""
        return self.__current_direction
    
    current_speed = property(get_current_speed)
    current_direction = property(get_current_direction)


