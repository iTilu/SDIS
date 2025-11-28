"""Тесты для класса Review"""
import pytest
from performances.review import Review


def test_review_creation():
    """Тест создания отзыва"""
    review = Review("Гамлет", "Иван Иванов", 8.5, "Отличный спектакль")
    assert review.performance_name == "Гамлет"
    assert review.rating == 8.5

