"""Тесты для класса Expense"""
import pytest
from datetime import datetime
from finance.expense import Expense


def test_expense_creation_valid():
    """Тест создания расхода с валидными данными"""
    test_date = datetime(2024, 1, 15, 10, 30)
    expense = Expense("Закупка костюмов", 50000.0, test_date)

    assert expense.description == "Закупка костюмов"
    assert expense.amount == 50000.0
    assert expense.expense_date == test_date
    assert expense.category == ""
    assert expense.is_approved == False
    assert expense.approved_by is None


def test_expense_creation_invalid_description():
    """Тест создания расхода с невалидным описанием"""
    test_date = datetime.now()

    with pytest.raises(ValueError, match="Описание должно быть непустой строкой"):
        Expense("", 50000.0, test_date)

    with pytest.raises(ValueError, match="Описание должно быть непустой строкой"):
        Expense(None, 50000.0, test_date)

    with pytest.raises(ValueError, match="Описание должно быть непустой строкой"):
        Expense(123, 50000.0, test_date)


def test_expense_creation_invalid_amount():
    """Тест создания расхода с невалидной суммой"""
    test_date = datetime.now()

    with pytest.raises(ValueError, match="Сумма должна быть неотрицательным числом"):
        Expense("Тест", -100.0, test_date)

    with pytest.raises(ValueError, match="Сумма должна быть неотрицательным числом"):
        Expense("Тест", "50000", test_date)

    # Проверяем, что сумма конвертируется в float
    expense = Expense("Тест", 50000, test_date)  # int должен конвертироваться в float
    assert expense.amount == 50000.0
    assert isinstance(expense.amount, float)


def test_expense_creation_zero_amount():
    """Тест создания расхода с нулевой суммой"""
    test_date = datetime.now()
    expense = Expense("Тест", 0.0, test_date)
    assert expense.amount == 0.0


def test_expense_creation_invalid_date():
    """Тест создания расхода с невалидной датой"""
    with pytest.raises(ValueError, match="Дата должна быть объектом datetime"):
        Expense("Тест", 50000.0, "2024-01-15")

    with pytest.raises(ValueError, match="Дата должна быть объектом datetime"):
        Expense("Тест", 50000.0, None)

    with pytest.raises(ValueError, match="Дата должна быть объектом datetime"):
        Expense("Тест", 50000.0, 1234567890)


def test_set_category_valid():
    """Тест установки валидной категории"""
    expense = Expense("Тест", 1000.0, datetime.now())
    expense.set_category("Костюмы")
    assert expense.category == "Костюмы"


def test_set_category_invalid():
    """Тест установки невалидной категории"""
    expense = Expense("Тест", 1000.0, datetime.now())

    with pytest.raises(TypeError, match="Категория должна быть строкой"):
        expense.set_category(123)

    with pytest.raises(TypeError, match="Категория должна быть строкой"):
        expense.set_category([])

    with pytest.raises(TypeError, match="Категория должна быть строкой"):
        expense.set_category(None)


def test_approve_expense():
    """Тест одобрения расхода"""
    expense = Expense("Тест", 1000.0, datetime.now())
    assert not expense.is_approved
    assert expense.approved_by is None

    expense.approve("Иванов И.И.")
    assert expense.is_approved == True
    assert expense.approved_by == "Иванов И.И."


def test_approve_expense_invalid_approver():
    """Тест одобрения расхода с невалидным одобряющим"""
    expense = Expense("Тест", 1000.0, datetime.now())

    with pytest.raises(TypeError, match="Имя одобряющего должно быть строкой"):
        expense.approve(123)

    with pytest.raises(TypeError, match="Имя одобряющего должно быть строкой"):
        expense.approve(None)


def test_approve_expense_twice():
    """Тест повторного одобрения расхода"""
    expense = Expense("Тест", 1000.0, datetime.now())

    expense.approve("Иванов И.И.")
    assert expense.is_approved == True
    assert expense.approved_by == "Иванов И.И."

    # Повторное одобрение должно перезаписать
    expense.approve("Петров П.П.")
    assert expense.is_approved == True
    assert expense.approved_by == "Петров П.П."


def test_is_valid_not_approved():
    """Тест валидности неодобренного расхода"""
    expense = Expense("Тест", 1000.0, datetime.now())
    assert not expense.is_valid()


def test_is_valid_zero_amount():
    """Тест валидности расхода с нулевой суммой"""
    expense = Expense("Тест", 0.0, datetime.now())
    expense.approve("Иванов И.И.")
    assert not expense.is_valid()  # Нулевая сумма не валидна даже при одобрении


def test_is_valid_negative_amount():
    """Тест валидности расхода с отрицательной суммой"""
    # Хотя создание с отрицательной суммой невозможно, проверим на всякий случай
    expense = Expense("Тест", 1000.0, datetime.now())
    expense.amount = -100.0  # Принудительно установим отрицательную сумму
    expense.approve("Иванов И.И.")
    assert not expense.is_valid()  # Отрицательная сумма не валидна


def test_is_valid_approved_positive():
    """Тест валидности одобренного расхода с положительной суммой"""
    expense = Expense("Тест", 1000.0, datetime.now())
    expense.approve("Иванов И.И.")
    assert expense.is_valid()


def test_expense_field_types():
    """Тест типов полей расхода"""
    test_date = datetime.now()
    expense = Expense("Тест", 1000.0, test_date)

    assert isinstance(expense.description, str)
    assert isinstance(expense.amount, float)
    assert isinstance(expense.expense_date, datetime)
    assert isinstance(expense.category, str)
    assert isinstance(expense.is_approved, bool)
    assert expense.approved_by is None or isinstance(expense.approved_by, str)


def test_expense_data_integrity():
    """Тест целостности данных расхода"""
    test_date = datetime(2024, 1, 15, 10, 30, 45)
    expense = Expense("Тестовый расход", 12345.67, test_date)

    # Проверяем, что данные не изменились
    assert expense.description == "Тестовый расход"
    assert expense.amount == 12345.67
    assert expense.expense_date == test_date

    # Изменяем категорию и проверяем одобрение
    expense.set_category("Тестовая категория")
    expense.approve("Тестовый одобряющий")

    assert expense.category == "Тестовая категория"
    assert expense.is_approved == True
    assert expense.approved_by == "Тестовый одобряющий"

