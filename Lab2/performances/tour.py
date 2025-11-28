"""Класс гастролей"""
from typing import List
from datetime import datetime


class Tour:
    """Гастроли театра"""
    
    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(start_date, datetime):
            raise ValueError("Дата начала должна быть объектом datetime")
        if not isinstance(end_date, datetime):
            raise ValueError("Дата окончания должна быть объектом datetime")
        if end_date < start_date:
            raise ValueError("Дата окончания должна быть позже даты начала")
        
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.__cities: List[str] = []
        self.__performances: List[str] = []
        self.total_revenue = 0.0
        self.is_completed = False
    
    def add_city(self, city: str) -> None:
        """Добавить город"""
        if not isinstance(city, str):
            raise TypeError("Город должен быть строкой")
        if city not in self.__cities:
            self.__cities.append(city)
    
    def remove_city(self, city: str) -> None:
        """Удалить город"""
        if city in self.__cities:
            self.__cities.remove(city)
    
    def get_cities(self) -> List[str]:
        """Получить список городов"""
        return self.__cities.copy()
    
    def add_performance(self, performance_name: str) -> None:
        """Добавить спектакль"""
        if not isinstance(performance_name, str):
            raise TypeError("Название спектакля должно быть строкой")
        if performance_name not in self.__performances:
            self.__performances.append(performance_name)
    
    def get_performances(self) -> List[str]:
        """Получить список спектаклей"""
        return self.__performances.copy()
    
    def add_revenue(self, amount: float) -> None:
        """Добавить доход"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        self.total_revenue += amount
    
    def mark_completed(self) -> None:
        """Отметить как завершенные"""
        self.is_completed = True
    
    cities = property(get_cities)
    performances = property(get_performances)

