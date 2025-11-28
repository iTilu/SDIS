"""Класс сенсора УФ-излучения"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import SensorMalfunctionException, InvalidSensorDataException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.measurement import Measurement


class UVSensor:
    """Сенсор ультрафиолетового излучения"""
    
    def __init__(self, sensor_id: str, max_uv_index: float, wavelength_range: str, response_time: float):
        if not isinstance(sensor_id, str) or not sensor_id:
            raise ValueError("ID сенсора должен быть непустой строкой")
        if not isinstance(max_uv_index, (int, float)) or max_uv_index < 0:
            raise ValueError("Максимальный УФ-индекс должен быть неотрицательным")
        if not isinstance(wavelength_range, str):
            raise TypeError("Диапазон длин волн должен быть строкой")
        if not isinstance(response_time, (int, float)) or response_time < 0:
            raise ValueError("Время отклика должно быть неотрицательным")
        
        self.sensor_id = sensor_id
        self.max_uv_index = max_uv_index
        self.wavelength_range = wavelength_range
        self.response_time = response_time
        self.__current_uv_index: Optional[float] = None
        self.is_active = True
        self.exposure_level = "moderate"
    
    def read_uv_index(self) -> float:
        """Прочитать УФ-индекс"""
        if not self.is_active:
            raise SensorMalfunctionException("Сенсор неактивен")
        if self.__current_uv_index is None:
            raise InvalidSensorDataException("УФ-индекс не измерен")
        return self.__current_uv_index
    
    def set_uv_index(self, uv_index: float) -> None:
        """Установить УФ-индекс"""
        if not isinstance(uv_index, (int, float)) or uv_index < 0:
            raise ValueError("УФ-индекс должен быть неотрицательным")
        if uv_index > self.max_uv_index:
            raise InvalidSensorDataException("УФ-индекс превышает максимальный")
        self.__current_uv_index = uv_index
        self._update_exposure_level()
    
    def _update_exposure_level(self) -> None:
        """Обновить уровень воздействия"""
        if self.__current_uv_index is None:
            return
        if self.__current_uv_index < 3:
            self.exposure_level = "low"
        elif self.__current_uv_index < 6:
            self.exposure_level = "moderate"
        elif self.__current_uv_index < 8:
            self.exposure_level = "high"
        else:
            self.exposure_level = "very_high"
    
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
        if self.__current_uv_index is not None:
            measurement.value = self.__current_uv_index
            measurement.set_parameter_type("uv_index")
    
    def get_current_uv_index(self) -> Optional[float]:
        """Получить текущий УФ-индекс"""
        return self.__current_uv_index
    
    current_uv_index = property(get_current_uv_index)


