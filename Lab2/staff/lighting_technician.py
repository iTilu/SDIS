"""Класс осветителя"""
from typing import List


class LightingTechnician:
    """Осветитель театра"""
    
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
        self.__lighting_equipment: List[str] = []
        self.is_available = True
        self.equipment_count = 0
    
    def add_equipment(self, equipment: str) -> None:
        """Добавить оборудование"""
        if not isinstance(equipment, str):
            raise TypeError("Оборудование должно быть строкой")
        if equipment not in self.__lighting_equipment:
            self.__lighting_equipment.append(equipment)
    
    def remove_equipment(self, equipment: str) -> None:
        """Удалить оборудование"""
        if equipment in self.__lighting_equipment:
            self.__lighting_equipment.remove(equipment)
    
    def get_equipment(self) -> List[str]:
        """Получить список оборудования"""
        return self.__lighting_equipment.copy()
    
    def set_equipment_count(self, count: int) -> None:
        """Установить количество оборудования"""
        if not isinstance(count, int) or count < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")
        self.equipment_count = count
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    equipment = property(get_equipment)

