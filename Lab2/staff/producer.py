"""Класс продюсера"""
from typing import List


class Producer:
    """Продюсер театра"""
    
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
        self.__produced_shows: List[str] = []
        self.is_available = True
        self.budget_managed = 0.0
    
    def add_show(self, show_name: str) -> None:
        """Добавить шоу"""
        if not isinstance(show_name, str):
            raise TypeError("Название шоу должно быть строкой")
        if show_name not in self.__produced_shows:
            self.__produced_shows.append(show_name)
    
    def remove_show(self, show_name: str) -> None:
        """Удалить шоу"""
        if show_name in self.__produced_shows:
            self.__produced_shows.remove(show_name)
    
    def get_shows(self) -> List[str]:
        """Получить список шоу"""
        return self.__produced_shows.copy()
    
    def set_budget_managed(self, budget: float) -> None:
        """Установить управляемый бюджет"""
        if not isinstance(budget, (int, float)) or budget < 0:
            raise ValueError("Бюджет должен быть неотрицательным числом")
        self.budget_managed = float(budget)
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    shows = property(get_shows)

