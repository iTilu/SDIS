"""Класс расхода"""
from datetime import datetime
from typing import Optional


class Expense:
    """Расход театра"""
    
    def __init__(self, description: str, amount: float, expense_date: datetime):
        if not isinstance(description, str) or not description:
            raise ValueError("Описание должно быть непустой строкой")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        if not isinstance(expense_date, datetime):
            raise ValueError("Дата должна быть объектом datetime")
        
        self.description = description
        self.amount = float(amount)
        self.expense_date = expense_date
        self.category = ""
        self.is_approved = False
        self.approved_by: Optional[str] = None
    
    def set_category(self, category: str) -> None:
        """Установить категорию"""
        if not isinstance(category, str):
            raise TypeError("Категория должна быть строкой")
        self.category = category
    
    def approve(self, approver_name: str) -> None:
        """Одобрить расход"""
        if not isinstance(approver_name, str):
            raise TypeError("Имя одобряющего должно быть строкой")
        self.is_approved = True
        self.approved_by = approver_name
    
    def is_valid(self) -> bool:
        """Проверить валидность"""
        return self.is_approved and self.amount > 0

