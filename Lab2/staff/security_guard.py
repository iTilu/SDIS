"""Класс охранника"""
from typing import List


class SecurityGuard:
    """Охранник театра"""
    
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
        self.__assigned_areas: List[str] = []
        self.license_number = ""
        self.is_available = True
        self.shift = ""
    
    def add_area(self, area_name: str) -> None:
        """Добавить зону"""
        if not isinstance(area_name, str):
            raise TypeError("Название зоны должно быть строкой")
        if area_name not in self.__assigned_areas:
            self.__assigned_areas.append(area_name)
    
    def get_areas(self) -> List[str]:
        """Получить список зон"""
        return self.__assigned_areas.copy()
    
    def set_license_number(self, number: str) -> None:
        """Установить номер лицензии"""
        if not isinstance(number, str):
            raise TypeError("Номер должен быть строкой")
        self.license_number = number
    
    def set_shift(self, shift: str) -> None:
        """Установить смену"""
        if not isinstance(shift, str):
            raise TypeError("Смена должна быть строкой")
        self.shift = shift
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    areas = property(get_areas)

