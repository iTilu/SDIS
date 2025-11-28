"""Класс места"""
from typing import Optional


class Seat:
    """Место в зале"""
    
    def __init__(self, seat_number: str, row: int, section: str):
        if not isinstance(seat_number, str) or not seat_number:
            raise ValueError("Номер места должен быть непустой строкой")
        if not isinstance(row, int) or row < 0:
            raise ValueError("Ряд должен быть неотрицательным целым числом")
        if not isinstance(section, str) or not section:
            raise ValueError("Секция должна быть непустой строкой")
        
        self.seat_number = seat_number
        self.row = row
        self.section = section
        self.is_occupied = False
        self.price_multiplier = 1.0
        self.view_quality = ""
    
    def occupy(self) -> None:
        """Занять место"""
        self.is_occupied = True
    
    def release(self) -> None:
        """Освободить место"""
        self.is_occupied = False
    
    def set_price_multiplier(self, multiplier: float) -> None:
        """Установить множитель цены"""
        if not isinstance(multiplier, (int, float)) or multiplier < 0:
            raise ValueError("Множитель должен быть неотрицательным числом")
        self.price_multiplier = float(multiplier)
    
    def set_view_quality(self, quality: str) -> None:
        """Установить качество обзора"""
        if not isinstance(quality, str):
            raise TypeError("Качество должно быть строкой")
        self.view_quality = quality
    
    def calculate_price(self, base_price: float) -> float:
        """Рассчитать цену"""
        if not isinstance(base_price, (int, float)) or base_price < 0:
            raise ValueError("Базовая цена должна быть неотрицательным числом")
        return base_price * self.price_multiplier

