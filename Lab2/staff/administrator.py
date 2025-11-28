"""Класс администратора"""
from typing import List


class Administrator:
    """Администратор театра"""
    
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
        self.__managed_events: List[str] = []
        self.is_available = True
        self.department = ""
    
    def add_event(self, event_name: str) -> None:
        """Добавить событие"""
        if not isinstance(event_name, str):
            raise TypeError("Название события должно быть строкой")
        if event_name not in self.__managed_events:
            self.__managed_events.append(event_name)
    
    def remove_event(self, event_name: str) -> None:
        """Удалить событие"""
        if event_name in self.__managed_events:
            self.__managed_events.remove(event_name)
    
    def get_events(self) -> List[str]:
        """Получить список событий"""
        return self.__managed_events.copy()
    
    def set_department(self, department: str) -> None:
        """Установить отдел"""
        if not isinstance(department, str):
            raise TypeError("Отдел должен быть строкой")
        self.department = department
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    events = property(get_events)

