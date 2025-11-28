"""Класс администратора"""
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from stations.station_network import StationNetwork
    from stations.station_manager import StationManager
    from staff.meteorologist import Meteorologist


class Administrator:
    """Администратор системы"""
    
    def __init__(self, employee_id: str, name: str, department: str, access_level: str):
        if not isinstance(employee_id, str) or not employee_id:
            raise ValueError("ID сотрудника должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(department, str):
            raise TypeError("Отдел должен быть строкой")
        if not isinstance(access_level, str):
            raise TypeError("Уровень доступа должен быть строкой")
        
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.access_level = access_level
        self.__managed_networks: List['StationNetwork'] = []
        self.system_access = True
    
    def add_network(self, network: 'StationNetwork') -> None:
        """Добавить сеть в управление"""
        if network not in self.__managed_networks:
            self.__managed_networks.append(network)
    
    def get_networks(self) -> List['StationNetwork']:
        """Получить сети"""
        return self.__managed_networks.copy()
    
    def manages_network(self, network: 'StationNetwork') -> None:
        """Управляет сетью (ассоциация с StationNetwork)"""
        if network is None:
            raise ValueError("Сеть не может быть None")
        self.add_network(network)
    
    def supervises_manager(self, manager: 'StationManager') -> None:
        """Наблюдает за менеджером (ассоциация с StationManager)"""
        if manager is None:
            raise ValueError("Менеджер не может быть None")
        # Администратор наблюдает за менеджером
    
    def manages_staff(self, meteorologist: 'Meteorologist') -> None:
        """Управляет персоналом (ассоциация с Meteorologist)"""
        if meteorologist is None:
            raise ValueError("Метеоролог не может быть None")
        # Администратор управляет персоналом
    
    networks = property(get_networks)


