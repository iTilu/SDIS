"""Класс процессора данных"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from data.weather_data import WeatherData
    from data.measurement import Measurement
    from analysis.weather_analyzer import WeatherAnalyzer


class DataProcessor:
    """Процессор данных о погоде"""
    
    def __init__(self, processor_id: str, processing_method: str, output_format: str):
        if not isinstance(processor_id, str) or not processor_id:
            raise ValueError("ID процессора должен быть непустой строкой")
        if not isinstance(processing_method, str):
            raise TypeError("Метод обработки должен быть строкой")
        if not isinstance(output_format, str):
            raise TypeError("Формат вывода должен быть строкой")
        
        self.processor_id = processor_id
        self.processing_method = processing_method
        self.output_format = output_format
        self.__processed_data: List['WeatherData'] = []
        self.processing_speed: Optional[float] = None
        self.error_rate: Optional[float] = None
    
    def process_data(self, weather_data: 'WeatherData') -> None:
        """Обработать данные"""
        if weather_data not in self.__processed_data:
            self.__processed_data.append(weather_data)
    
    def get_processed_data(self) -> List['WeatherData']:
        """Получить обработанные данные"""
        return self.__processed_data.copy()
    
    def set_processing_speed(self, speed: float) -> None:
        """Установить скорость обработки"""
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError("Скорость должна быть неотрицательной")
        self.processing_speed = speed
    
    def processes_weather_data(self, weather_data: 'WeatherData') -> None:
        """Обрабатывает данные о погоде (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        weather_data.validate_data()
        self.process_data(weather_data)
    
    def processes_measurement(self, measurement: 'Measurement') -> None:
        """Обрабатывает измерение (ассоциация с Measurement)"""
        if measurement is None:
            raise ValueError("Измерение не может быть None")
        measurement.validate()
        # Измерение обрабатывается
    
    def extends_analyzer(self, analyzer: 'WeatherAnalyzer') -> None:
        """Расширяет анализатор (ассоциация с WeatherAnalyzer)"""
        if analyzer is None:
            raise ValueError("Анализатор не может быть None")
        # Процессор данных расширяет анализатор
    
    processed_data = property(get_processed_data)


