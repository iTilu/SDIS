"""Класс метеоролога"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from forecasts.forecast import Forecast
    from models.weather_model import WeatherModel
    from data.weather_data import WeatherData
    from stations.weather_station import WeatherStation


class Meteorologist:
    """Метеоролог"""
    
    def __init__(self, employee_id: str, name: str, specialization: str, years_experience: int):
        if not isinstance(employee_id, str) or not employee_id:
            raise ValueError("ID сотрудника должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(specialization, str):
            raise TypeError("Специализация должна быть строкой")
        if not isinstance(years_experience, int) or years_experience < 0:
            raise ValueError("Опыт должен быть неотрицательным")
        
        self.employee_id = employee_id
        self.name = name
        self.specialization = specialization
        self.years_experience = years_experience
        self.__created_forecasts: List['Forecast'] = []
        self.certification_level: Optional[str] = None
        self.is_available = True
        self.department = "forecasting"
    
    def create_forecast(self, forecast: 'Forecast') -> None:
        """Создать прогноз"""
        if forecast not in self.__created_forecasts:
            self.__created_forecasts.append(forecast)
    
    def get_forecasts(self) -> List['Forecast']:
        """Получить прогнозы"""
        return self.__created_forecasts.copy()
    
    def set_certification(self, level: str) -> None:
        """Установить уровень сертификации"""
        if not isinstance(level, str):
            raise TypeError("Уровень должен быть строкой")
        self.certification_level = level
    
    def uses_model(self, model: 'WeatherModel') -> None:
        """Использует модель (ассоциация с WeatherModel)"""
        if model is None:
            raise ValueError("Модель не может быть None")
        if not model.is_active:
            raise ValueError("Модель неактивна")
        # Метеоролог использует модель для создания прогнозов
    
    def analyzes_data(self, weather_data: 'WeatherData') -> None:
        """Анализирует данные (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        # Метеоролог анализирует данные
        weather_data.validate_data()
    
    def works_at_station(self, station: 'WeatherStation') -> None:
        """Работает на станции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Станция не может быть None")
        if not station.is_operational:
            raise ValueError("Станция не работает")
        # Метеоролог работает на станции
    
    forecasts = property(get_forecasts)


