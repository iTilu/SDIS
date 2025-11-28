"""Класс менеджера"""
from typing import List


class Manager:
    """Менеджер театра"""
    
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
        self.__managed_projects: List[str] = []
        self.is_available = True
        self.team_size = 0
    
    def add_project(self, project_name: str) -> None:
        """Добавить проект"""
        if not isinstance(project_name, str):
            raise TypeError("Название проекта должно быть строкой")
        if project_name not in self.__managed_projects:
            self.__managed_projects.append(project_name)
    
    def remove_project(self, project_name: str) -> None:
        """Удалить проект"""
        if project_name in self.__managed_projects:
            self.__managed_projects.remove(project_name)
    
    def get_projects(self) -> List[str]:
        """Получить список проектов"""
        return self.__managed_projects.copy()
    
    def set_team_size(self, size: int) -> None:
        """Установить размер команды"""
        if not isinstance(size, int) or size < 0:
            raise ValueError("Размер должен быть неотрицательным целым числом")
        self.team_size = size
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    projects = property(get_projects)

