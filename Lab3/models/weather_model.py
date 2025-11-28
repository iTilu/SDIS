"""Класс модели погоды"""
from typing import Optional, List, TYPE_CHECKING
from exceptions.weather_exceptions import ModelException

if TYPE_CHECKING:
    from forecasts.forecast import Forecast
    from data.weather_data import WeatherData
    from staff.meteorologist import Meteorologist


class WeatherModel:
    """Модель прогноза погоды"""
    
    def __init__(self, model_id: str, model_name: str, model_type: str, version: str):
        if not isinstance(model_id, str) or not model_id:
            raise ValueError("ID модели должен быть непустой строкой")
        if not isinstance(model_name, str) or not model_name:
            raise ValueError("Название модели должно быть непустой строкой")
        if not isinstance(model_type, str):
            raise TypeError("Тип модели должен быть строкой")
        if not isinstance(version, str):
            raise TypeError("Версия должна быть строкой")
        
        self.model_id = model_id
        self.model_name = model_name
        self.model_type = model_type
        self.version = version
        self.__generated_forecasts: List['Forecast'] = []
        self.accuracy: Optional[float] = None
        self.is_active = True
        self.training_data_size = 0
    
    def generate_forecast(self, forecast: 'Forecast') -> None:
        """Сгенерировать прогноз"""
        if forecast not in self.__generated_forecasts:
            self.__generated_forecasts.append(forecast)
    
    def get_forecasts(self) -> List['Forecast']:
        """Получить прогнозы"""
        return self.__generated_forecasts.copy()
    
    def set_accuracy(self, accuracy: float) -> None:
        """Установить точность"""
        if not isinstance(accuracy, (int, float)) or accuracy < 0 or accuracy > 100:
            raise ModelException("Точность должна быть от 0 до 100")
        self.accuracy = accuracy
    
    def uses_data(self, weather_data: 'WeatherData') -> None:
        """Использует данные (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        weather_data.validate_data()
        self.training_data_size += 1
    
    def generates_forecast(self, forecast: 'Forecast') -> None:
        """Генерирует прогноз (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        self.generate_forecast(forecast)
    
    def used_by_meteorologist(self, meteorologist: 'Meteorologist') -> None:
        """Используется метеорологом (ассоциация с Meteorologist)"""
        if meteorologist is None:
            raise ValueError("Метеоролог не может быть None")
        if not meteorologist.is_available:
            raise ValueError("Метеоролог недоступен")
    
    forecasts = property(get_forecasts)


