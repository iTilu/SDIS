"""Тесты для класса Ticket"""
import pytest
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from tickets.ticket import Ticket


def test_ticket_creation_valid():
    """Тест создания билета с валидными данными"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    assert ticket.ticket_number == "T001"
    assert ticket.performance_name == "Гамлет"
    assert ticket.price == 1500.0
    assert ticket.seat_number == "A12"
    assert ticket.purchase_date is None
    assert ticket.is_sold == False
    assert ticket.is_used == False
    assert ticket.section == ""


def test_ticket_creation_invalid_ticket_number():
    """Тест создания билета с невалидным номером"""
    with pytest.raises(ValueError, match="Номер билета должен быть непустой строкой"):
        Ticket("", "Гамлет", 1500.0, "A12")

    with pytest.raises(ValueError, match="Номер билета должен быть непустой строкой"):
        Ticket(None, "Гамлет", 1500.0, "A12")


def test_ticket_creation_invalid_performance_name():
    """Тест создания билета с невалидным названием спектакля"""
    with pytest.raises(ValueError, match="Название спектакля должно быть непустой строкой"):
        Ticket("T001", "", 1500.0, "A12")

    with pytest.raises(ValueError, match="Название спектакля должно быть непустой строкой"):
        Ticket("T001", None, 1500.0, "A12")


def test_ticket_creation_invalid_price():
    """Тест создания билета с невалидной ценой"""
    with pytest.raises(ValueError, match="Цена должна быть неотрицательным числом"):
        Ticket("T001", "Гамлет", -100.0, "A12")

    with pytest.raises(ValueError, match="Цена должна быть неотрицательным числом"):
        Ticket("T001", "Гамлет", "1500", "A12")

    # Проверяем конвертацию int в float
    ticket = Ticket("T001", "Гамлет", 1500, "A12")  # int
    assert ticket.price == 1500.0
    assert isinstance(ticket.price, float)


def test_ticket_creation_zero_price():
    """Тест создания билета с нулевой ценой"""
    ticket = Ticket("T001", "Гамлет", 0.0, "A12")
    assert ticket.price == 0.0


def test_ticket_creation_invalid_seat_number():
    """Тест создания билета с невалидным номером места"""
    with pytest.raises(ValueError, match="Номер места должен быть непустой строкой"):
        Ticket("T001", "Гамлет", 1500.0, "")

    with pytest.raises(ValueError, match="Номер места должен быть непустой строкой"):
        Ticket("T001", "Гамлет", 1500.0, None)


def test_ticket_sell_valid():
    """Тест продажи валидного билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    purchase_date = datetime(2024, 1, 15, 14, 30)

    ticket.sell(purchase_date)
    assert ticket.is_sold == True
    assert ticket.purchase_date == purchase_date
    assert ticket.is_used == False


def test_ticket_sell_invalid_date():
    """Тест продажи билета с невалидной датой"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")

    with pytest.raises(TypeError, match="Дата покупки должна быть объектом datetime"):
        ticket.sell("2024-01-15")

    with pytest.raises(TypeError, match="Дата покупки должна быть объектом datetime"):
        ticket.sell(None)


def test_ticket_sell_already_sold():
    """Тест повторной продажи уже проданного билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    first_date = datetime(2024, 1, 15, 14, 30)
    second_date = datetime(2024, 1, 16, 16, 45)

    ticket.sell(first_date)
    ticket.sell(second_date)  # Повторная продажа

    # Дата должна обновиться на последнюю
    assert ticket.is_sold == True
    assert ticket.purchase_date == second_date


def test_ticket_use_valid():
    """Тест использования проданного билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    purchase_date = datetime(2024, 1, 15, 14, 30)

    ticket.sell(purchase_date)
    ticket.use()

    assert ticket.is_sold == True
    assert ticket.is_used == True
    assert ticket.purchase_date == purchase_date


def test_ticket_use_unsold():
    """Тест использования непроданного билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")

    with pytest.raises(ValueError, match="Билет должен быть продан перед использованием"):
        ticket.use()

    assert ticket.is_used == False


def test_ticket_use_already_used():
    """Тест повторного использования уже использованного билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    purchase_date = datetime(2024, 1, 15, 14, 30)

    ticket.sell(purchase_date)
    ticket.use()
    ticket.use()  # Повторное использование

    # Билет остается использованным
    assert ticket.is_sold == True
    assert ticket.is_used == True


def test_ticket_set_section_valid():
    """Тест установки валидной секции"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    ticket.set_section("Партер")
    assert ticket.section == "Партер"


def test_ticket_set_section_invalid():
    """Тест установки невалидной секции"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")

    with pytest.raises(TypeError, match="Секция должна быть строкой"):
        ticket.set_section(123)

    with pytest.raises(TypeError, match="Секция должна быть строкой"):
        ticket.set_section(None)


def test_ticket_set_section_empty():
    """Тест установки пустой секции"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    ticket.set_section("")
    assert ticket.section == ""


def test_ticket_is_valid_new():
    """Тест валидности нового билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    assert ticket.is_valid() == False  # Не продан


def test_ticket_is_valid_sold():
    """Тест валидности проданного билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    purchase_date = datetime(2024, 1, 15, 14, 30)

    ticket.sell(purchase_date)
    assert ticket.is_valid() == True  # Продан, но не использован


def test_ticket_is_valid_used():
    """Тест валидности использованного билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    purchase_date = datetime(2024, 1, 15, 14, 30)

    ticket.sell(purchase_date)
    ticket.use()
    assert ticket.is_valid() == False  # Продан и использован


def test_ticket_field_types():
    """Тест типов полей билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    purchase_date = datetime(2024, 1, 15, 14, 30)

    ticket.sell(purchase_date)
    ticket.set_section("Партер")

    assert isinstance(ticket.ticket_number, str)
    assert isinstance(ticket.performance_name, str)
    assert isinstance(ticket.price, float)
    assert isinstance(ticket.seat_number, str)
    assert ticket.purchase_date is None or isinstance(ticket.purchase_date, datetime)
    assert isinstance(ticket.is_sold, bool)
    assert isinstance(ticket.is_used, bool)
    assert isinstance(ticket.section, str)


def test_ticket_data_integrity():
    """Тест целостности данных билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")
    purchase_date = datetime(2024, 1, 15, 14, 30)

    # Изменяем поля
    ticket.sell(purchase_date)
    ticket.set_section("Партер")
    ticket.use()

    # Проверяем, что основные поля остались неизменными
    assert ticket.ticket_number == "T001"
    assert ticket.performance_name == "Гамлет"
    assert ticket.price == 1500.0
    assert ticket.seat_number == "A12"

    # Проверяем измененные поля
    assert ticket.is_sold == True
    assert ticket.is_used == True
    assert ticket.purchase_date == purchase_date
    assert ticket.section == "Партер"


def test_ticket_boundary_values():
    """Тест граничных значений для билета"""
    # Нулевая цена
    ticket1 = Ticket("T001", "Бесплатный спектакль", 0.0, "A1")
    assert ticket1.price == 0.0

    # Очень большая цена
    ticket2 = Ticket("T002", "Элитный спектакль", 1000000.0, "VIP1")
    assert ticket2.price == 1000000.0

    # Разные номера мест
    ticket3 = Ticket("T003", "Спектакль", 1500.0, "1")  # Цифровой номер
    assert ticket3.seat_number == "1"

    ticket4 = Ticket("T004", "Спектакль", 1500.0, "A100")  # Буквенно-цифровой
    assert ticket4.seat_number == "A100"


def test_ticket_workflow():
    """Тест полного жизненного цикла билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")

    # Начальное состояние
    assert not ticket.is_sold
    assert not ticket.is_used
    assert not ticket.is_valid()

    # Продажа
    purchase_date = datetime(2024, 1, 15, 14, 30)
    ticket.sell(purchase_date)
    assert ticket.is_sold
    assert not ticket.is_used
    assert ticket.is_valid()
    assert ticket.purchase_date == purchase_date

    # Установка секции
    ticket.set_section("Партер")
    assert ticket.section == "Партер"

    # Использование
    ticket.use()
    assert ticket.is_sold
    assert ticket.is_used
    assert not ticket.is_valid()


def test_ticket_multiple_operations():
    """Тест множественных операций с билетом"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")

    # Множественные продажи (обновление даты)
    dates = [
        datetime(2024, 1, 15, 10, 0),
        datetime(2024, 1, 15, 14, 30),
        datetime(2024, 1, 16, 19, 0)
    ]

    for date in dates:
        ticket.sell(date)

    assert ticket.purchase_date == dates[-1]  # Последняя дата

    # Множественные использования
    ticket.use()
    ticket.use()  # Повторное использование
    assert ticket.is_used  # Остается использованным


def test_ticket_section_operations():
    """Тест операций с секцией билета"""
    ticket = Ticket("T001", "Гамлет", 1500.0, "A12")

    # Изменение секции
    sections = ["Партер", "Бельэтаж", "Балкон", "Ложа"]
    for section in sections:
        ticket.set_section(section)
        assert ticket.section == section


def test_ticket_validation_scenarios():
    """Тест различных сценариев валидации билета"""
    # Сценарий 1: Новый билет
    ticket1 = Ticket("T001", "Гамлет", 1500.0, "A12")
    assert not ticket1.is_valid()

    # Сценарий 2: Проданный билет
    ticket2 = Ticket("T002", "Отелло", 1200.0, "B5")
    ticket2.sell(datetime.now())
    assert ticket2.is_valid()

    # Сценарий 3: Использованный билет
    ticket3 = Ticket("T003", "Макбет", 1300.0, "C8")
    ticket3.sell(datetime.now())
    ticket3.use()
    assert not ticket3.is_valid()

    # Сценарий 4: Билет с нулевой ценой
    ticket4 = Ticket("T004", "Бесплатный", 0.0, "D1")
    ticket4.sell(datetime.now())
    assert ticket4.is_valid()

