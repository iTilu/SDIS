"""Класс музыканта"""
from typing import List


class Musician:
    """Музыкант театра"""
    
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
        self.__instruments: List[str] = []
        self.is_available = True
        self.specialization = ""
    
    def add_instrument(self, instrument: str) -> None:
        """Добавить инструмент"""
        if not isinstance(instrument, str):
            raise TypeError("Инструмент должен быть строкой")
        if instrument not in self.__instruments:
            self.__instruments.append(instrument)
    
    def remove_instrument(self, instrument: str) -> None:
        """Удалить инструмент"""
        if instrument in self.__instruments:
            self.__instruments.remove(instrument)
    
    def get_instruments(self) -> List[str]:
        """Получить список инструментов"""
        return self.__instruments.copy()
    
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
    
    instruments = property(get_instruments)

