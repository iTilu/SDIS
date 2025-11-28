"""Исключения для системы прогноза погоды"""


class WeatherException(Exception):
    """Базовое исключение для системы прогноза погоды"""
    
    def __init__(self, message: str):
        if not isinstance(message, str):
            raise TypeError("Сообщение должно быть строкой")
        self.message = message
        super().__init__(self.message)


class InvalidSensorDataException(WeatherException):
    """Исключение при невалидных данных сенсора"""
    pass


class ForecastNotFoundException(WeatherException):
    """Исключение при отсутствии прогноза"""
    pass


class InvalidForecastDataException(WeatherException):
    """Исключение при невалидных данных прогноза"""
    pass


class SensorMalfunctionException(WeatherException):
    """Исключение при неисправности сенсора"""
    pass


class DataValidationException(WeatherException):
    """Исключение при ошибке валидации данных"""
    pass


class WeatherStationException(WeatherException):
    """Исключение для метеостанции"""
    pass


class AlertException(WeatherException):
    """Исключение для системы оповещений"""
    pass


class ModelException(WeatherException):
    """Исключение для моделей прогноза"""
    pass


class SatelliteException(WeatherException):
    """Исключение для спутников"""
    pass


class RadarException(WeatherException):
    """Исключение для радаров"""
    pass


class ClimateDataException(WeatherException):
    """Исключение для климатических данных"""
    pass


