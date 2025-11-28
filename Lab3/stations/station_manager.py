"""Класс менеджера станций"""
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from stations.station_network import StationNetwork
    from staff.administrator import Administrator


class StationManager:
    """Менеджер метеостанций"""
    
    def __init__(self, manager_id: str, name: str, experience_years: int):
        if not isinstance(manager_id, str) or not manager_id:
            raise ValueError("ID менеджера должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(experience_years, int) or experience_years < 0:
            raise ValueError("Опыт должен быть неотрицательным")
        
        self.manager_id = manager_id
        self.name = name
        self.experience_years = experience_years
        self.__managed_stations: List['WeatherStation'] = []
        self.__managed_networks: List['StationNetwork'] = []
        self.department = "operations"
        self.contact_email: Optional[str] = None
    
    def add_station(self, station: 'WeatherStation') -> None:
        """Добавить станцию в управление"""
        if station not in self.__managed_stations:
            self.__managed_stations.append(station)
    
    def add_network(self, network: 'StationNetwork') -> None:
        """Добавить сеть в управление"""
        if network not in self.__managed_networks:
            self.__managed_networks.append(network)
    
    def get_managed_stations(self) -> List['WeatherStation']:
        """Получить управляемые станции"""
        return self.__managed_stations.copy()
    
    def manages_station(self, station: 'WeatherStation') -> None:
        """Управляет станцией (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        self.add_station(station)
    
    def manages_network(self, network: 'StationNetwork') -> None:
        """Управляет сетью (ассоциация с StationNetwork)"""
        if network is None:
            raise ValueError("Сеть не может быть None")
        self.add_network(network)
    
    def reports_to(self, administrator: 'Administrator') -> None:
        """Отчитывается (ассоциация с Administrator)"""
        if administrator is None:
            raise ValueError("Администратор не может быть None")
        # Менеджер отчитывается администратору
    
    managed_stations = property(get_managed_stations)


