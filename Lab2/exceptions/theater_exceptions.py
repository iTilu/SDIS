"""Театральные исключения"""


class TheaterException(Exception):
    """Базовое исключение для театра"""
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsException(TheaterException):
    """Недостаточно средств"""
    
    def __init__(self, message: str = "Недостаточно средств"):
        super().__init__(message)


class InvalidActorDataException(TheaterException):
    """Некорректные данные актера"""
    
    def __init__(self, message: str = "Некорректные данные актера"):
        super().__init__(message)


class PerformanceNotFoundException(TheaterException):
    """Спектакль не найден"""
    
    def __init__(self, message: str = "Спектакль не найден"):
        super().__init__(message)


class InvalidPerformanceDataException(TheaterException):
    """Некорректные данные спектакля"""
    
    def __init__(self, message: str = "Некорректные данные спектакля"):
        super().__init__(message)


class InvalidTicketDataException(TheaterException):
    """Некорректные данные билета"""
    
    def __init__(self, message: str = "Некорректные данные билета"):
        super().__init__(message)


class TicketSoldOutException(TheaterException):
    """Билеты распроданы"""
    
    def __init__(self, message: str = "Билеты распроданы"):
        super().__init__(message)


class VenueOverloadException(TheaterException):
    """Перегрузка зала"""
    
    def __init__(self, message: str = "Перегрузка зала"):
        super().__init__(message)


class ActorNotAvailableException(TheaterException):
    """Актер недоступен"""
    
    def __init__(self, message: str = "Актер недоступен"):
        super().__init__(message)


class DirectorNotAvailableException(TheaterException):
    """Режиссер недоступен"""
    
    def __init__(self, message: str = "Режиссер недоступен"):
        super().__init__(message)


class InvalidLicenseException(TheaterException):
    """Некорректная лицензия"""
    
    def __init__(self, message: str = "Некорректная лицензия"):
        super().__init__(message)


class InvalidScheduleException(TheaterException):
    """Некорректное расписание"""
    
    def __init__(self, message: str = "Некорректное расписание"):
        super().__init__(message)

