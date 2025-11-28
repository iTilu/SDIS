"""Класс сеанса"""
from datetime import datetime
from typing import Optional


class Session:
    """Сеанс спектакля"""
    
    def __init__(self, performance_name: str, start_time: datetime, venue_name: str):
        if not isinstance(performance_name, str) or not performance_name:
            raise ValueError("Название спектакля должно быть непустой строкой")
        if not isinstance(start_time, datetime):
            raise ValueError("Время начала должно быть объектом datetime")
        if not isinstance(venue_name, str) or not venue_name:
            raise ValueError("Название площадки должно быть непустой строкой")
        
        self.performance_name = performance_name
        self.start_time = start_time
        self.venue_name = venue_name
        self.end_time: Optional[datetime] = None
        self.tickets_sold = 0
        self.is_sold_out = False
        self.director_name = ""
    
    def set_end_time(self, end_time: datetime) -> None:
        """Установить время окончания"""
        if not isinstance(end_time, datetime):
            raise TypeError("Время должно быть объектом datetime")
        if end_time <= self.start_time:
            raise ValueError("Время окончания должно быть позже времени начала")
        self.end_time = end_time
    
    def sell_ticket(self) -> None:
        """Продать билет"""
        self.tickets_sold += 1
    
    def check_sold_out(self, capacity: int) -> None:
        """Проверить распродажу"""
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Вместимость должна быть неотрицательным целым числом")
        self.is_sold_out = self.tickets_sold >= capacity
    
    def set_director_name(self, name: str) -> None:
        """Установить имя режиссера"""
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.director_name = name
    
    def get_duration_minutes(self) -> int:
        """Получить длительность в минутах"""
        if self.end_time is None:
            return 0
        delta = self.end_time - self.start_time
        return int(delta.total_seconds() / 60)

