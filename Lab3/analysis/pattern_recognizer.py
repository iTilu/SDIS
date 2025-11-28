"""Класс распознавателя паттернов"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from data.historical_data import HistoricalData
    from analysis.weather_analyzer import WeatherAnalyzer


class PatternRecognizer:
    """Распознаватель паттернов погоды"""
    
    def __init__(self, recognizer_id: str, pattern_types: List[str], recognition_accuracy: float):
        if not isinstance(recognizer_id, str) or not recognizer_id:
            raise ValueError("ID распознавателя должен быть непустой строкой")
        if not isinstance(pattern_types, list):
            raise TypeError("Типы паттернов должны быть списком")
        if not isinstance(recognition_accuracy, (int, float)) or recognition_accuracy < 0 or recognition_accuracy > 100:
            raise ValueError("Точность должна быть от 0 до 100")
        
        self.recognizer_id = recognizer_id
        self.pattern_types = pattern_types
        self.recognition_accuracy = recognition_accuracy
        self.recognized_patterns: List[str] = []
        self.pattern_count = 0
        self.machine_learning_enabled = True
    
    def recognize_pattern(self, pattern: str) -> None:
        """Распознать паттерн"""
        if not isinstance(pattern, str):
            raise TypeError("Паттерн должен быть строкой")
        if pattern not in self.recognized_patterns:
            self.recognized_patterns.append(pattern)
            self.pattern_count = len(self.recognized_patterns)
    
    def analyzes_historical(self, historical_data: 'HistoricalData') -> None:
        """Анализирует исторические данные (ассоциация с HistoricalData)"""
        if historical_data is None:
            raise ValueError("Исторические данные не могут быть None")
        if historical_data.data_count > 100:
            self.recognize_pattern("seasonal")
        if historical_data.average_temperature is not None:
            self.recognize_pattern("temperature_variation")
    
    def extends_analyzer(self, analyzer: 'WeatherAnalyzer') -> None:
        """Расширяет анализатор (ассоциация с WeatherAnalyzer)"""
        if analyzer is None:
            raise ValueError("Анализатор не может быть None")
        # Распознаватель паттернов расширяет базовый анализатор


