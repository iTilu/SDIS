СИСТЕМА ПРОГНОЗА ПОГОДЫ

ОПИСАНИЕ КЛАССОВ, ПОЛЕЙ, МЕТОДОВ, АССОЦИАЦИЙ И ИСКЛЮЧЕНИЙ

СЕНСОРЫ (SENSORS):
TemperatureSensor 8 7 → WeatherStation, Measurement
HumiditySensor 8 6 → WeatherStation, Measurement
PressureSensor 8 6 → WeatherStation, Measurement
WindSensor 8 7 → WeatherStation, Measurement
RainSensor 8 6 → WeatherStation, Measurement
UVSensor 8 6 → WeatherStation, Measurement
VisibilitySensor 7 5 → WeatherStation, Measurement
AirQualitySensor 8 7 → WeatherStation, Measurement

ДАННЫЕ (DATA):
WeatherData 9 6 → WeatherStation, Forecast, TemperatureSensor, HumiditySensor
Measurement 7 6 → TemperatureSensor, HumiditySensor, PressureSensor, WeatherData
HistoricalData 7 5 → WeatherData, Location
ClimateData 7 6 → Location, HistoricalData
DataPoint 6 4 → WeatherData, HistoricalData
WeatherReport 7 5 → WeatherData, Forecast, Location

ПРОГНОЗЫ (FORECASTS):
Forecast 9 7 → Location, WeatherData, WeatherModel, Meteorologist
ShortTermForecast 7 5 → Forecast, Location, WeatherModel
LongTermForecast 8 6 → Forecast, Location, WeatherModel
HourlyForecast 7 4 → Forecast, Location
DailyForecast 8 5 → Forecast, HourlyForecast, Location

СТАНЦИИ (STATIONS):
WeatherStation 8 6 → Location, TemperatureSensor, HumiditySensor, PressureSensor, WeatherData, Technician
StationNetwork 6 5 → WeatherStation, Administrator
StationManager 7 5 → WeatherStation, StationNetwork, Administrator

ПЕРСОНАЛ (STAFF):
Meteorologist 8 5 → Forecast, WeatherModel, WeatherData, WeatherStation
Forecaster 7 5 → Forecast, ShortTermForecast, WeatherModel
DataAnalyst 7 5 → WeatherData, HistoricalData, WeatherAnalyzer
Technician 6 5 → WeatherStation, TemperatureSensor, Anemometer
Observer 7 5 → WeatherStation, WeatherData, Barometer
Administrator 6 4 → StationNetwork, StationManager, Meteorologist

МОДЕЛИ (MODELS):
WeatherModel 8 5 → Forecast, WeatherData, Meteorologist
NumericalModel 6 4 → WeatherModel, Forecast
StatisticalModel 7 4 → WeatherModel, HistoricalData
AIForecastModel 7 5 → WeatherModel, Forecast, WeatherData

ОПОВЕЩЕНИЯ (ALERTS):
WeatherAlert 7 4 → Location, Forecast
StormAlert 6 4 → WeatherAlert, Location
TemperatureAlert 7 4 → WeatherAlert, Location
WindAlert 7 4 → WeatherAlert, Location

ОБОРУДОВАНИЕ (EQUIPMENT):
Satellite 7 5 → Location, WeatherData, WeatherStation
Radar 7 5 → Location, WeatherData, WeatherStation
Anemometer 6 3 → WindSensor, WeatherStation
Barometer 6 3 → PressureSensor, WeatherStation
Thermometer 6 3 → TemperatureSensor, WeatherStation
Hygrometer 6 3 → HumiditySensor, WeatherStation

ЛОКАЦИИ (LOCATIONS):
Location 6 5 → Coordinates, WeatherStation, Forecast, WeatherData
City 6 4 → Location, Coordinates, Forecast
Region 7 4 → Location, City, ClimateData
Coordinates 3 2 → Location, City

АНАЛИЗ (ANALYSIS):
WeatherAnalyzer 6 5 → WeatherData, HistoricalData, DataAnalyst
TrendAnalyzer 5 4 → HistoricalData, WeatherAnalyzer
PatternRecognizer 6 3 → HistoricalData, WeatherAnalyzer
DataProcessor 6 4 → WeatherData, Measurement, WeatherAnalyzer

ИСКЛЮЧЕНИЯ (EXCEPTIONS):
WeatherException 1 1 →
InvalidSensorDataException 0 0 →
ForecastNotFoundException 0 0 →
InvalidForecastDataException 0 0 →
SensorMalfunctionException 0 0 →
DataValidationException 0 0 →
WeatherStationException 0 0 →
AlertException 0 0 →
ModelException 0 0 →
SatelliteException 0 0 →
RadarException 0 0 →
ClimateDataException 0 0 →

ИТОГО:
Классы: 50
Поля: 195
Методы: 120
Ассоциации: 67
Исключения: 12

ИСКЛЮЧЕНИЯ:
WeatherException - базовое исключение
InvalidSensorDataException - невалидные данные сенсора
ForecastNotFoundException - прогноз не найден
InvalidForecastDataException - невалидные данные прогноза
SensorMalfunctionException - неисправность сенсора
DataValidationException - ошибка валидации данных
WeatherStationException - исключение метеостанции
AlertException - исключение оповещений
ModelException - исключение моделей
SatelliteException - исключение спутников
RadarException - исключение радаров
ClimateDataException - исключение климатических данных


