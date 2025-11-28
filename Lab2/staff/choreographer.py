"""Класс хореографа"""
from typing import List


class Choreographer:
    """Хореограф театра"""
    
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
        self.__choreographies: List[str] = []
        self.is_available = True
        self.dance_style = ""
    
    def add_choreography(self, choreography_name: str) -> None:
        """Добавить хореографию"""
        if not isinstance(choreography_name, str):
            raise TypeError("Название хореографии должно быть строкой")
        if choreography_name not in self.__choreographies:
            self.__choreographies.append(choreography_name)
    
    def remove_choreography(self, choreography_name: str) -> None:
        """Удалить хореографию"""
        if choreography_name in self.__choreographies:
            self.__choreographies.remove(choreography_name)
    
    def get_choreographies(self) -> List[str]:
        """Получить список хореографий"""
        return self.__choreographies.copy()
    
    def set_dance_style(self, style: str) -> None:
        """Установить стиль танца"""
        if not isinstance(style, str):
            raise TypeError("Стиль должен быть строкой")
        self.dance_style = style
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    choreographies = property(get_choreographies)

