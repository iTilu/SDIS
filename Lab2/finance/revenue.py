"""Класс дохода"""
from datetime import datetime
from typing import Optional


class Revenue:
    """Доход театра"""
    
    def __init__(self, description: str, amount: float, revenue_date: datetime):
        if not isinstance(description, str) or not description:
            raise ValueError("Описание должно быть непустой строкой")
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        if not isinstance(revenue_date, datetime):
            raise ValueError("Дата должна быть объектом datetime")
        
        self.description = description
        self.amount = float(amount)
        self.revenue_date = revenue_date
        self.source = ""
        self.is_recorded = False
        self.recorded_by: Optional[str] = None
    
    def set_source(self, source: str) -> None:
        """Установить источник"""
        if not isinstance(source, str):
            raise TypeError("Источник должен быть строкой")
        self.source = source
    
    def record(self, recorder_name: str) -> None:
        """Записать доход"""
        if not isinstance(recorder_name, str):
            raise TypeError("Имя записывающего должно быть строкой")
        self.is_recorded = True
        self.recorded_by = recorder_name
    
    def is_valid(self) -> bool:
        """Проверить валидность"""
        return self.is_recorded and self.amount > 0

