"""Исключения для системы прогноза погоды"""
from .weather_exceptions import (
    WeatherException,
    InvalidSensorDataException,
    ForecastNotFoundException,
    InvalidForecastDataException,
    SensorMalfunctionException,
    DataValidationException,
    WeatherStationException,
    AlertException,
    ModelException,
    SatelliteException,
    RadarException,
    ClimateDataException
)

__all__ = [
    'WeatherException',
    'InvalidSensorDataException',
    'ForecastNotFoundException',
    'InvalidForecastDataException',
    'SensorMalfunctionException',
    'DataValidationException',
    'WeatherStationException',
    'AlertException',
    'ModelException',
    'SatelliteException',
    'RadarException',
    'ClimateDataException'
]


