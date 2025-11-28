"""Класс сенсора дождя"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.measurement import Measurement


class RainSensor:
    """Сенсор осадков"""
    
    def __init__(self, sensor_id: str, collection_area: float, max_intensity: float, sensitivity: float):
        if not isinstance(sensor_id, str) or not sensor_id:
            raise ValueError("ID сенсора должен быть непустой строкой")
        if not isinstance(collection_area, (int, float)) or collection_area <= 0:
            raise ValueError("Площадь сбора должна быть положительной")
        if not isinstance(max_intensity, (int, float)) or max_intensity < 0:
            raise ValueError("Максимальная интенсивность должна быть неотрицательной")
        if not isinstance(sensitivity, (int, float)) or sensitivity < 0:
            raise ValueError("Чувствительность должна быть неотрицательной")
        
        self.sensor_id = sensor_id
        self.collection_area = collection_area
        self.max_intensity = max_intensity
        self.sensitivity = sensitivity
        self.__rainfall_amount: Optional[float] = None
        self.__intensity: Optional[float] = None
        self.is_active = True
        self.tip_count = 0
    
    def read_rainfall(self) -> float:
        """Прочитать количество осадков"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__rainfall_amount is None:
            raise InvalidSensorDataException("Осадки не измерены")
        return self.__rainfall_amount
    
    def read_intensity(self) -> float:
        """Прочитать интенсивность дождя"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__intensity is None:
            raise InvalidSensorDataException("Интенсивность не измерена")
        return self.__intensity
    
    def set_rain_data(self, amount: float, intensity: float) -> None:
        """Установить данные осадков"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Количество осадков должно быть неотрицательным")
        if not isinstance(intensity, (int, float)) or intensity < 0:
            raise ValueError("Интенсивность должна быть неотрицательной")
        self.__rainfall_amount = amount
        self.__intensity = intensity
    
    def reset_tip_counter(self) -> None:
        """Сбросить счетчик наклонов"""
        self.tip_count = 0
    
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
        if self.__rainfall_amount is not None:
            measurement.value = self.__rainfall_amount
            measurement.set_parameter_type("rainfall")
    
    def get_rainfall_amount(self) -> Optional[float]:
        """Получить количество осадков"""
        return self.__rainfall_amount
    
    rainfall_amount = property(get_rainfall_amount)


