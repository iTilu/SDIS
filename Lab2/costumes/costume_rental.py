"""Класс проката костюмов"""
from typing import List
from datetime import datetime, timedelta


class CostumeRental:
    """Прокат костюма"""
    
    def __init__(self, costume_name: str, actor_name: str, start_date: datetime):
        if not isinstance(costume_name, str) or not costume_name:
            raise ValueError("Название костюма должно быть непустой строкой")
        if not isinstance(actor_name, str) or not actor_name:
            raise ValueError("Имя актера должно быть непустой строкой")
        if not isinstance(start_date, datetime):
            raise ValueError("Дата начала должна быть объектом datetime")
        
        self.costume_name = costume_name
        self.actor_name = actor_name
        self.start_date = start_date
        self.end_date: datetime = start_date + timedelta(days=30)
        self.rental_fee = 0.0
        self.is_returned = False
        self.damage_fee = 0.0
    
    def set_end_date(self, end_date: datetime) -> None:
        """Установить дату окончания"""
        if not isinstance(end_date, datetime):
            raise TypeError("Дата должна быть объектом datetime")
        if end_date < self.start_date:
            raise ValueError("Дата окончания должна быть позже даты начала")
        self.end_date = end_date
    
    def set_rental_fee(self, fee: float) -> None:
        """Установить плату за прокат"""
        if not isinstance(fee, (int, float)) or fee < 0:
            raise ValueError("Плата должна быть неотрицательным числом")
        self.rental_fee = float(fee)
    
    def return_costume(self) -> None:
        """Вернуть костюм"""
        self.is_returned = True
    
    def add_damage_fee(self, fee: float) -> None:
        """Добавить плату за повреждение"""
        if not isinstance(fee, (int, float)) or fee < 0:
            raise ValueError("Плата должна быть неотрицательным числом")
        self.damage_fee += fee
    
    def calculate_total_fee(self) -> float:
        """Рассчитать общую плату"""
        return self.rental_fee + self.damage_fee

