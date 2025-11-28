"""Тесты для класса PropsMaster"""
import pytest
from staff.props_master import PropsMaster


def test_props_master_creation():
    """Тест создания реквизитора"""
    props_master = PropsMaster("Петр Реквизитов", 28, 3, 45000.0)
    assert props_master.name == "Петр Реквизитов"
    assert props_master.age == 28
    assert props_master.experience_years == 3
    assert props_master.salary == 45000.0
    assert props_master.is_available is True
    assert props_master.props_count == 0


def test_props_master_invalid_name():
    """Тест с невалидным именем"""
    with pytest.raises(ValueError):
        PropsMaster("", 28, 3, 45000.0)


def test_props_master_add_prop():
    """Тест добавления реквизита"""
    props_master = PropsMaster("Петр Реквизитов", 28, 3, 45000.0)
    props_master.add_prop("Меч")
    assert "Меч" in props_master.props


def test_props_master_remove_prop():
    """Тест удаления реквизита"""
    props_master = PropsMaster("Петр Реквизитов", 28, 3, 45000.0)
    props_master.add_prop("Меч")
    props_master.remove_prop("Меч")
    assert "Меч" not in props_master.props


def test_props_master_set_props_count():
    """Тест установки количества реквизита"""
    props_master = PropsMaster("Петр Реквизитов", 28, 3, 45000.0)
    props_master.set_props_count(10)
    assert props_master.props_count == 10


def test_props_master_set_availability():
    """Тест установки доступности"""
    props_master = PropsMaster("Петр Реквизитов", 28, 3, 45000.0)
    props_master.set_availability(False)
    assert props_master.is_available is False


