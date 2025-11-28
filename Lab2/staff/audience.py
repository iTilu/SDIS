"""Класс зрителя"""
from typing import List


class Audience:
    """Зритель театра"""
    
    def __init__(self, name: str, age: int, email: str):
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")
        if not isinstance(email, str) or not email:
            raise ValueError("Email должен быть непустой строкой")
        
        self.name = name
        self.age = age
        self.email = email
        self.__tickets_purchased: List[str] = []
        self.loyalty_points = 0
        self.is_member = False
        self.membership_type = ""
    
    def purchase_ticket(self, ticket_number: str) -> None:
        """Купить билет"""
        if not isinstance(ticket_number, str):
            raise TypeError("Номер билета должен быть строкой")
        if ticket_number not in self.__tickets_purchased:
            self.__tickets_purchased.append(ticket_number)
            self.loyalty_points += 10
    
    def get_tickets_purchased(self) -> List[str]:
        """Получить список купленных билетов"""
        return self.__tickets_purchased.copy()
    
    def add_loyalty_points(self, points: int) -> None:
        """Добавить баллы лояльности"""
        if not isinstance(points, int) or points < 0:
            raise ValueError("Баллы должны быть неотрицательным целым числом")
        self.loyalty_points += points
    
    def become_member(self, membership_type: str) -> None:
        """Стать членом"""
        if not isinstance(membership_type, str):
            raise TypeError("Тип членства должен быть строкой")
        self.is_member = True
        self.membership_type = membership_type
    
    tickets_purchased = property(get_tickets_purchased)

