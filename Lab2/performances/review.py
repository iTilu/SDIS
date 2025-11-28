"""Класс отзыва"""
from datetime import datetime
from typing import Optional


class Review:
    """Отзыв на спектакль"""
    
    def __init__(self, performance_name: str, reviewer_name: str, rating: float, comment: str):
        if not isinstance(performance_name, str) or not performance_name:
            raise ValueError("Название спектакля должно быть непустой строкой")
        if not isinstance(reviewer_name, str) or not reviewer_name:
            raise ValueError("Имя рецензента должно быть непустой строкой")
        if not isinstance(rating, (int, float)) or rating < 0 or rating > 10:
            raise ValueError("Рейтинг должен быть числом от 0 до 10")
        if not isinstance(comment, str):
            raise ValueError("Комментарий должен быть строкой")
        
        self.performance_name = performance_name
        self.reviewer_name = reviewer_name
        self.rating = float(rating)
        self.comment = comment
        self.review_date: datetime = datetime.now()
        self.is_published = False
        self.is_verified = False
    
    def publish(self) -> None:
        """Опубликовать отзыв"""
        self.is_published = True
    
    def verify(self) -> None:
        """Верифицировать отзыв"""
        self.is_verified = True
    
    def set_review_date(self, date: datetime) -> None:
        """Установить дату отзыва"""
        if not isinstance(date, datetime):
            raise TypeError("Дата должна быть объектом datetime")
        self.review_date = date
    
    def is_positive(self) -> bool:
        """Проверить положительный ли отзыв"""
        return self.rating >= 7.0

