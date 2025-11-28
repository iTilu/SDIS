"""Класс бухгалтера"""
from typing import List


class Accountant:
    """Бухгалтер театра"""
    
    def __init__(self, name: str, age: int, experience_years: int, salary: float):
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")
        if not isinstance(experience_years, int) or experience_years < 0:
            raise ValueError("Опыт должен быть неотрицательным целым числом")
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Зарплата должна быть неотрицательным числом")
        
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.salary = salary
        self.__managed_accounts: List[str] = []
        self.certification = ""
        self.is_available = True
    
    def add_account(self, account_name: str) -> None:
        """Добавить счет"""
        if not isinstance(account_name, str):
            raise TypeError("Название счета должно быть строкой")
        if account_name not in self.__managed_accounts:
            self.__managed_accounts.append(account_name)
    
    def get_accounts(self) -> List[str]:
        """Получить список счетов"""
        return self.__managed_accounts.copy()
    
    def set_certification(self, cert: str) -> None:
        """Установить сертификацию"""
        if not isinstance(cert, str):
            raise TypeError("Сертификация должна быть строкой")
        self.certification = cert
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available
    
    accounts = property(get_accounts)

