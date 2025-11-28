"""Класс сенсора давления"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.measurement import Measurement


class PressureSensor:
    """Сенсор атмосферного давления"""
    
    def __init__(self, sensor_id: str, min_pressure: float, max_pressure: float, resolution: float):
        if not isinstance(sensor_id, str) or not sensor_id:
            raise ValueError("ID сенсора должен быть непустой строкой")
        if not isinstance(min_pressure, (int, float)) or min_pressure < 0:
            raise ValueError("Давление должно быть положительным")
        if not isinstance(max_pressure, (int, float)) or max_pressure < 0:
            raise ValueError("Давление должно быть положительным")
        if not isinstance(resolution, (int, float)) or resolution < 0:
            raise ValueError("Разрешение должно быть неотрицательным числом")
        
        self.sensor_id = sensor_id
        self.min_pressure = min_pressure
        self.max_pressure = max_pressure
        self.resolution = resolution
        self.__current_pressure: Optional[float] = None
        self.is_active = True
        self.altitude_correction = 0.0
        self.sensor_model = "barometric"
    
    def read_pressure(self) -> float:
        """Прочитать давление"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__current_pressure is None:
            raise InvalidSensorDataException("Давление не измерено")
        return self.__current_pressure
    
    def set_pressure(self, pressure: float) -> None:
        """Установить давление"""
        if not isinstance(pressure, (int, float)):
            raise TypeError("Давление должно быть числом")
        if pressure < self.min_pressure or pressure > self.max_pressure:
            raise InvalidSensorDataException("Давление вне допустимого диапазона")
        self.__current_pressure = pressure
    
    def apply_altitude_correction(self, altitude: float) -> None:
        """Применить поправку на высоту"""
        if not isinstance(altitude, (int, float)):
            raise TypeError("Высота должна быть числом")
        self.altitude_correction = altitude * 0.1
    
    def attach_to_station(self, station: 'WeatherStation') -> None:
        """Присоединить к метеостанции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Метеостанция не может быть None")
        if not self.is_active:
            raise ValueError("Сенсор неактивен и не может быть присоединен")
        station.add_pressure_sensor(self)
    
    def create_measurement(self, measurement: 'Measurement') -> None:
        """Создать измерение (ассоциация с Measurement)"""
        if measurement is None:
            raise ValueError("Измерение не может быть None")
        if self.__current_pressure is not None:
            measurement.value = self.__current_pressure
            measurement.set_parameter_type("pressure")
            measurement.set_accuracy(self.resolution)
    
    def get_current_pressure(self) -> Optional[float]:
        """Получить текущее давление"""
        return self.__current_pressure
    
    current_pressure = property(get_current_pressure)


