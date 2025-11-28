"""Класс гримерки"""
from typing import List


class DressingRoom:
    """Гримерка театра"""
    
    def __init__(self, number: int, capacity: int):
        if not isinstance(number, int) or number < 0:
            raise ValueError("Номер должен быть неотрицательным целым числом")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")
        
        self.number = number
        self.capacity = capacity
        self.__occupants: List[str] = []
        self.has_mirror = True
        self.has_lighting = True
        self.is_available = True
    
    def add_occupant(self, name: str) -> None:
        """Добавить жильца"""
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if len(self.__occupants) < self.capacity:
            if name not in self.__occupants:
                self.__occupants.append(name)
    
    def remove_occupant(self, name: str) -> None:
        """Удалить жильца"""
        if name in self.__occupants:
            self.__occupants.remove(name)
    
    def get_occupants(self) -> List[str]:
        """Получить список жильцов"""
        return self.__occupants.copy()
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    def is_full(self) -> bool:
        """Проверить заполненность"""
        return len(self.__occupants) >= self.capacity
    
    occupants = property(get_occupants)

