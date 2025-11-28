"""Класс гардероба"""
from typing import List


class Wardrobe:
    """Гардероб театра"""
    
    def __init__(self, name: str, capacity: int):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")
        
        self.name = name
        self.capacity = capacity
        self.__costumes: List[str] = []
        self.temperature = 20.0
        self.humidity = 50.0
        self.is_climate_controlled = True
    
    def add_costume(self, costume_name: str) -> None:
        """Добавить костюм"""
        if not isinstance(costume_name, str):
            raise TypeError("Название костюма должно быть строкой")
        if len(self.__costumes) < self.capacity:
            if costume_name not in self.__costumes:
                self.__costumes.append(costume_name)
    
    def remove_costume(self, costume_name: str) -> None:
        """Удалить костюм"""
        if costume_name in self.__costumes:
            self.__costumes.remove(costume_name)
    
    def get_costumes(self) -> List[str]:
        """Получить список костюмов"""
        return self.__costumes.copy()
    
    def set_temperature(self, temp: float) -> None:
        """Установить температуру"""
        if not isinstance(temp, (int, float)):
            raise TypeError("Температура должна быть числом")
        self.temperature = float(temp)
    
    def set_humidity(self, humidity: float) -> None:
        """Установить влажность"""
        if not isinstance(humidity, (int, float)) or humidity < 0 or humidity > 100:
            raise ValueError("Влажность должна быть числом от 0 до 100")
        self.humidity = float(humidity)
    
    def is_full(self) -> bool:
        """Проверить заполненность"""
        return len(self.__costumes) >= self.capacity
    
    costumes = property(get_costumes)

