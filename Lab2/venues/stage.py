"""Класс сцены"""
from typing import List


class Stage:
    """Сцена театра"""
    
    def __init__(self, name: str, width: float, depth: float, height: float):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        if not isinstance(depth, (int, float)) or depth <= 0:
            raise ValueError("Глубина должна быть положительным числом")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        
        self.name = name
        self.width = float(width)
        self.depth = float(depth)
        self.height = float(height)
        self.__equipment: List[str] = []
        self.is_available = True
        self.current_performance = ""
    
    def add_equipment(self, equipment: str) -> None:
        """Добавить оборудование"""
        if not isinstance(equipment, str):
            raise TypeError("Оборудование должно быть строкой")
        if equipment not in self.__equipment:
            self.__equipment.append(equipment)
    
    def get_equipment(self) -> List[str]:
        """Получить список оборудования"""
        return self.__equipment.copy()
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    def set_current_performance(self, performance: str) -> None:
        """Установить текущий спектакль"""
        if not isinstance(performance, str):
            raise TypeError("Спектакль должен быть строкой")
        self.current_performance = performance
    
    def calculate_area(self) -> float:
        """Рассчитать площадь"""
        return self.width * self.depth
    
    equipment = property(get_equipment)

