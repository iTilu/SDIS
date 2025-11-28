"""Тесты для класса SecurityGuard"""
import pytest
from staff.security_guard import SecurityGuard


def test_security_guard_creation():
    """Тест создания охранника"""
    guard = SecurityGuard("Иван Сидоров", 35, 5, 40000.0)
    assert guard.name == "Иван Сидоров"
    assert guard.age == 35
    assert guard.experience_years == 5
    assert guard.salary == 40000.0
    assert guard.is_available is True
    assert guard.license_number == ""


def test_security_guard_invalid_name():
    """Тест с невалидным именем"""
    with pytest.raises(ValueError):
        SecurityGuard("", 35, 5, 40000.0)


def test_security_guard_add_area():
    """Тест добавления зоны"""
    guard = SecurityGuard("Иван Сидоров", 35, 5, 40000.0)
    guard.add_area("Главный вход")
    assert "Главный вход" in guard.areas


def test_security_guard_set_license():
    """Тест установки лицензии"""
    guard = SecurityGuard("Иван Сидоров", 35, 5, 40000.0)
    guard.set_license_number("LIC123")
    assert guard.license_number == "LIC123"


def test_security_guard_set_shift():
    """Тест установки смены"""
    guard = SecurityGuard("Иван Сидоров", 35, 5, 40000.0)
    guard.set_shift("Дневная")
    assert guard.shift == "Дневная"


def test_security_guard_set_availability():
    """Тест установки доступности"""
    guard = SecurityGuard("Иван Сидоров", 35, 5, 40000.0)
    guard.set_availability(False)
    assert guard.is_available is False

