"""Класс художника-декоратора"""
from typing import List


class SetDesigner:
    """Художник-декоратор театра"""
    
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
        self.__designed_sets: List[str] = []
        self.is_available = True
        self.style = ""
    
    def add_set(self, set_name: str) -> None:
        """Добавить декорацию"""
        if not isinstance(set_name, str):
            raise TypeError("Название декорации должно быть строкой")
        if set_name not in self.__designed_sets:
            self.__designed_sets.append(set_name)
    
    def remove_set(self, set_name: str) -> None:
        """Удалить декорацию"""
        if set_name in self.__designed_sets:
            self.__designed_sets.remove(set_name)
    
    def get_sets(self) -> List[str]:
        """Получить список декораций"""
        return self.__designed_sets.copy()
    
    def set_style(self, style: str) -> None:
        """Установить стиль"""
        if not isinstance(style, str):
            raise TypeError("Стиль должен быть строкой")
        self.style = style
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    sets = property(get_sets)

