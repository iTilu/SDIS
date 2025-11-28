"""Класс зарплаты"""
from typing import List
from datetime import datetime


class Salary:
    """Зарплата сотрудника"""
    
    def __init__(self, employee_name: str, base_salary: float, payment_date: datetime):
        if not isinstance(employee_name, str) or not employee_name:
            raise ValueError("Имя сотрудника должно быть непустой строкой")
        if not isinstance(base_salary, (int, float)) or base_salary < 0:
            raise ValueError("Базовая зарплата должна быть неотрицательным числом")
        if not isinstance(payment_date, datetime):
            raise ValueError("Дата выплаты должна быть объектом datetime")
        
        self.employee_name = employee_name
        self.base_salary = float(base_salary)
        self.payment_date = payment_date
        self.bonuses: List[float] = []
        self.deductions: List[float] = []
        self.is_paid = False
        self.tax_rate = 0.13
    
    def add_bonus(self, amount: float) -> None:
        """Добавить премию"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        self.bonuses.append(float(amount))
    
    def add_deduction(self, amount: float) -> None:
        """Добавить удержание"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        self.deductions.append(float(amount))
    
    def calculate_gross_salary(self) -> float:
        """Рассчитать валовую зарплату"""
        return self.base_salary + sum(self.bonuses) - sum(self.deductions)
    
    def calculate_net_salary(self) -> float:
        """Рассчитать чистую зарплату"""
        gross = self.calculate_gross_salary()
        tax = gross * self.tax_rate
        return gross - tax
    
    def pay(self) -> None:
        """Выплатить зарплату"""
        self.is_paid = True
    
    def set_tax_rate(self, rate: float) -> None:
        """Установить налоговую ставку"""
        if not isinstance(rate, (int, float)) or rate < 0 or rate > 1:
            raise ValueError("Ставка должна быть числом от 0 до 1")
        self.tax_rate = float(rate)

