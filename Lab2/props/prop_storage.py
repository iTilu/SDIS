"""Класс хранилища реквизита"""
from typing import List


class PropStorage:
    """Хранилище реквизита"""
    
    def __init__(self, name: str, capacity: int):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")
        
        self.name = name
        self.capacity = capacity
        self.__props: List[str] = []
        self.temperature = 20.0
        self.humidity = 50.0
        self.is_climate_controlled = False
    
    def add_prop(self, prop_name: str) -> None:
        """Добавить реквизит"""
        if not isinstance(prop_name, str):
            raise TypeError("Название реквизита должно быть строкой")
        if len(self.__props) < self.capacity:
            if prop_name not in self.__props:
                self.__props.append(prop_name)
    
    def remove_prop(self, prop_name: str) -> None:
        """Удалить реквизит"""
        if prop_name in self.__props:
            self.__props.remove(prop_name)
    
    def get_props(self) -> List[str]:
        """Получить список реквизита"""
        return self.__props.copy()
    
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
        return len(self.__props) >= self.capacity
    
    props = property(get_props)

