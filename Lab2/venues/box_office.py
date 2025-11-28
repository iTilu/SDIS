"""Класс кассы"""
from typing import List


class BoxOffice:
    """Касса театра"""
    
    def __init__(self, number: int, location: str):
        if not isinstance(number, int) or number < 0:
            raise ValueError("Номер должен быть неотрицательным целым числом")
        if not isinstance(location, str) or not location:
            raise ValueError("Местоположение должно быть непустой строкой")
        
        self.number = number
        self.location = location
        self.__sellers: List[str] = []
        self.daily_revenue = 0.0
        self.tickets_sold_today = 0
        self.is_open = False
    
    def add_seller(self, seller_name: str) -> None:
        """Добавить продавца"""
        if not isinstance(seller_name, str):
            raise TypeError("Имя продавца должно быть строкой")
        if seller_name not in self.__sellers:
            self.__sellers.append(seller_name)
    
    def get_sellers(self) -> List[str]:
        """Получить список продавцов"""
        return self.__sellers.copy()
    
    def add_revenue(self, amount: float) -> None:
        """Добавить доход"""
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма должна быть неотрицательным числом")
        self.daily_revenue += amount
    
    def sell_ticket(self) -> None:
        """Продать билет"""
        self.tickets_sold_today += 1
    
    def open(self) -> None:
        """Открыть кассу"""
        self.is_open = True
    
    def close(self) -> None:
        """Закрыть кассу"""
        self.is_open = False
    
    def reset_daily_stats(self) -> None:
        """Сбросить дневную статистику"""
        self.daily_revenue = 0.0
        self.tickets_sold_today = 0
    
    sellers = property(get_sellers)

