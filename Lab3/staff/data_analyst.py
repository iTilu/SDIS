"""Класс аналитика данных"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from data.weather_data import WeatherData
    from data.historical_data import HistoricalData
    from analysis.weather_analyzer import WeatherAnalyzer


class DataAnalyst:
    """Аналитик данных"""
    
    def __init__(self, employee_id: str, name: str, specialization: str, tools: List[str]):
        if not isinstance(employee_id, str) or not employee_id:
            raise ValueError("ID сотрудника должен быть непустой строкой")
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(specialization, str):
            raise TypeError("Специализация должна быть строкой")
        if not isinstance(tools, list):
            raise TypeError("Инструменты должны быть списком")
        
        self.employee_id = employee_id
        self.name = name
        self.specialization = specialization
        self.tools = tools
        self.__analyzed_data: List['WeatherData'] = []
        self.reports_generated = 0
        self.department = "data_science"
    
    def analyze_data(self, weather_data: 'WeatherData') -> None:
        """Анализировать данные"""
        if weather_data not in self.__analyzed_data:
            self.__analyzed_data.append(weather_data)
    
    def get_analyzed_data(self) -> List['WeatherData']:
        """Получить проанализированные данные"""
        return self.__analyzed_data.copy()
    
    def analyzes_weather_data(self, weather_data: 'WeatherData') -> None:
        """Анализирует данные о погоде (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        self.analyze_data(weather_data)
    
    def analyzes_historical(self, historical_data: 'HistoricalData') -> None:
        """Анализирует исторические данные (ассоциация с HistoricalData)"""
        if historical_data is None:
            raise ValueError("Исторические данные не могут быть None")
        historical_data.calculate_averages()
    
    def uses_analyzer(self, analyzer: 'WeatherAnalyzer') -> None:
        """Использует анализатор (ассоциация с WeatherAnalyzer)"""
        if analyzer is None:
            raise ValueError("Анализатор не может быть None")
        # Аналитик использует анализатор
    
    analyzed_data = property(get_analyzed_data)


