"""Класс техника"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from sensors.temperature_sensor import TemperatureSensor
    from equipment.anemometer import Anemometer


class Technician:
    """Техник по обслуживанию оборудования"""
    
    def __init__(self, employee_id: str, name: str, specialization: str, certification: str):
        if not isinstance(employee_id, str) or not employee_id:
            raise ValueError("ID сотрудника должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(specialization, str):
            raise TypeError("Специализация должна быть строкой")
        if not isinstance(certification, str):
            raise TypeError("Сертификация должна быть строкой")
        
        self.employee_id = employee_id
        self.name = name
        self.specialization = specialization
        self.certification = certification
        self.__maintained_stations: List['WeatherStation'] = []
        self.maintenance_count = 0
        self.is_available = True
    
    def add_station(self, station: 'WeatherStation') -> None:
        """Добавить станцию для обслуживания"""
        if station not in self.__maintained_stations:
            self.__maintained_stations.append(station)
    
    def get_stations(self) -> List['WeatherStation']:
        """Получить станции"""
        return self.__maintained_stations.copy()
    
    def maintains_station(self, station: 'WeatherStation') -> None:
        """Обслуживает станцию (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        self.add_station(station)
        self.maintenance_count += 1
    
    def repairs_sensor(self, sensor: 'TemperatureSensor') -> None:
        """Ремонтирует сенсор (ассоциация с TemperatureSensor)"""
        if sensor is None:
            raise ValueError("Сенсор не может быть None")
        if not sensor.is_active:
            sensor.is_active = True
            self.maintenance_count += 1
    
    def repairs_equipment(self, equipment: 'Anemometer') -> None:
        """Ремонтирует оборудование (ассоциация с Anemometer)"""
        if equipment is None:
            raise ValueError("Оборудование не может быть None")
        if not equipment.is_calibrated:
            equipment.is_calibrated = True
            self.maintenance_count += 1
    
    stations = property(get_stations)


