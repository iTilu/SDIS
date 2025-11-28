"""Класс численной модели"""
from typing import Optional, TYPE_CHECKING
from exceptions.weather_exceptions import ModelException

if TYPE_CHECKING:
    from models.weather_model import WeatherModel
    from forecasts.forecast import Forecast


class NumericalModel:
    """Численная модель прогноза"""
    
    def __init__(self, model_id: str, resolution: float, grid_size: int, time_step: float):
        if not isinstance(model_id, str) or not model_id:
            raise ValueError("ID модели должен быть непустой строкой")
        if not isinstance(resolution, (int, float)) or resolution <= 0:
            raise ValueError("Разрешение должно быть положительным")
        if not isinstance(grid_size, int) or grid_size <= 0:
            raise ValueError("Размер сетки должен быть положительным")
        if not isinstance(time_step, (int, float)) or time_step <= 0:
            raise ValueError("Шаг времени должен быть положительным")
        
        self.model_id = model_id
        self.resolution = resolution
        self.grid_size = grid_size
        self.time_step = time_step
        self.computation_time: Optional[float] = None
        self.memory_usage: Optional[float] = None
        self.parallel_processing = True
    
    def set_computation_time(self, time: float) -> None:
        """Установить время вычисления"""
        if not isinstance(time, (int, float)) or time < 0:
            raise ValueError("Время должно быть неотрицательным")
        self.computation_time = time
    
    def set_memory_usage(self, memory: float) -> None:
        """Установить использование памяти"""
        if not isinstance(memory, (int, float)) or memory < 0:
            raise ValueError("Память должна быть неотрицательной")
        self.memory_usage = memory
    
    def extends_weather_model(self, model: 'WeatherModel') -> None:
        """Расширяет модель погоды (ассоциация с WeatherModel)"""
        if model is None:
            raise ValueError("Модель погоды не может быть None")
        if not model.is_active:
            raise ValueError("Модель неактивна")
        # Численная модель расширяет базовую модель
    
    def generates_forecast(self, forecast: 'Forecast') -> None:
        """Генерирует прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        # Численная модель генерирует прогноз


