"""Класс сенсора температуры"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.measurement import Measurement


class TemperatureSensor:
    """Сенсор температуры"""
    
    def __init__(self, sensor_id: str, min_temp: float, max_temp: float, accuracy: float):
        if not isinstance(sensor_id, str) or not sensor_id:
            raise ValueError("ID сенсора должен быть непустой строкой")
        if not isinstance(min_temp, (int, float)):
            raise TypeError("Минимальная температура должна быть числом")
        if not isinstance(max_temp, (int, float)):
            raise TypeError("Максимальная температура должна быть числом")
        if not isinstance(accuracy, (int, float)) or accuracy < 0:
            raise ValueError("Точность должна быть неотрицательным числом")
        
        self.sensor_id = sensor_id
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.accuracy = accuracy
        self.__current_temperature: Optional[float] = None
        self.is_active = True
        self.calibration_date: Optional[str] = None
        self.battery_level = 100.0
    
    def read_temperature(self) -> float:
        """Прочитать температуру"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__current_temperature is None:
            raise InvalidSensorDataException("Температура не измерена")
        return self.__current_temperature
    
    def set_temperature(self, temperature: float) -> None:
        """Установить температуру"""
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")
        if temperature < self.min_temp or temperature > self.max_temp:
            raise InvalidSensorDataException("Температура вне допустимого диапазона")
        self.__current_temperature = temperature
    
    def calibrate(self, reference_temp: float) -> None:
        """Калибровать сенсор"""
        if not isinstance(reference_temp, (int, float)):
            raise TypeError("Эталонная температура должна быть числом")
        self.calibration_date = "2024-01-01"
    
    def get_battery_level(self) -> float:
        """Получить уровень батареи"""
        return self.battery_level
    
    def attach_to_station(self, station: 'WeatherStation') -> None:
        """Присоединить к метеостанции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Метеостанция не может быть None")
        if not self.is_active:
            raise ValueError("Сенсор неактивен и не может быть присоединен")
        station.add_temperature_sensor(self)
    
    def create_measurement(self, measurement: 'Measurement') -> None:
        """Создать измерение (ассоциация с Measurement)"""
        if measurement is None:
            raise ValueError("Измерение не может быть None")
        if self.__current_temperature is not None:
            measurement.value = self.__current_temperature
            measurement.set_parameter_type("temperature")
            measurement.set_accuracy(self.accuracy)
    
    def get_current_temperature(self) -> Optional[float]:
        """Получить текущую температуру"""
        return self.__current_temperature
    
    current_temperature = property(get_current_temperature)


