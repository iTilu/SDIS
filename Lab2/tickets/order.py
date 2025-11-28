"""Класс заказа"""
from typing import List
from datetime import datetime


class Order:
    """Заказ билетов"""
    
    def __init__(self, order_number: str, customer_name: str, order_date: datetime):
        if not isinstance(order_number, str) or not order_number:
            raise ValueError("Номер заказа должен быть непустой строкой")
        if not isinstance(customer_name, str) or not customer_name:
            raise ValueError("Имя клиента должно быть непустой строкой")
        if not isinstance(order_date, datetime):
            raise ValueError("Дата заказа должна быть объектом datetime")
        
        self.order_number = order_number
        self.customer_name = customer_name
        self.order_date = order_date
        self.__tickets: List[str] = []
        self.total_amount = 0.0
        self.is_paid = False
        self.is_cancelled = False
    
    def add_ticket(self, ticket_number: str) -> None:
        """Добавить билет"""
        if not isinstance(ticket_number, str):
            raise TypeError("Номер билета должен быть строкой")
        if ticket_number not in self.__tickets:
            self.__tickets.append(ticket_number)
    
    def remove_ticket(self, ticket_number: str) -> None:
        """Удалить билет"""
        if ticket_number in self.__tickets:
            self.__tickets.remove(ticket_number)
    
    def get_tickets(self) -> List[str]:
        """Получить список билетов"""
        return self.__tickets.copy()
    
    def set_total_amount(self, amount: float) -> None:
        """Установить общую сумму"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        self.total_amount = float(amount)
    
    def pay(self) -> None:
        """Оплатить заказ"""
        self.is_paid = True
    
    def cancel(self) -> None:
        """Отменить заказ"""
        self.is_cancelled = True
    
    tickets = property(get_tickets)

