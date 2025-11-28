"""Класс возврата"""
from datetime import datetime
from typing import Optional


class Refund:
    """Возврат билета"""
    
    def __init__(self, refund_number: str, ticket_number: str, amount: float):
        if not isinstance(refund_number, str) or not refund_number:
            raise ValueError("Номер возврата должен быть непустой строкой")
        if not isinstance(ticket_number, str) or not ticket_number:
            raise ValueError("Номер билета должен быть непустой строкой")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        
        self.refund_number = refund_number
        self.ticket_number = ticket_number
        self.amount = float(amount)
        self.refund_date: Optional[datetime] = None
        self.reason = ""
        self.is_processed = False
    
    def process_refund(self, refund_date: datetime, reason: str) -> None:
        """Обработать возврат"""
        if not isinstance(refund_date, datetime):
            raise TypeError("Дата возврата должна быть объектом datetime")
        if not isinstance(reason, str):
            raise TypeError("Причина должна быть строкой")
        self.refund_date = refund_date
        self.reason = reason
        self.is_processed = True
    
    def set_reason(self, reason: str) -> None:
        """Установить причину"""
        if not isinstance(reason, str):
            raise TypeError("Причина должна быть строкой")
        self.reason = reason
    
    def is_valid(self) -> bool:
        """Проверить валидность возврата"""
        return self.is_processed and self.refund_date is not None

