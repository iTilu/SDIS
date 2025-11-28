"""Класс данных о погоде"""
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from exceptions.weather_exceptions import DataValidationException

if TYPE_CHECKING:
    from stations.weather_station import WeatherStation
    from forecasts.forecast import Forecast
    from sensors.temperature_sensor import TemperatureSensor
    from sensors.humidity_sensor import HumiditySensor


class WeatherData:
    """Данные о погоде"""
    
    def __init__(self, data_id: str, timestamp: datetime, temperature: float, humidity: float):
        if not isinstance(data_id, str) or not data_id:
            raise ValueError("ID данных должен быть непустой строкой")
        if not isinstance(timestamp, datetime):
            raise TypeError("Временная метка должна быть datetime")
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")
        if not isinstance(humidity, (int, float)) or humidity < 0 or humidity > 100:
            raise ValueError("Влажность должна быть от 0 до 100")
        
        self.data_id = data_id
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        self.pressure: Optional[float] = None
        self.wind_speed: Optional[float] = None
        self.wind_direction: Optional[int] = None
        self.rainfall: Optional[float] = None
        self.visibility: Optional[float] = None
        self.data_quality = "good"
    
    def add_pressure(self, pressure: float) -> None:
        """Добавить давление"""
        if not isinstance(pressure, (int, float)) or pressure < 0:
            raise ValueError("Давление должно быть положительным")
        self.pressure = pressure
    
    def add_wind_data(self, speed: float, direction: int) -> None:
        """Добавить данные ветра"""
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError("Скорость ветра должна быть неотрицательной")
        if not isinstance(direction, int) or direction < 0 or direction > 360:
            raise ValueError("Направление должно быть от 0 до 360")
        self.wind_speed = speed
        self.wind_direction = direction
    
    def validate_data(self) -> bool:
        """Валидировать данные"""
        if self.temperature < -100 or self.temperature > 100:
            raise DataValidationException("Температура вне допустимого диапазона")
        if self.humidity < 0 or self.humidity > 100:
            raise DataValidationException("Влажность вне допустимого диапазона")
        return True
    
    def get_from_station(self, station: 'WeatherStation') -> None:
        """Получить данные со станции (ассоциация с WeatherStation)"""
        if station is None:
            raise ValueError("Метеостанция не может быть None")
        if not station.is_operational:
            raise ValueError("Станция не работает")
        # Данные получаются со станции
        self.data_quality = "good"
    
    def used_in_forecast(self, forecast: 'Forecast') -> None:
        """Использовано в прогнозе (ассоциация с Forecast)"""
        if forecast is None:
            raise ValueError("Прогноз не может быть None")
        # Данные используются для создания прогноза
        if self.temperature is not None:
            forecast.temperature = self.temperature
        if self.humidity is not None:
            forecast.add_humidity(self.humidity)
    
    def get_data_summary(self) -> str:
        """Получить сводку данных"""
        return f"Temp: {self.temperature}°C, Humidity: {self.humidity}%"


