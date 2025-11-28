"""Класс билета"""
from datetime import datetime
from typing import Optional


class Ticket:
    """Билет на спектакль"""
    
    def __init__(self, ticket_number: str, performance_name: str, price: float, seat_number: str):
        if not isinstance(ticket_number, str) or not ticket_number:
            raise ValueError("Номер билета должен быть непустой строкой")
        if not isinstance(performance_name, str) or not performance_name:
            raise ValueError("Название спектакля должно быть непустой строкой")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена должна быть неотрицательным числом")
        if not isinstance(seat_number, str) or not seat_number:
            raise ValueError("Номер места должен быть непустой строкой")
        
        self.ticket_number = ticket_number
        self.performance_name = performance_name
        self.price = float(price)
        self.seat_number = seat_number
        self.purchase_date: Optional[datetime] = None
        self.is_sold = False
        self.is_used = False
        self.section = ""
    
    def sell(self, purchase_date: datetime) -> None:
        """Продать билет"""
        if not isinstance(purchase_date, datetime):
            raise TypeError("Дата покупки должна быть объектом datetime")
        self.is_sold = True
        self.purchase_date = purchase_date
    
    def use(self) -> None:
        """Использовать билет"""
        if not self.is_sold:
            raise ValueError("Билет должен быть продан перед использованием")
        self.is_used = True
    
    def set_section(self, section: str) -> None:
        """Установить секцию"""
        if not isinstance(section, str):
            raise TypeError("Секция должна быть строкой")
        self.section = section
    
    def is_valid(self) -> bool:
        """Проверить валидность билета"""
        return self.is_sold and not self.is_used

