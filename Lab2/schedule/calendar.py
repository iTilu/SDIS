"""Класс календаря"""
from typing import List
from datetime import datetime


class Calendar:
    """Календарь театра"""
    
    def __init__(self, year: int):
        if not isinstance(year, int) or year < 0:
            raise ValueError("Год должен быть неотрицательным целым числом")
        
        self.year = year
        self.__holidays: List[datetime] = []
        self.__special_dates: List[datetime] = []
        self.season_start: datetime = datetime(year, 9, 1)
        self.season_end: datetime = datetime(year + 1, 6, 30)
    
    def add_holiday(self, date: datetime) -> None:
        """Добавить праздник"""
        if not isinstance(date, datetime):
            raise TypeError("Дата должна быть объектом datetime")
        if date.year != self.year:
            raise ValueError("Дата должна быть в текущем году")
        if date not in self.__holidays:
            self.__holidays.append(date)
    
    def get_holidays(self) -> List[datetime]:
        """Получить список праздников"""
        return self.__holidays.copy()
    
    def add_special_date(self, date: datetime) -> None:
        """Добавить особую дату"""
        if not isinstance(date, datetime):
            raise TypeError("Дата должна быть объектом datetime")
        if date not in self.__special_dates:
            self.__special_dates.append(date)
    
    def get_special_dates(self) -> List[datetime]:
        """Получить список особых дат"""
        return self.__special_dates.copy()
    
    def set_season(self, start: datetime, end: datetime) -> None:
        """Установить сезон"""
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise TypeError("Даты должны быть объектами datetime")
        if end <= start:
            raise ValueError("Дата окончания должна быть позже даты начала")
        self.season_start = start
        self.season_end = end
    
    holidays = property(get_holidays)
    special_dates = property(get_special_dates)

