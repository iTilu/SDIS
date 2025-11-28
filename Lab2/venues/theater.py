"""Класс театра"""
from typing import List


class Theater:
    """Театр"""
    
    def __init__(self, name: str, address: str, capacity: int):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(address, str) or not address:
            raise ValueError("Адрес должен быть непустой строкой")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")
        
        self.name = name
        self.address = address
        self.capacity = capacity
        self.__stages: List[str] = []
        self.__dressing_rooms: List[str] = []
        self.founded_year = 0
        self.is_active = True
    
    def add_stage(self, stage_name: str) -> None:
        """Добавить сцену"""
        if not isinstance(stage_name, str):
            raise TypeError("Название сцены должно быть строкой")
        if stage_name not in self.__stages:
            self.__stages.append(stage_name)
    
    def get_stages(self) -> List[str]:
        """Получить список сцен"""
        return self.__stages.copy()
    
    def add_dressing_room(self, room_name: str) -> None:
        """Добавить гримерку"""
        if not isinstance(room_name, str):
            raise TypeError("Название гримерки должно быть строкой")
        if room_name not in self.__dressing_rooms:
            self.__dressing_rooms.append(room_name)
    
    def get_dressing_rooms(self) -> List[str]:
        """Получить список гримерок"""
        return self.__dressing_rooms.copy()
    
    def set_founded_year(self, year: int) -> None:
        """Установить год основания"""
        if not isinstance(year, int) or year < 0:
            raise ValueError("Год должен быть неотрицательным целым числом")
        self.founded_year = year
    
    stages = property(get_stages)
    dressing_rooms = property(get_dressing_rooms)

