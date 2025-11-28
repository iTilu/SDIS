"""Класс бюджета"""
from typing import List


class Budget:
    """Бюджет театра"""
    
    def __init__(self, year: int, total_amount: float):
        if not isinstance(year, int) or year < 0:
            raise ValueError("Год должен быть неотрицательным целым числом")
        if not isinstance(total_amount, (int, float)) or total_amount < 0:
            raise ValueError("Общая сумма должна быть неотрицательным числом")
        
        self.year = year
        self.total_amount = float(total_amount)
        self.__expenses: List[float] = []
        self.__revenues: List[float] = []
        self.allocated_amount = 0.0
        self.remaining_amount = float(total_amount)
    
    def add_expense(self, amount: float) -> None:
        """Добавить расход"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        if amount > self.remaining_amount:
            raise ValueError("Недостаточно средств в бюджете")
        self.__expenses.append(float(amount))
        self.remaining_amount -= amount
    
    def add_revenue(self, amount: float) -> None:
        """Добавить доход"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        self.__revenues.append(float(amount))
        self.remaining_amount += amount
    
    def get_total_expenses(self) -> float:
        """Получить общие расходы"""
        return sum(self.__expenses)
    
    def get_total_revenues(self) -> float:
        """Получить общие доходы"""
        return sum(self.__revenues)
    
    def allocate(self, amount: float) -> None:
        """Выделить средства"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        if amount > self.remaining_amount:
            raise ValueError("Недостаточно средств")
        self.allocated_amount += amount
        self.remaining_amount -= amount
    
    def get_balance(self) -> float:
        """Получить баланс"""
        return self.total_amount + self.get_total_revenues() - self.get_total_expenses()

