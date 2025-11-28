"""Тесты для класса Prop"""
import pytest
from props.prop import Prop


def test_prop_creation():
    """Тест создания реквизита"""
    prop = Prop("Меч", "Оружие", 2.5)
    assert prop.name == "Меч"
    assert prop.prop_type == "Оружие"
    assert prop.weight == 2.5

