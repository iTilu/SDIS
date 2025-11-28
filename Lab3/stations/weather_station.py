"""Класс метеостанции"""
from typing import List, Optional, TYPE_CHECKING
from exceptions.weather_exceptions import WeatherStationException

if TYPE_CHECKING:
    from locations.location import Location
    from sensors.temperature_sensor import TemperatureSensor
    from sensors.humidity_sensor import HumiditySensor
    from sensors.pressure_sensor import PressureSensor
    from data.weather_data import WeatherData
    from staff.technician import Technician


class WeatherStation:
    """Метеостанция"""
    
    def __init__(self, station_id: str, name: str, latitude: float, longitude: float):
        if not isinstance(station_id, str) or not station_id:
            raise ValueError("ID станции должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(latitude, (int, float)) or latitude < -90 or latitude > 90:
            raise ValueError("Широта должна быть от -90 до 90")
        if not isinstance(longitude, (int, float)) or longitude < -180 or longitude > 180:
            raise ValueError("Долгота должна быть от -180 до 180")
        
        self.station_id = station_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.__temperature_sensors: List['TemperatureSensor'] = []
        self.__humidity_sensors: List['HumiditySensor'] = []
        self.__pressure_sensors: List['PressureSensor'] = []
        self.is_operational = True
        self.installation_date: Optional[str] = None
        self.elevation: Optional[float] = None
    
    def add_temperature_sensor(self, sensor: 'TemperatureSensor') -> None:
        """Добавить сенсор температуры"""
        if sensor not in self.__temperature_sensors:
            self.__temperature_sensors.append(sensor)
    
    def add_humidity_sensor(self, sensor: 'HumiditySensor') -> None:
        """Добавить сенсор влажности"""
        if sensor not in self.__humidity_sensors:
            self.__humidity_sensors.append(sensor)
    
    def add_pressure_sensor(self, sensor: 'PressureSensor') -> None:
        """Добавить сенсор давления"""
        if sensor not in self.__pressure_sensors:
            self.__pressure_sensors.append(sensor)
    
    def get_temperature_sensors(self) -> List['TemperatureSensor']:
        """Получить сенсоры температуры"""
        return self.__temperature_sensors.copy()
    
    def set_elevation(self, elevation: float) -> None:
        """Установить высоту"""
        if not isinstance(elevation, (int, float)) or elevation < 0:
            raise ValueError("Высота должна быть неотрицательной")
        self.elevation = elevation
    
    def located_at(self, location: 'Location') -> None:
        """Расположена в (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        # Станция расположена в локации
        if hasattr(location, 'latitude') and hasattr(location, 'longitude'):
            self.latitude = location.latitude
            self.longitude = location.longitude
    
    def generates_data(self, weather_data: 'WeatherData') -> None:
        """Генерирует данные (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        # Станция генерирует данные
        if self.__temperature_sensors:
            for sensor in self.__temperature_sensors:
                if sensor.current_temperature is not None:
                    weather_data.temperature = sensor.current_temperature
    
    def maintained_by(self, technician: 'Technician') -> None:
        """Обслуживается (ассоциация с Technician)"""
        if technician is None:
            raise ValueError("Техник не может быть None")
        if not technician.is_available:
            raise ValueError("Техник недоступен")
        technician.add_station(self)
    
    temperature_sensors = property(get_temperature_sensors)


