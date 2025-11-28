"""Класс костюмера"""
from typing import List


class CostumeDesigner:
    """Костюмер театра"""
    
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
        self.__designed_costumes: List[str] = []
        self.is_available = True
        self.specialization: str = ""
    
    def add_costume(self, costume_name: str) -> None:
        """Добавить костюм"""
        if not isinstance(costume_name, str):
            raise TypeError("Название костюма должно быть строкой")
        if costume_name not in self.__designed_costumes:
            self.__designed_costumes.append(costume_name)
    
    def remove_costume(self, costume_name: str) -> None:
        """Удалить костюм"""
        if costume_name in self.__designed_costumes:
            self.__designed_costumes.remove(costume_name)
    
    def get_costumes(self) -> List[str]:
        """Получить список костюмов"""
        return self.__designed_costumes.copy()
    
    def set_specialization(self, specialization: str) -> None:
        """Установить специализацию"""
        if not isinstance(specialization, str):
            raise TypeError("Специализация должна быть строкой")
        self.specialization = specialization
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    costumes = property(get_costumes)

