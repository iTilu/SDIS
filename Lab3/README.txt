AIForecastModel 7 5 -> WeatherModel, Forecast, WeatherData
Administrator 6 4 -> StationNetwork, StationManager, Meteorologist
AirQualitySensor 8 7 -> WeatherStation, Measurement
AlertException 0 0
Anemometer 6 3 -> WindSensor, WeatherStation
Barometer 6 3 -> PressureSensor, WeatherStation
City 6 4 -> Location, Coordinates, Forecast
ClimateData 7 6 -> Location, HistoricalData
ClimateDataException 0 0
Coordinates 3 2 -> Location, City
DailyForecast 8 5 -> Forecast, HourlyForecast, Location
DataAnalyst 7 5 -> WeatherData, HistoricalData, WeatherAnalyzer
DataPoint 6 4 -> WeatherData, HistoricalData
DataProcessor 6 4 -> WeatherData, Measurement, WeatherAnalyzer
Forecast 9 7 -> Location, WeatherData, WeatherModel, Meteorologist
ForecastNotFoundException 0 0
Forecaster 7 5 -> Forecast, ShortTermForecast, WeatherModel
HistoricalData 7 5 -> WeatherData, Location
HourlyForecast 7 4 -> Forecast, Location
HumiditySensor 8 6 -> WeatherStation, Measurement
Hygrometer 6 3 -> HumiditySensor, WeatherStation
InvalidForecastDataException 0 0
InvalidSensorDataException 0 0
Location 7 7 -> Coordinates, WeatherStation, Forecast, WeatherData
LongTermForecast 8 6 -> Forecast, Location, WeatherModel
Measurement 7 8 -> TemperatureSensor, HumiditySensor, PressureSensor, WeatherData
Meteorologist 8 5 -> Forecast, WeatherModel, WeatherData, WeatherStation
ModelException 0 0
NumericalModel 6 4 -> WeatherModel, Forecast
Observer 7 5 -> WeatherStation, WeatherData, Barometer
PatternRecognizer 6 3 -> HistoricalData, WeatherAnalyzer
PressureSensor 8 6 -> WeatherStation, Measurement
Radar 7 5 -> Location, WeatherData, WeatherStation
RadarException 0 0
RainSensor 8 6 -> WeatherStation, Measurement
Region 7 4 -> Location, City, ClimateData
Satellite 7 5 -> Location, WeatherData, WeatherStation
SatelliteException 0 0
SensorMalfunctionException 0 0
ShortTermForecast 7 5 -> Forecast, Location, WeatherModel
StatisticalModel 7 4 -> WeatherModel, HistoricalData
StationManager 7 5 -> WeatherStation, StationNetwork, Administrator
StationNetwork 6 5 -> WeatherStation, Administrator
StormAlert 6 4 -> WeatherAlert, Location
Technician 6 5 -> WeatherStation, TemperatureSensor, Anemometer
TemperatureAlert 7 4 -> WeatherAlert, Location
TemperatureSensor 8 7 -> WeatherStation, Measurement
Thermometer 6 3 -> TemperatureSensor, WeatherStation
TrendAnalyzer 5 4 -> HistoricalData, WeatherAnalyzer
UVSensor 8 6 -> WeatherStation, Measurement
VisibilitySensor 7 5 -> WeatherStation, Measurement
WeatherAlert 7 4 -> Location, Forecast
WeatherAnalyzer 6 5 -> WeatherData, HistoricalData, DataAnalyst
WeatherData 9 6 -> WeatherStation, Forecast, TemperatureSensor, HumiditySensor
WeatherException 1 1
WeatherModel 8 5 -> Forecast, WeatherData, Meteorologist
WeatherReport 7 5 -> WeatherData, Forecast, Location
WeatherStation 10 9 -> Location, TemperatureSensor, HumiditySensor, PressureSensor, WeatherData, Technician
WindAlert 7 4 -> WeatherAlert, Location
WindSensor 8 7 -> WeatherStation, Measurement


