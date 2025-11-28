"""Класс прогноза погоды"""
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime, date
from exceptions.weather_exceptions import ForecastNotFoundException, InvalidForecastDataException

if TYPE_CHECKING:
    from locations.location import Location
    from data.weather_data import WeatherData
    from models.weather_model import WeatherModel
    from staff.meteorologist import Meteorologist


class Forecast:
    """Прогноз погоды"""
    
    def __init__(self, forecast_id: str, location_name: str, forecast_date: date, temperature: float):
        if not isinstance(forecast_id, str) or not forecast_id:
            raise ValueError("ID прогноза должен быть непустой строкой")
        if not isinstance(location_name, str) or not location_name:
            raise ValueError("Название локации должно быть непустой строкой")
        if not isinstance(forecast_date, date):
            raise TypeError("Дата прогноза должна быть date")
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")
        
        self.forecast_id = forecast_id
        self.location_name = location_name
        self.forecast_date = forecast_date
        self.temperature = temperature
        self.humidity: Optional[float] = None
        self.precipitation_probability: Optional[float] = None
        self.wind_speed: Optional[float] = None
        self.forecast_type = "general"
        self.accuracy_score: Optional[float] = None
        self.created_at = datetime.now()
    
    def add_humidity(self, humidity: float) -> None:
        """Добавить влажность"""
        if not isinstance(humidity, (int, float)) or humidity < 0 or humidity > 100:
            raise ValueError("Влажность должна быть от 0 до 100")
        self.humidity = humidity
    
    def set_precipitation_probability(self, probability: float) -> None:
        """Установить вероятность осадков"""
        if not isinstance(probability, (int, float)) or probability < 0 or probability > 100:
            raise InvalidForecastDataException("Вероятность должна быть от 0 до 100")
        self.precipitation_probability = probability
    
    def add_wind_forecast(self, wind_speed: float) -> None:
        """Добавить прогноз ветра"""
        if not isinstance(wind_speed, (int, float)) or wind_speed < 0:
            raise ValueError("Скорость ветра должна быть неотрицательной")
        self.wind_speed = wind_speed
    
    def set_accuracy(self, score: float) -> None:
        """Установить точность"""
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            raise InvalidForecastDataException("Оценка точности должна быть от 0 до 100")
        self.accuracy_score = score
    
    def for_location(self, location: 'Location') -> None:
        """Для локации (ассоциация с Location)"""
        if location is None:
            raise ValueError("Локация не может быть None")
        if self.location_name != location.name:
            self.location_name = location.name
    
    def based_on_data(self, weather_data: 'WeatherData') -> None:
        """На основе данных (ассоциация с WeatherData)"""
        if weather_data is None:
            raise ValueError("Данные о погоде не могут быть None")
        if weather_data.temperature is not None:
            self.temperature = weather_data.temperature
        if weather_data.humidity is not None:
            self.add_humidity(weather_data.humidity)
    
    def generated_by_model(self, model: 'WeatherModel') -> None:
        """Сгенерирован моделью (ассоциация с WeatherModel)"""
        if model is None:
            raise ValueError("Модель не может быть None")
        if not model.is_active:
            raise ValueError("Модель неактивна")
        model.generate_forecast(self)
        if model.accuracy is not None:
            self.set_accuracy(model.accuracy)
    
    def created_by_meteorologist(self, meteorologist: 'Meteorologist') -> None:
        """Создан метеорологом (ассоциация с Meteorologist)"""
        if meteorologist is None:
            raise ValueError("Метеоролог не может быть None")
        if not meteorologist.is_available:
            raise ValueError("Метеоролог недоступен")
        meteorologist.create_forecast(self)
    
    def get_forecast_summary(self) -> str:
        """Получить сводку прогноза"""
        return f"{self.location_name}: {self.temperature}°C on {self.forecast_date}"


