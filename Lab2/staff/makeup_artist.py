"""Класс гримера"""
from typing import List


class MakeupArtist:
    """Гример театра"""
    
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
        self.__makeup_styles: List[str] = []
        self.is_available = True
        self.tools_count = 0
    
    def add_makeup_style(self, style: str) -> None:
        """Добавить стиль грима"""
        if not isinstance(style, str):
            raise TypeError("Стиль должен быть строкой")
        if style not in self.__makeup_styles:
            self.__makeup_styles.append(style)
    
    def remove_makeup_style(self, style: str) -> None:
        """Удалить стиль грима"""
        if style in self.__makeup_styles:
            self.__makeup_styles.remove(style)
    
    def get_makeup_styles(self) -> List[str]:
        """Получить список стилей"""
        return self.__makeup_styles.copy()
    
    def set_tools_count(self, count: int) -> None:
        """Установить количество инструментов"""
        if not isinstance(count, int) or count < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")
        self.tools_count = count
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    makeup_styles = property(get_makeup_styles)

