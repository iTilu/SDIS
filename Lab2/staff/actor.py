"""Класс актера"""
from typing import List, Optional, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from performances.performance import Performance
    from costumes.costume import Costume
    from schedule.rehearsal import Rehearsal
    from finance.salary import Salary


class Actor:
    """Актер театра"""
    
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
        self.__roles: List[str] = []
        self.is_available = True
        self.contract_end_date: Optional[date] = None
    
    def add_role(self, role: str) -> None:
        """Добавить роль"""
        if not isinstance(role, str):
            raise TypeError("Роль должна быть строкой")
        if role not in self.__roles:
            self.__roles.append(role)
    
    def remove_role(self, role: str) -> None:
        """Удалить роль"""
        if role in self.__roles:
            self.__roles.remove(role)
    
    def get_roles(self) -> List[str]:
        """Получить список ролей"""
        return self.__roles.copy()
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    def calculate_total_earnings(self, months: int) -> float:
        """Рассчитать общий заработок за месяцы"""
        if not isinstance(months, int) or months < 0:
            raise ValueError("Количество месяцев должно быть неотрицательным")
        return self.salary * months
    
    def join_performance(self, performance: 'Performance') -> None:
        """Присоединиться к спектаклю (ассоциация с Performance)"""
        if performance is None:
            raise ValueError("Спектакль не может быть None")
        if self.is_available:
            performance.assign_actor(self)
    
    def get_costume(self, costume: 'Costume') -> None:
        """Получить костюм (ассоциация с Costume)"""
        if costume is None:
            raise ValueError("Костюм не может быть None")
        # Актер получает костюм для спектакля
        if not self.is_available:
            raise ValueError("Актер недоступен для получения костюма")
    
    def attend_rehearsal(self, rehearsal: 'Rehearsal') -> None:
        """Посетить репетицию (ассоциация с Rehearsal)"""
        if rehearsal is None:
            raise ValueError("Репетиция не может быть None")
        if not self.is_available:
            raise ValueError("Актер недоступен для репетиции")
    
    def receive_salary(self, salary: 'Salary') -> None:
        """Получить зарплату (ассоциация с Salary)"""
        if salary is None:
            raise ValueError("Зарплата не может быть None")
        if salary.employee_name != self.name:
            raise ValueError("Зарплата предназначена другому сотруднику")
    
    roles = property(get_roles)

