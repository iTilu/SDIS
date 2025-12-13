"""Класс измерения"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import DataValidationException

if TYPE_CHECKING:
    from sensors.temperature_sensor import TemperatureSensor
    from sensors.humidity_sensor import HumiditySensor
    from sensors.pressure_sensor import PressureSensor
    from data.weather_data import WeatherData


class Measurement:
    """Измерение погодного параметра"""
    
    def __init__(self, measurement_id: str, value: float, unit: str, timestamp: datetime):
        if not isinstance(measurement_id, str) or not measurement_id:
            raise ValueError("ID измерения должен быть непустой строкой")
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if not isinstance(unit, str):
            raise TypeError("Единица измерения должна быть строкой")
        if not isinstance(timestamp, datetime):
            raise TypeError("Временная метка должна быть datetime")
        
        self.measurement_id = measurement_id
        self.value = value
        self.unit = unit
        self.timestamp = timestamp
        self.parameter_type: Optional[str] = None
        self.accuracy: Optional[float] = None
        self.is_valid = True
    
    def set_parameter_type(self, param_type: str) -> None:
        """Установить тип параметра"""
        if not isinstance(param_type, str):
            raise TypeError("Тип параметра должен быть строкой")
        self.parameter_type = param_type
    
    def set_accuracy(self, accuracy: float) -> None:
        """Установить точность"""
        if not isinstance(accuracy, (int, float)) or accuracy < 0:
            raise ValueError("Точность должна быть неотрицательной")
        self.accuracy = accuracy
    
    def validate(self) -> bool:
        """Валидировать измерение"""
        if self.value is None:
            raise DataValidationException("Значение измерения отсутствует")
        return True
    
    def from_temperature_sensor(self, sensor: 'TemperatureSensor') -> None:
        """От сенсора температуры (ассоциация с TemperatureSensor)"""
        if sensor is None:
            raise ValueError("Сенсор не может быть None")
        if sensor.current_temperature is not None:
            self.value = sensor.current_temperature
            self.parameter_type = "temperature"
    
    def from_humidity_sensor(self, sensor: 'HumiditySensor') -> None:
        """От сенсора влажности (ассоциация с HumiditySensor)"""
        if sensor is None:
            raise ValueError("Сенсор не может быть None")
        if sensor.current_humidity is not None:
            self.value = sensor.current_humidity
            self.parameter_type = "humidity"
    
    def from_pressure_sensor(self, sensor: 'PressureSensor') -> None:
        """От сенсора давления (ассоциация с PressureSensor)"""
        if sensor is None:
            raise ValueError("Сенсор не может быть None")
        if sensor.current_pressure is not None:
            self.value = sensor.current_pressure
            self.parameter_type = "pressure"
    
    def add_to_weather_data(self, weather_data: 'WeatherData') -> None:
        """Добавить к данным о погоде (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        if self.parameter_type == "temperature":
            weather_data.temperature = self.value
        elif self.parameter_type == "humidity":
            weather_data.humidity = self.value
        elif self.parameter_type == "pressure":
            weather_data.add_pressure(self.value)


