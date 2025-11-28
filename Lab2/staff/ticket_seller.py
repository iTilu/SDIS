"""Класс билетера"""
from typing import List


class TicketSeller:
    """Билетер театра"""
    
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
        self.__sold_tickets_count = 0
        self.is_available = True
        self.workplace_number = 0
    
    def sell_ticket(self) -> None:
        """Продать билет"""
        self.__sold_tickets_count += 1
    
    def get_sold_tickets_count(self) -> int:
        """Получить количество проданных билетов"""
        return self.__sold_tickets_count
    
    def reset_sold_tickets(self) -> None:
        """Сбросить счетчик проданных билетов"""
        self.__sold_tickets_count = 0
    
    def set_workplace_number(self, number: int) -> None:
        """Установить номер рабочего места"""
        if not isinstance(number, int) or number < 0:
            raise ValueError("Номер должен быть неотрицательным целым числом")
        self.workplace_number = number
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    sold_tickets_count = property(get_sold_tickets_count)

