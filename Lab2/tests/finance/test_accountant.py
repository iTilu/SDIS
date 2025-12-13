"""Тесты для класса Accountant"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from finance.accountant import Accountant


def test_accountant_creation_valid():
    """Тест создания бухгалтера с валидными данными"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)
    assert accountant.name == "Иван Петров"
    assert accountant.age == 45
    assert accountant.experience_years == 20
    assert accountant.salary == 90000.0
    assert accountant.certification == ""
    assert accountant.is_available == True
    assert accountant.get_accounts() == []


def test_accountant_creation_invalid_name():
    """Тест создания бухгалтера с невалидным именем"""
    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Accountant("", 45, 20, 90000.0)

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Accountant(None, 45, 20, 90000.0)


def test_accountant_creation_invalid_age():
    """Тест создания бухгалтера с невалидным возрастом"""
    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Accountant("Иван Петров", -5, 20, 90000.0)

    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Accountant("Иван Петров", "45", 20, 90000.0)


def test_accountant_creation_invalid_experience():
    """Тест создания бухгалтера с невалидным опытом"""
    with pytest.raises(ValueError, match="Опыт должен быть неотрицательным целым числом"):
        Accountant("Иван Петров", 45, -1, 90000.0)


def test_accountant_creation_invalid_salary():
    """Тест создания бухгалтера с невалидной зарплатой"""
    with pytest.raises(ValueError, match="Зарплата должна быть неотрицательным числом"):
        Accountant("Иван Петров", 45, 20, -1000.0)

    # Проверяем конвертацию int в float
    accountant = Accountant("Иван Петров", 45, 20, 90000)  # int
    assert accountant.salary == 90000.0
    assert isinstance(accountant.salary, float)


def test_accountant_add_account_valid():
    """Тест добавления валидного счета"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)
    accountant.add_account("Основной счет")
    assert "Основной счет" in accountant.get_accounts()
    assert len(accountant.get_accounts()) == 1


def test_accountant_add_account_invalid():
    """Тест добавления невалидного счета"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    with pytest.raises(TypeError, match="Название счета должно быть строкой"):
        accountant.add_account(123)

    with pytest.raises(TypeError, match="Название счета должно быть строкой"):
        accountant.add_account(None)


def test_accountant_add_account_duplicate():
    """Тест добавления дублированного счета"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)
    accountant.add_account("Основной счет")
    accountant.add_account("Основной счет")  # Дубликат

    accounts = accountant.get_accounts()
    assert accounts.count("Основной счет") == 1  # Должен быть только один экземпляр
    assert len(accounts) == 1


def test_accountant_get_accounts():
    """Тест получения списка счетов"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)
    accountant.add_account("Основной счет")
    accountant.add_account("Резервный счет")

    accounts = accountant.get_accounts()
    assert "Основной счет" in accounts
    assert "Резервный счет" in accounts
    assert len(accounts) == 2

    # Проверяем, что возвращается копия, а не оригинал
    accounts.append("Новый счет")
    assert "Новый счет" not in accountant.get_accounts()  # Оригинал не должен измениться


def test_accountant_get_accounts_empty():
    """Тест получения пустого списка счетов"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)
    accounts = accountant.get_accounts()
    assert accounts == []
    assert len(accounts) == 0


def test_accountant_set_certification_valid():
    """Тест установки валидной сертификации"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)
    accountant.set_certification("CPA")
    assert accountant.certification == "CPA"


def test_accountant_set_certification_invalid():
    """Тест установки невалидной сертификации"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    with pytest.raises(TypeError, match="Сертификация должна быть строкой"):
        accountant.set_certification(123)

    with pytest.raises(TypeError, match="Сертификация должна быть строкой"):
        accountant.set_certification(None)


def test_accountant_calculate_total_earnings():
    """Тест расчета общего заработка бухгалтера"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    earnings = accountant.calculate_total_earnings(12)
    assert earnings == 1080000.0

    earnings = accountant.calculate_total_earnings(1)
    assert earnings == 90000.0

    earnings = accountant.calculate_total_earnings(0)
    assert earnings == 0.0


def test_accountant_calculate_total_earnings_invalid():
    """Тест расчета заработка с невалидными данными"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    with pytest.raises(ValueError, match="Количество месяцев должно быть неотрицательным"):
        accountant.calculate_total_earnings(-1)

    with pytest.raises(ValueError, match="Количество месяцев должно быть неотрицательным"):
        accountant.calculate_total_earnings("12")


def test_accountant_field_types():
    """Тест типов полей бухгалтера"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)
    accountant.set_certification("CPA")
    accountant.add_account("Основной счет")

    assert isinstance(accountant.name, str)
    assert isinstance(accountant.age, int)
    assert isinstance(accountant.experience_years, int)
    assert isinstance(accountant.salary, float)
    assert isinstance(accountant.certification, str)
    assert isinstance(accountant.is_available, bool)
    assert isinstance(accountant.get_accounts(), list)


def test_accountant_data_integrity():
    """Тест целостности данных бухгалтера"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    # Изменяем поля
    accountant.add_account("Основной счет")
    accountant.add_account("Резервный счет")
    accountant.set_certification("CPA")
    accountant.is_available = False

    # Проверяем, что основные поля остались неизменными
    assert accountant.name == "Иван Петров"
    assert accountant.age == 45
    assert accountant.experience_years == 20
    assert accountant.salary == 90000.0

    # Проверяем измененные поля
    assert len(accountant.get_accounts()) == 2
    assert accountant.certification == "CPA"
    assert not accountant.is_available


def test_accountant_boundary_values():
    """Тест граничных значений для бухгалтера"""
    # Максимальный возраст
    accountant1 = Accountant("Старый бухгалтер", 150, 50, 200000.0)
    assert accountant1.age == 150

    # Нулевые значения
    accountant2 = Accountant("Начинающий", 0, 0, 0.0)
    assert accountant2.calculate_total_earnings(12) == 0.0

    # Большая зарплата
    accountant3 = Accountant("Главный бухгалтер", 50, 30, 500000.0)
    assert accountant3.salary == 500000.0


def test_accountant_accounts_management():
    """Тест управления счетами бухгалтера"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    # Добавляем счета
    accounts = ["Основной счет", "Резервный счет", "Инвестиционный счет", "Налоговый счет"]
    for account in accounts:
        accountant.add_account(account)

    assert len(accountant.get_accounts()) == 4
    for account in accounts:
        assert account in accountant.get_accounts()


def test_accountant_certifications():
    """Тест различных сертификаций бухгалтера"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    certifications = ["CPA", "CMA", "CIMA", "ACCA", "ДипИФР", "Росфинмониторинг"]
    for cert in certifications:
        accountant.set_certification(cert)
        assert accountant.certification == cert


def test_accountant_workflow():
    """Тест полного жизненного цикла бухгалтера"""
    # Создание бухгалтера
    accountant = Accountant("Мария Сидорова", 35, 12, 75000.0)

    # Настройка профиля
    accountant.set_certification("CPA")
    accountant.add_account("Зарплатный счет")
    accountant.add_account("Налоговый счет")
    accountant.add_account("Инвестиционный счет")

    # Расчет заработка
    earnings = accountant.calculate_total_earnings(12)

    # Проверки
    assert accountant.name == "Мария Сидорова"
    assert accountant.certification == "CPA"
    assert len(accountant.get_accounts()) == 3
    assert earnings == 900000.0
    assert accountant.is_available == True


def test_accountant_multiple_calculations():
    """Тест множественных расчетов заработка"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    # Разные периоды
    periods = [1, 3, 6, 12, 24]
    expected_earnings = [90000.0, 270000.0, 540000.0, 1080000.0, 2160000.0]

    for period, expected in zip(periods, expected_earnings):
        earnings = accountant.calculate_total_earnings(period)
        assert earnings == expected


def test_accountant_availability_management():
    """Тест управления доступностью бухгалтера"""
    accountant = Accountant("Иван Петров", 45, 20, 90000.0)

    # Начальное состояние
    assert accountant.is_available

    # Изменение доступности
    accountant.is_available = False
    assert not accountant.is_available

    accountant.is_available = True
    assert accountant.is_available


def test_accountant_experience_levels():
    """Тест различных уровней опыта бухгалтера"""
    # Начинающий бухгалтер
    junior = Accountant("Молодой специалист", 25, 2, 45000.0)
    assert junior.experience_years == 2

    # Опытный бухгалтер
    senior = Accountant("Опытный специалист", 50, 25, 120000.0)
    assert senior.experience_years == 25

    # Ветеран
    veteran = Accountant("Ветеран", 65, 40, 150000.0)
    assert veteran.experience_years == 40

    # Проверяем расчеты
    assert junior.calculate_total_earnings(12) == 540000.0
    assert senior.calculate_total_earnings(12) == 1440000.0
    assert veteran.calculate_total_earnings(12) == 1800000.0
