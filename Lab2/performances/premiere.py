"""Класс премьеры"""
from datetime import datetime
from typing import Optional


class Premiere:
    """Премьера спектакля"""
    
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
        self.is_successful = False
        self.reviews_count = 0
        self.rating = 0.0
    
    def sell_ticket(self) -> None:
        """Продать билет"""
        self.tickets_sold += 1
    
    def get_tickets_sold(self) -> int:
        """Получить количество проданных билетов"""
        return self.tickets_sold
    
    def mark_successful(self) -> None:
        """Отметить как успешную"""
        self.is_successful = True
    
    def add_review(self) -> None:
        """Добавить отзыв"""
        self.reviews_count += 1
    
    def set_rating(self, rating: float) -> None:
        """Установить рейтинг"""
        if not isinstance(rating, (int, float)) or rating < 0 or rating > 10:
            raise ValueError("Рейтинг должен быть числом от 0 до 10")
        self.rating = float(rating)
    
    tickets_sold_count = property(get_tickets_sold)

