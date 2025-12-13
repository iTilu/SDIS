"""Тесты для класса Budget"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from finance.budget import Budget


def test_budget_creation_valid():
    """Тест создания бюджета с валидными данными"""
    budget = Budget(2024, 1000000.0)
    assert budget.year == 2024
    assert budget.total_amount == 1000000.0
    assert budget.allocated_amount == 0.0
    assert budget.remaining_amount == 1000000.0
    assert budget.get_total_expenses() == 0.0
    assert budget.get_total_revenues() == 0.0
    assert budget.get_balance() == 1000000.0


def test_budget_creation_invalid_year():
    """Тест создания бюджета с невалидным годом"""
    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        Budget(-1, 1000000.0)

    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        Budget("2024", 1000000.0)

    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        Budget(2024.5, 1000000.0)


def test_budget_creation_invalid_amount():
    """Тест создания бюджета с невалидной суммой"""
    with pytest.raises(ValueError, match="Общая сумма должна быть неотрицательным числом"):
        Budget(2024, -1000000.0)

    with pytest.raises(ValueError, match="Общая сумма должна быть неотрицательным числом"):
        Budget(2024, "1000000")

    # Проверяем конвертацию int в float
    budget = Budget(2024, 1000000)  # int
    assert budget.total_amount == 1000000.0
    assert isinstance(budget.total_amount, float)


def test_budget_creation_zero_amount():
    """Тест создания бюджета с нулевой суммой"""
    budget = Budget(2024, 0.0)
    assert budget.total_amount == 0.0
    assert budget.remaining_amount == 0.0
    assert budget.get_balance() == 0.0


def test_budget_add_expense_valid():
    """Тест добавления валидного расхода"""
    budget = Budget(2024, 1000000.0)
    budget.add_expense(50000.0)

    assert budget.get_total_expenses() == 50000.0
    assert budget.remaining_amount == 950000.0
    assert budget.get_balance() == 950000.0


def test_budget_add_expense_invalid_amount():
    """Тест добавления расхода с невалидной суммой"""
    budget = Budget(2024, 1000000.0)

    with pytest.raises(ValueError, match="Сумма должна быть неотрицательным числом"):
        budget.add_expense(-10000.0)

    with pytest.raises(ValueError, match="Сумма должна быть неотрицательным числом"):
        budget.add_expense("50000")


def test_budget_add_expense_insufficient_funds():
    """Тест добавления расхода при недостатке средств"""
    budget = Budget(2024, 50000.0)

    # Добавляем первый расход
    budget.add_expense(30000.0)
    assert budget.remaining_amount == 20000.0

    # Пытаемся добавить слишком большой расход
    with pytest.raises(ValueError, match="Недостаточно средств в бюджете"):
        budget.add_expense(30000.0)  # Больше оставшихся средств


def test_budget_add_expense_zero():
    """Тест добавления нулевого расхода"""
    budget = Budget(2024, 1000000.0)
    budget.add_expense(0.0)

    assert budget.get_total_expenses() == 0.0
    assert budget.remaining_amount == 1000000.0


def test_budget_add_revenue_valid():
    """Тест добавления валидного дохода"""
    budget = Budget(2024, 1000000.0)
    budget.add_revenue(50000.0)

    assert budget.get_total_revenues() == 50000.0
    assert budget.remaining_amount == 1050000.0
    assert budget.get_balance() == 1050000.0


def test_budget_add_revenue_invalid_amount():
    """Тест добавления дохода с невалидной суммой"""
    budget = Budget(2024, 1000000.0)

    with pytest.raises(ValueError, match="Сумма должна быть неотрицательным числом"):
        budget.add_revenue(-10000.0)

    with pytest.raises(ValueError, match="Сумма должна быть неотрицательным числом"):
        budget.add_revenue("50000")


def test_budget_add_revenue_zero():
    """Тест добавления нулевого дохода"""
    budget = Budget(2024, 1000000.0)
    budget.add_revenue(0.0)

    assert budget.get_total_revenues() == 0.0
    assert budget.remaining_amount == 1000000.0


def test_budget_get_total_expenses():
    """Тест получения общих расходов"""
    budget = Budget(2024, 1000000.0)

    # Без расходов
    assert budget.get_total_expenses() == 0.0

    # С расходами
    budget.add_expense(10000.0)
    budget.add_expense(20000.0)
    budget.add_expense(30000.0)

    assert budget.get_total_expenses() == 60000.0


def test_budget_get_total_revenues():
    """Тест получения общих доходов"""
    budget = Budget(2024, 1000000.0)

    # Без доходов
    assert budget.get_total_revenues() == 0.0

    # С доходами
    budget.add_revenue(15000.0)
    budget.add_revenue(25000.0)

    assert budget.get_total_revenues() == 40000.0


def test_budget_allocate_valid():
    """Тест выделения валидных средств"""
    budget = Budget(2024, 1000000.0)
    budget.allocate(200000.0)

    assert budget.allocated_amount == 200000.0
    assert budget.remaining_amount == 800000.0


def test_budget_allocate_invalid_amount():
    """Тест выделения средств с невалидной суммой"""
    budget = Budget(2024, 1000000.0)

    with pytest.raises(ValueError, match="Сумма должна быть неотрицательным числом"):
        budget.allocate(-50000.0)

    with pytest.raises(ValueError, match="Сумма должна быть неотрицательным числом"):
        budget.allocate("200000")


def test_budget_allocate_insufficient_funds():
    """Тест выделения средств при недостатке"""
    budget = Budget(2024, 100000.0)
    budget.allocate(80000.0)  # Выделяем почти все

    # Пытаемся выделить больше оставшихся средств
    with pytest.raises(ValueError, match="Недостаточно средств"):
        budget.allocate(30000.0)  # Больше оставшихся


def test_budget_allocate_zero():
    """Тест выделения нулевых средств"""
    budget = Budget(2024, 1000000.0)
    budget.allocate(0.0)

    assert budget.allocated_amount == 0.0
    assert budget.remaining_amount == 1000000.0


def test_budget_get_balance():
    """Тест получения баланса"""
    budget = Budget(2024, 1000000.0)

    # Начальный баланс
    assert budget.get_balance() == 1000000.0

    # Добавляем расходы
    budget.add_expense(100000.0)
    assert budget.get_balance() == 900000.0

    # Добавляем доходы
    budget.add_revenue(50000.0)
    assert budget.get_balance() == 950000.0

    # Еще расходы и доходы
    budget.add_expense(200000.0)
    budget.add_revenue(150000.0)
    assert budget.get_balance() == 900000.0  # 1000000 - 300000 + 200000


def test_budget_complex_operations():
    """Тест комплексных операций с бюджетом"""
    budget = Budget(2024, 1000000.0)

    # Начальное состояние
    assert budget.remaining_amount == 1000000.0
    assert budget.allocated_amount == 0.0
    assert budget.get_total_expenses() == 0.0
    assert budget.get_total_revenues() == 0.0

    # Выделяем средства
    budget.allocate(200000.0)
    assert budget.allocated_amount == 200000.0
    assert budget.remaining_amount == 800000.0

    # Добавляем расходы
    budget.add_expense(150000.0)  # В рамках выделенных средств
    assert budget.get_total_expenses() == 150000.0
    assert budget.remaining_amount == 650000.0

    # Добавляем доходы
    budget.add_revenue(50000.0)
    assert budget.get_total_revenues() == 50000.0
    assert budget.remaining_amount == 700000.0

    # Финальный баланс
    assert budget.get_balance() == 900000.0  # 1000000 - 150000 + 50000


def test_budget_field_types():
    """Тест типов полей бюджета"""
    budget = Budget(2024, 1000000.0)
    budget.add_expense(50000.0)
    budget.add_revenue(25000.0)
    budget.allocate(100000.0)

    assert isinstance(budget.year, int)
    assert isinstance(budget.total_amount, float)
    assert isinstance(budget.allocated_amount, float)
    assert isinstance(budget.remaining_amount, float)
    assert isinstance(budget.get_total_expenses(), float)
    assert isinstance(budget.get_total_revenues(), float)
    assert isinstance(budget.get_balance(), float)


def test_budget_data_integrity():
    """Тест целостности данных бюджета"""
    budget = Budget(2024, 1000000.0)

    # Изменяем бюджет через различные операции
    budget.allocate(100000.0)
    budget.add_expense(50000.0)
    budget.add_revenue(25000.0)

    # Проверяем, что основные поля остались неизменными
    assert budget.year == 2024
    assert budget.total_amount == 1000000.0

    # Проверяем корректность расчетов
    expected_remaining = 1000000.0 - 100000.0 - 50000.0 + 25000.0
    assert budget.remaining_amount == expected_remaining
    assert budget.allocated_amount == 100000.0
    assert budget.get_total_expenses() == 50000.0
    assert budget.get_total_revenues() == 25000.0
    assert budget.get_balance() == 975000.0


def test_budget_boundary_values():
    """Тест граничных значений для бюджета"""
    # Минимальный бюджет
    budget1 = Budget(0, 0.0)
    assert budget1.total_amount == 0.0
    assert budget1.remaining_amount == 0.0

    # Очень большой бюджет
    budget2 = Budget(2024, 1000000000.0)
    assert budget2.total_amount == 1000000000.0
    assert budget2.remaining_amount == 1000000000.0

    # Много операций
    budget3 = Budget(2024, 100000.0)
    for i in range(10):
        budget3.add_expense(5000.0)  # 50000 total
        budget3.add_revenue(3000.0)  # 30000 total

    assert budget3.get_total_expenses() == 50000.0
    assert budget3.get_total_revenues() == 30000.0
    assert budget3.remaining_amount == 80000.0  # 100000 - 50000 + 30000


def test_budget_edge_cases():
    """Тест крайних случаев для бюджета"""
    budget = Budget(2024, 1000.0)

    # Точное совпадение суммы расходов с остатком
    budget.add_expense(1000.0)
    assert budget.remaining_amount == 0.0
    assert budget.get_balance() == 0.0

    # Попытка потратить больше после полного расходования
    with pytest.raises(ValueError, match="Недостаточно средств в бюджете"):
        budget.add_expense(1.0)

    # Добавление дохода после полного расходования
    budget.add_revenue(500.0)
    assert budget.remaining_amount == 500.0
    assert budget.get_balance() == 500.0

    # Теперь можно потратить
    budget.add_expense(200.0)
    assert budget.remaining_amount == 300.0
    assert budget.get_balance() == 300.0


