"""Класс расписания"""
from typing import List
from datetime import datetime


class Schedule:
    """Расписание театра"""
    
    def __init__(self, month: int, year: int):
        if not isinstance(month, int) or month < 1 or month > 12:
            raise ValueError("Месяц должен быть числом от 1 до 12")
        if not isinstance(year, int) or year < 0:
            raise ValueError("Год должен быть неотрицательным целым числом")
        
        self.month = month
        self.year = year
        self.__events: List[str] = []
        self.__performances: List[str] = []
        self.is_published = False
        self.last_updated: datetime = datetime.now()
    
    def add_event(self, event_name: str) -> None:
        """Добавить событие"""
        if not isinstance(event_name, str):
            raise TypeError("Название события должно быть строкой")
        if event_name not in self.__events:
            self.__events.append(event_name)
    
    def get_events(self) -> List[str]:
        """Получить список событий"""
        return self.__events.copy()
    
    def add_performance(self, performance_name: str) -> None:
        """Добавить спектакль"""
        if not isinstance(performance_name, str):
            raise TypeError("Название спектакля должно быть строкой")
        if performance_name not in self.__performances:
            self.__performances.append(performance_name)
    
    def get_performances(self) -> List[str]:
        """Получить список спектаклей"""
        return self.__performances.copy()
    
    def publish(self) -> None:
        """Опубликовать расписание"""
        self.is_published = True
        self.last_updated = datetime.now()
    
    events = property(get_events)
    performances = property(get_performances)

