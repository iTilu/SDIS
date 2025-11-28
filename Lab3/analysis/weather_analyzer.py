"""Класс анализатора погоды"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from data.weather_data import WeatherData
    from data.historical_data import HistoricalData
    from staff.data_analyst import DataAnalyst


class WeatherAnalyzer:
    """Анализатор погодных данных"""
    
    def __init__(self, analyzer_id: str, analysis_type: str, algorithms: List[str]):
        if not isinstance(analyzer_id, str) or not analyzer_id:
            raise ValueError("ID анализатора должен быть непустой строкой")
        if not isinstance(analysis_type, str):
            raise TypeError("Тип анализа должен быть строкой")
        if not isinstance(algorithms, list):
            raise TypeError("Алгоритмы должны быть списком")
        
        self.analyzer_id = analyzer_id
        self.analysis_type = analysis_type
        self.algorithms = algorithms
        self.__analyzed_data: List['WeatherData'] = []
        self.analysis_count = 0
        self.processing_time: Optional[float] = None
    
    def analyze(self, weather_data: 'WeatherData') -> None:
        """Анализировать данные"""
        if weather_data not in self.__analyzed_data:
            self.__analyzed_data.append(weather_data)
            self.analysis_count = len(self.__analyzed_data)
    
    def get_analyzed_data(self) -> List['WeatherData']:
        """Получить проанализированные данные"""
        return self.__analyzed_data.copy()
    
    def analyzes_weather_data(self, weather_data: 'WeatherData') -> None:
        """Анализирует данные о погоде (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        self.analyze(weather_data)
    
    def analyzes_historical(self, historical_data: 'HistoricalData') -> None:
        """Анализирует исторические данные (ассоциация с HistoricalData)"""
        if historical_data is None:
            raise ValueError("Исторические данные не могут быть None")
        historical_data.calculate_averages()
        for data_point in historical_data.get_data_points():
            self.analyze(data_point)
    
    def used_by_analyst(self, analyst: 'DataAnalyst') -> None:
        """Используется аналитиком (ассоциация с DataAnalyst)"""
        if analyst is None:
            raise ValueError("Аналитик не может быть None")
        # Анализатор используется аналитиком
    
    analyzed_data = property(get_analyzed_data)


