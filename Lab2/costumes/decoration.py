"""Класс декорации"""
from typing import List


class Decoration:
    """Декорация для спектакля"""
    
    def __init__(self, name: str, width: float, height: float, depth: float):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        if not isinstance(depth, (int, float)) or depth <= 0:
            raise ValueError("Глубина должна быть положительным числом")
        
        self.name = name
        self.width = float(width)
        self.height = float(height)
        self.depth = float(depth)
        self.__performances: List[str] = []
        self.material = ""
        self.is_portable = True
        self.storage_location = ""
    
    def add_performance(self, performance_name: str) -> None:
        """Добавить спектакль"""
        if not isinstance(performance_name, str):
            raise TypeError("Название спектакля должно быть строкой")
        if performance_name not in self.__performances:
            self.__performances.append(performance_name)
    
    def get_performances(self) -> List[str]:
        """Получить список спектаклей"""
        return self.__performances.copy()
    
    def set_material(self, material: str) -> None:
        """Установить материал"""
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = material
    
    def calculate_volume(self) -> float:
        """Рассчитать объем"""
        return self.width * self.height * self.depth
    
    def set_storage_location(self, location: str) -> None:
        """Установить место хранения"""
        if not isinstance(location, str):
            raise TypeError("Место должно быть строкой")
        self.storage_location = location
    
    performances = property(get_performances)

