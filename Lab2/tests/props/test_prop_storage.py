"""Тесты для класса PropStorage"""
import pytest
from props.prop_storage import PropStorage


def test_prop_storage_creation():
    """Тест создания хранилища"""
    storage = PropStorage("Склад 1", 100)
    assert storage.name == "Склад 1"
    assert storage.capacity == 100

