"""Класс наблюдателя"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from data.weather_data import WeatherData
    from equipment.barometer import Barometer


class Observer:
    """Наблюдатель погоды"""
    
    def __init__(self, employee_id: str, name: str, observation_skills: List[str], shift_hours: int):
        if not isinstance(employee_id, str) or not employee_id:
            raise ValueError("ID сотрудника должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(observation_skills, list):
            raise TypeError("Навыки должны быть списком")
        if not isinstance(shift_hours, int) or shift_hours < 0:
            raise ValueError("Часы смены должны быть неотрицательными")
        
        self.employee_id = employee_id
        self.name = name
        self.observation_skills = observation_skills
        self.shift_hours = shift_hours
        self.__observations: List['WeatherData'] = []
        self.observation_count = 0
        self.station_assignment: Optional[str] = None
    
    def add_observation(self, weather_data: 'WeatherData') -> None:
        """Добавить наблюдение"""
        if weather_data not in self.__observations:
            self.__observations.append(weather_data)
            self.observation_count = len(self.__observations)
    
    def get_observations(self) -> List['WeatherData']:
        """Получить наблюдения"""
        return self.__observations.copy()
    
    def observes_at_station(self, station: 'WeatherStation') -> None:
        """Наблюдает на станции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if not station.is_operational:
            raise ValueError("Станция не работает")
        self.station_assignment = station.station_id
    
    def records_data(self, weather_data: 'WeatherData') -> None:
        """Записывает данные (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        self.add_observation(weather_data)
    
    def uses_barometer(self, barometer: 'Barometer') -> None:
        """Использует барометр (ассоциация с Barometer)"""
        if barometer is None:
            raise ValueError("Барометр не может быть None")
        if not barometer.is_calibrated:
            raise ValueError("Барометр не откалиброван")
    
    observations = property(get_observations)


