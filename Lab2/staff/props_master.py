"""Класс реквизитора"""
from typing import List


class PropsMaster:
    """Реквизитор театра"""
    
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
        self.__managed_props: List[str] = []
        self.is_available = True
        self.props_count = 0
    
    def add_prop(self, prop_name: str) -> None:
        """Добавить реквизит"""
        if not isinstance(prop_name, str):
            raise TypeError("Название реквизита должно быть строкой")
        if prop_name not in self.__managed_props:
            self.__managed_props.append(prop_name)
    
    def remove_prop(self, prop_name: str) -> None:
        """Удалить реквизит"""
        if prop_name in self.__managed_props:
            self.__managed_props.remove(prop_name)
    
    def get_props(self) -> List[str]:
        """Получить список реквизита"""
        return self.__managed_props.copy()
    
    def set_props_count(self, count: int) -> None:
        """Установить количество реквизита"""
        if not isinstance(count, int) or count < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")
        self.props_count = count
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    props = property(get_props)

