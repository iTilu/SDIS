"""Класс сенсора качества воздуха"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.measurement import Measurement


class AirQualitySensor:
    """Сенсор качества воздуха"""
    
    def __init__(self, sensor_id: str, pm25_max: float, pm10_max: float, co_max: float):
        if not isinstance(sensor_id, str) or not sensor_id:
            raise ValueError("ID сенсора должен быть непустой строкой")
        if not isinstance(pm25_max, (int, float)) or pm25_max < 0:
            raise ValueError("Максимальный PM2.5 должен быть неотрицательным")
        if not isinstance(pm10_max, (int, float)) or pm10_max < 0:
            raise ValueError("Максимальный PM10 должен быть неотрицательным")
        if not isinstance(co_max, (int, float)) or co_max < 0:
            raise ValueError("Максимальный CO должен быть неотрицательным")
        
        self.sensor_id = sensor_id
        self.pm25_max = pm25_max
        self.pm10_max = pm10_max
        self.co_max = co_max
        self.__pm25_value: Optional[float] = None
        self.__pm10_value: Optional[float] = None
        self.__co_value: Optional[float] = None
        self.is_active = True
        self.air_quality_index = 0
    
    def read_pm25(self) -> float:
        """Прочитать PM2.5"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__pm25_value is None:
            raise InvalidSensorDataException("PM2.5 не измерен")
        return self.__pm25_value
    
    def read_pm10(self) -> float:
        """Прочитать PM10"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__pm10_value is None:
            raise InvalidSensorDataException("PM10 не измерен")
        return self.__pm10_value
    
    def read_co(self) -> float:
        """Прочитать CO"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__co_value is None:
            raise InvalidSensorDataException("CO не измерен")
        return self.__co_value
    
    def set_air_quality_data(self, pm25: float, pm10: float, co: float) -> None:
        """Установить данные качества воздуха"""
        if not isinstance(pm25, (int, float)) or pm25 < 0:
            raise ValueError("PM2.5 должен быть неотрицательным")
        if not isinstance(pm10, (int, float)) or pm10 < 0:
            raise ValueError("PM10 должен быть неотрицательным")
        if not isinstance(co, (int, float)) or co < 0:
            raise ValueError("CO должен быть неотрицательным")
        self.__pm25_value = pm25
        self.__pm10_value = pm10
        self.__co_value = co
        self._calculate_aqi()
    
    def _calculate_aqi(self) -> None:
        """Рассчитать индекс качества воздуха"""
        if self.__pm25_value is None or self.__pm10_value is None:
            return
        self.air_quality_index = (self.__pm25_value + self.__pm10_value) / 2
    
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
        if self.__pm25_value is not None:
            measurement.value = self.__pm25_value
            measurement.set_parameter_type("pm25")
    
    def get_pm25_value(self) -> Optional[float]:
        """Получить значение PM2.5"""
        return self.__pm25_value
    
    pm25_value = property(get_pm25_value)


