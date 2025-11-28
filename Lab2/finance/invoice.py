"""Класс счета"""
from datetime import datetime
from typing import Optional


class Invoice:
    """Счет на оплату"""
    
    def __init__(self, invoice_number: str, amount: float, issue_date: datetime):
        if not isinstance(invoice_number, str) or not invoice_number:
            raise ValueError("Номер счета должен быть непустой строкой")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        if not isinstance(issue_date, datetime):
            raise ValueError("Дата должна быть объектом datetime")
        
        self.invoice_number = invoice_number
        self.amount = float(amount)
        self.issue_date = issue_date
        self.due_date: Optional[datetime] = None
        self.is_paid = False
        self.client_name = ""
    
    def set_due_date(self, due_date: datetime) -> None:
        """Установить срок оплаты"""
        if not isinstance(due_date, datetime):
            raise TypeError("Дата должна быть объектом datetime")
        self.due_date = due_date
    
    def set_client_name(self, name: str) -> None:
        """Установить имя клиента"""
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.client_name = name
    
    def pay(self) -> None:
        """Оплатить счет"""
        self.is_paid = True
    
    def is_overdue(self) -> bool:
        """Проверить просрочку"""
        if self.due_date is None:
            return False
        from datetime import datetime
        return datetime.now() > self.due_date and not self.is_paid

