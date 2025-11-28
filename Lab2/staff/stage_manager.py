"""Класс постановщика"""
from typing import List


class StageManager:
    """Постановщик театра"""
    
    def __init__(self, name: str, age: int, experience_years: int, salary: float):
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")
        if not isinstance(experience_years, int) or experience_years < 0:
            raise ValueError("Опыт должен быть неотрицательным целым числом")
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Зарплата должна быть неотрицательным числом")
        
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.salary = salary
        self.__managed_stages: List[str] = []
        self.is_available = True
        self.stage_count = 0
    
    def add_stage(self, stage_name: str) -> None:
        """Добавить сцену"""
        if not isinstance(stage_name, str):
            raise TypeError("Название сцены должно быть строкой")
        if stage_name not in self.__managed_stages:
            self.__managed_stages.append(stage_name)
    
    def remove_stage(self, stage_name: str) -> None:
        """Удалить сцену"""
        if stage_name in self.__managed_stages:
            self.__managed_stages.remove(stage_name)
    
    def get_stages(self) -> List[str]:
        """Получить список сцен"""
        return self.__managed_stages.copy()
    
    def set_stage_count(self, count: int) -> None:
        """Установить количество сцен"""
        if not isinstance(count, int) or count < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")
        self.stage_count = count
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    stages = property(get_stages)

