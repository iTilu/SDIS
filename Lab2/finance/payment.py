"""Класс платежа"""
from datetime import datetime
from typing import Optional


class Payment:
    """Платеж"""
    
    def __init__(self, payment_number: str, amount: float, payment_date: datetime):
        if not isinstance(payment_number, str) or not payment_number:
            raise ValueError("Номер платежа должен быть непустой строкой")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        if not isinstance(payment_date, datetime):
            raise ValueError("Дата должна быть объектом datetime")
        
        self.payment_number = payment_number
        self.amount = float(amount)
        self.payment_date = payment_date
        self.payment_method = ""
        self.is_completed = False
        self.recipient: Optional[str] = None
    
    def set_payment_method(self, method: str) -> None:
        """Установить способ оплаты"""
        if not isinstance(method, str):
            raise TypeError("Способ оплаты должен быть строкой")
        self.payment_method = method
    
    def set_recipient(self, recipient: str) -> None:
        """Установить получателя"""
        if not isinstance(recipient, str):
            raise TypeError("Получатель должен быть строкой")
        self.recipient = recipient
    
    def complete(self) -> None:
        """Завершить платеж"""
        self.is_completed = True
    
    def is_valid(self) -> bool:
        """Проверить валидность"""
        return self.is_completed and self.recipient is not None

