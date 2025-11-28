"""Класс зрительного зала"""
from typing import List


class Auditorium:
    """Зрительный зал театра"""
    
    def __init__(self, name: str, capacity: int):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")
        
        self.name = name
        self.capacity = capacity
        self.__sections: List[str] = []
        self.has_balcony = False
        self.has_orchestra = True
        self.acoustics_rating = 0.0
    
    def add_section(self, section_name: str) -> None:
        """Добавить секцию"""
        if not isinstance(section_name, str):
            raise TypeError("Название секции должно быть строкой")
        if section_name not in self.__sections:
            self.__sections.append(section_name)
    
    def get_sections(self) -> List[str]:
        """Получить список секций"""
        return self.__sections.copy()
    
    def set_has_balcony(self, has_balcony: bool) -> None:
        """Установить наличие балкона"""
        if not isinstance(has_balcony, bool):
            raise TypeError("Значение должно быть булевым")
        self.has_balcony = has_balcony
    
    def set_acoustics_rating(self, rating: float) -> None:
        """Установить рейтинг акустики"""
        if not isinstance(rating, (int, float)) or rating < 0 or rating > 10:
            raise ValueError("Рейтинг должен быть числом от 0 до 10")
        self.acoustics_rating = float(rating)
    
    def calculate_occupancy(self, tickets_sold: int) -> float:
        """Рассчитать заполненность"""
        if not isinstance(tickets_sold, int) or tickets_sold < 0:
            raise ValueError("Количество билетов должно быть неотрицательным")
        if self.capacity == 0:
            return 0.0
        return (tickets_sold / self.capacity) * 100
    
    sections = property(get_sections)

