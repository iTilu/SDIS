"""Класс продажи"""
from datetime import datetime
from typing import Optional


class Sale:
    """Продажа билетов"""
    
    def __init__(self, sale_number: str, ticket_number: str, amount: float):
        if not isinstance(sale_number, str) or not sale_number:
            raise ValueError("Номер продажи должен быть непустой строкой")
        if not isinstance(ticket_number, str) or not ticket_number:
            raise ValueError("Номер билета должен быть непустой строкой")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        
        self.sale_number = sale_number
        self.ticket_number = ticket_number
        self.amount = float(amount)
        self.sale_date: Optional[datetime] = None
        self.seller_name = ""
        self.payment_method = ""
    
    def complete_sale(self, sale_date: datetime, seller_name: str) -> None:
        """Завершить продажу"""
        if not isinstance(sale_date, datetime):
            raise TypeError("Дата продажи должна быть объектом datetime")
        if not isinstance(seller_name, str):
            raise TypeError("Имя продавца должно быть строкой")
        self.sale_date = sale_date
        self.seller_name = seller_name
    
    def set_payment_method(self, method: str) -> None:
        """Установить способ оплаты"""
        if not isinstance(method, str):
            raise TypeError("Способ оплаты должен быть строкой")
        self.payment_method = method
    
    def is_completed(self) -> bool:
        """Проверить завершенность продажи"""
        return self.sale_date is not None

