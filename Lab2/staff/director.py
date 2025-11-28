"""Класс режиссера"""
from typing import List, Optional, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from performances.performance import Performance
    from performances.rehearsal import Rehearsal
    from schedule.session import Session


class Director:
    """Режиссер театра"""
    
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
        self.__directed_performances: List[str] = []
        self.is_available = True
        self.contract_end_date: Optional[date] = None
        self.awards: List[str] = []
    
    def add_performance(self, performance_name: str) -> None:
        """Добавить спектакль"""
        if not isinstance(performance_name, str):
            raise TypeError("Название спектакля должно быть строкой")
        if performance_name not in self.__directed_performances:
            self.__directed_performances.append(performance_name)
    
    def remove_performance(self, performance_name: str) -> None:
        """Удалить спектакль"""
        if performance_name in self.__directed_performances:
            self.__directed_performances.remove(performance_name)
    
    def get_performances(self) -> List[str]:
        """Получить список спектаклей"""
        return self.__directed_performances.copy()
    
    def add_award(self, award: str) -> None:
        """Добавить награду"""
        if not isinstance(award, str):
            raise TypeError("Награда должна быть строкой")
        if award not in self.awards:
            self.awards.append(award)
    
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
    
    def direct_performance(self, performance: 'Performance') -> None:
        """Режиссировать спектакль (ассоциация с Performance)"""
        if performance is None:
            raise ValueError("Спектакль не может быть None")
        if self.is_available:
            performance.assign_director(self)
            if performance.name not in self.__directed_performances:
                self.__directed_performances.append(performance.name)
    
    def conduct_rehearsal(self, rehearsal: 'Rehearsal') -> None:
        """Провести репетицию (ассоциация с Rehearsal)"""
        if rehearsal is None:
            raise ValueError("Репетиция не может быть None")
        if not self.is_available:
            raise ValueError("Режиссер недоступен для проведения репетиции")
    
    def manage_session(self, session: 'Session') -> None:
        """Управлять сеансом (ассоциация с Session)"""
        if session is None:
            raise ValueError("Сеанс не может быть None")
        if not self.is_available:
            raise ValueError("Режиссер недоступен для управления сеансом")
    
    performances = property(get_performances)

