"""Класс реквизита"""
from typing import List, Optional


class Prop:
    """Реквизит для спектакля"""
    
    def __init__(self, name: str, prop_type: str, weight: float):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(prop_type, str) or not prop_type:
            raise ValueError("Тип должен быть непустой строкой")
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Вес должен быть неотрицательным числом")
        
        self.name = name
        self.prop_type = prop_type
        self.weight = float(weight)
        self.__performances: List[str] = []
        self.condition = ""
        self.is_available = True
        self.storage_location: Optional[str] = None
    
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
    
    def set_storage_location(self, location: str) -> None:
        """Установить место хранения"""
        if not isinstance(location, str):
            raise TypeError("Место должно быть строкой")
        self.storage_location = location
        self.is_available = False
    
    def release(self) -> None:
        """Освободить реквизит"""
        self.storage_location = None
        self.is_available = True
    
    performances = property(get_performances)

