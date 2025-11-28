"""Класс сети метеостанций"""
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from staff.administrator import Administrator


class StationNetwork:
    """Сеть метеостанций"""
    
    def __init__(self, network_id: str, network_name: str, region: str):
        if not isinstance(network_id, str) or not network_id:
            raise ValueError("ID сети должен быть непустой строкой")
        if not isinstance(network_name, str) or not network_name:
            raise ValueError("Название сети должно быть непустой строкой")
        if not isinstance(region, str):
            raise TypeError("Регион должен быть строкой")
        
        self.network_id = network_id
        self.network_name = network_name
        self.region = region
        self.__stations: List['WeatherStation'] = []
        self.coverage_area = 0.0
        self.data_sync_frequency = "hourly"
    
    def add_station(self, station: 'WeatherStation') -> None:
        """Добавить станцию"""
        if station not in self.__stations:
            self.__stations.append(station)
    
    def remove_station(self, station: 'WeatherStation') -> None:
        """Удалить станцию"""
        if station in self.__stations:
            self.__stations.remove(station)
    
    def get_stations(self) -> List['WeatherStation']:
        """Получить станции"""
        return self.__stations.copy()
    
    def set_coverage_area(self, area: float) -> None:
        """Установить площадь покрытия"""
        if not isinstance(area, (int, float)) or area < 0:
            raise ValueError("Площадь должна быть неотрицательной")
        self.coverage_area = area
    
    def contains_station(self, station: 'WeatherStation') -> None:
        """Содержит станцию (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        self.add_station(station)
    
    def managed_by(self, administrator: 'Administrator') -> None:
        """Управляется (ассоциация с Administrator)"""
        if administrator is None:
            raise ValueError("Администратор не может быть None")
        administrator.add_network(self)
    
    stations = property(get_stations)


