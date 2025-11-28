"""Тесты для класса Costume"""
import pytest
from costumes.costume import Costume


def test_costume_creation():
    """Тест создания костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    assert costume.name == "Королевский наряд"
    assert costume.size == "M"
    assert costume.material == "Шелк"


def test_costume_assign_to_actor():
    """Тест назначения актеру"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.assign_to_actor("Иван Иванов")
    assert costume.actor_name == "Иван Иванов"
    assert costume.is_available is False

