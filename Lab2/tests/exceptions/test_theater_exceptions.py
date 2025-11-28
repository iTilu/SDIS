"""Тесты для исключений"""
import pytest
from exceptions.theater_exceptions import (
    TheaterException,
    InsufficientFundsException,
    InvalidActorDataException,
    PerformanceNotFoundException,
    InvalidPerformanceDataException,
    InvalidTicketDataException,
    TicketSoldOutException,
    VenueOverloadException,
    ActorNotAvailableException,
    DirectorNotAvailableException,
    InvalidLicenseException,
    InvalidScheduleException
)


def test_theater_exception():
    """Тест базового исключения"""
    exc = TheaterException("Тестовая ошибка")
    assert str(exc) == "Тестовая ошибка"


def test_insufficient_funds_exception():
    """Тест исключения недостатка средств"""
    exc = InsufficientFundsException()
    assert isinstance(exc, TheaterException)


def test_invalid_actor_data_exception():
    """Тест исключения невалидных данных актера"""
    exc = InvalidActorDataException()
    assert isinstance(exc, TheaterException)

