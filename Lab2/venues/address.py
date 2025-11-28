"""Класс адреса"""
from typing import Optional


class Address:
    """Адрес театра"""
    
    def __init__(self, street: str, city: str, country: str):
        if not isinstance(street, str) or not street:
            raise ValueError("Улица должна быть непустой строкой")
        if not isinstance(city, str) or not city:
            raise ValueError("Город должен быть непустой строкой")
        if not isinstance(country, str) or not country:
            raise ValueError("Страна должна быть непустой строкой")
        
        self.street = street
        self.city = city
        self.country = country
        self.building_number = ""
        self.postal_code: Optional[str] = None
        self.district = ""
    
    def set_building_number(self, number: str) -> None:
        """Установить номер здания"""
        if not isinstance(number, str):
            raise TypeError("Номер должен быть строкой")
        self.building_number = number
    
    def set_postal_code(self, code: str) -> None:
        """Установить почтовый индекс"""
        if not isinstance(code, str):
            raise TypeError("Индекс должен быть строкой")
        self.postal_code = code
    
    def set_district(self, district: str) -> None:
        """Установить район"""
        if not isinstance(district, str):
            raise TypeError("Район должен быть строкой")
        self.district = district
    
    def get_full_address(self) -> str:
        """Получить полный адрес"""
        parts = [self.street]
        if self.building_number:
            parts.append(self.building_number)
        parts.extend([self.city, self.country])
        if self.postal_code:
            parts.append(self.postal_code)
        return ", ".join(parts)

