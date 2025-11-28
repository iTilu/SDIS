"""Класс показа"""
from datetime import datetime
from typing import Optional


class Show:
    """Показ спектакля"""
    
    def __init__(self, performance_name: str, date: datetime, venue_name: str):
        if not isinstance(performance_name, str) or not performance_name:
            raise ValueError("Название спектакля должно быть непустой строкой")
        if not isinstance(date, datetime):
            raise ValueError("Дата должна быть объектом datetime")
        if not isinstance(venue_name, str) or not venue_name:
            raise ValueError("Название площадки должно быть непустой строкой")
        
        self.performance_name = performance_name
        self.date = date
        self.venue_name = venue_name
        self.tickets_sold = 0
        self.tickets_available = 0
        self.is_cancelled = False
        self.start_time: Optional[datetime] = None
    
    def sell_ticket(self) -> None:
        """Продать билет"""
        if self.tickets_available > 0:
            self.tickets_sold += 1
            self.tickets_available -= 1
    
    def set_tickets_available(self, count: int) -> None:
        """Установить доступные билеты"""
        if not isinstance(count, int) or count < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")
        self.tickets_available = count
    
    def cancel(self) -> None:
        """Отменить показ"""
        self.is_cancelled = True
    
    def set_start_time(self, time: datetime) -> None:
        """Установить время начала"""
        if not isinstance(time, datetime):
            raise TypeError("Время должно быть объектом datetime")
        self.start_time = time
    
    def get_occupancy_rate(self) -> float:
        """Получить процент заполненности"""
        total = self.tickets_sold + self.tickets_available
        if total == 0:
            return 0.0
        return (self.tickets_sold / total) * 100

