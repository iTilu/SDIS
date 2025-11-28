"""Класс костюма"""
from typing import List, Optional


class Costume:
    """Костюм для спектакля"""
    
    def __init__(self, name: str, size: str, material: str):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(size, str) or not size:
            raise ValueError("Размер должен быть непустой строкой")
        if not isinstance(material, str) or not material:
            raise ValueError("Материал должен быть непустой строкой")
        
        self.name = name
        self.size = size
        self.material = material
        self.__performances: List[str] = []
        self.condition = ""
        self.is_available = True
        self.actor_name: Optional[str] = None
    
    def add_performance(self, performance_name: str) -> None:
        """Добавить спектакль"""
        if not isinstance(performance_name, str):
            raise TypeError("Название спектакля должно быть строкой")
        if performance_name not in self.__performances:
            self.__performances.append(performance_name)
    
    def get_performances(self) -> List[str]:
        """Получить список спектаклей"""
        return self.__performances.copy()
    
    def set_condition(self, condition: str) -> None:
        """Установить состояние"""
        if not isinstance(condition, str):
            raise TypeError("Состояние должно быть строкой")
        self.condition = condition
    
    def assign_to_actor(self, actor_name: str) -> None:
        """Назначить актеру"""
        if not isinstance(actor_name, str):
            raise TypeError("Имя актера должно быть строкой")
        self.actor_name = actor_name
        self.is_available = False
    
    def release(self) -> None:
        """Освободить костюм"""
        self.actor_name = None
        self.is_available = True
    
    performances = property(get_performances)

