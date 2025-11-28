"""Класс анализатора трендов"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from data.historical_data import HistoricalData
    from analysis.weather_analyzer import WeatherAnalyzer


class TrendAnalyzer:
    """Анализатор трендов погоды"""
    
    def __init__(self, analyzer_id: str, trend_period_days: int, sensitivity: float):
        if not isinstance(analyzer_id, str) or not analyzer_id:
            raise ValueError("ID анализатора должен быть непустой строкой")
        if not isinstance(trend_period_days, int) or trend_period_days < 0:
            raise ValueError("Период должен быть неотрицательным")
        if not isinstance(sensitivity, (int, float)) or sensitivity < 0:
            raise ValueError("Чувствительность должна быть неотрицательной")
        
        self.analyzer_id = analyzer_id
        self.trend_period_days = trend_period_days
        self.sensitivity = sensitivity
        self.identified_trends: List[str] = []
        self.trend_strength: Optional[float] = None
        self.confidence_score: Optional[float] = None
    
    def add_trend(self, trend: str) -> None:
        """Добавить тренд"""
        if not isinstance(trend, str):
            raise TypeError("Тренд должен быть строкой")
        if trend not in self.identified_trends:
            self.identified_trends.append(trend)
    
    def set_trend_strength(self, strength: float) -> None:
        """Установить силу тренда"""
        if not isinstance(strength, (int, float)) or strength < 0 or strength > 100:
            raise ValueError("Сила тренда должна быть от 0 до 100")
        self.trend_strength = strength
    
    def analyzes_historical(self, historical_data: 'HistoricalData') -> None:
        """Анализирует исторические данные (ассоциация с HistoricalData)"""
        if historical_data is None:
            raise ValueError("Исторические данные не могут быть None")
        historical_data.calculate_averages()
        if historical_data.average_temperature is not None:
            if historical_data.average_temperature > 20:
                self.add_trend("warming")
            else:
                self.add_trend("cooling")
    
    def extends_analyzer(self, analyzer: 'WeatherAnalyzer') -> None:
        """Расширяет анализатор (ассоциация с WeatherAnalyzer)"""
        if analyzer is None:
            raise ValueError("Анализатор не может быть None")
        # Анализатор трендов расширяет базовый анализатор


