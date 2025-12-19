"""Тесты для класса TicketSeller"""
import pytest
import sys
import os
from datetime import datetime, timedelta
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from Lab2.staff.ticket_seller import TicketSeller
from Lab2.venues.box_office import BoxOffice
from Lab2.tickets.ticket import Ticket
from Lab2.finance.budget import Budget
from Lab2.tickets.order import Order
from Lab2.tickets.sale import Sale
from Lab2.finance.payment import Payment


def test_ticket_seller_creation():
    """Тест создания билетера"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    assert seller.name == "Ольга Сидорова"
    assert seller.age == 25
    assert seller.experience_years == 2
    assert seller.salary == 30000.0
    assert seller.workplace_number == 0
    assert seller.is_available == True
    assert seller.sold_tickets_count == 0


def test_ticket_seller_shift_management():
    """Тест управления сменой"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    box_office = BoxOffice(1, "Главный зал")

    # Назначаем кассу
    seller.assign_to_box_office(box_office)
    assert seller._TicketSeller__box_office == box_office

    # Начинаем смену
    seller.start_shift()
    assert seller.is_available == True

    # Заканчиваем смену
    seller.end_shift()
    assert seller.is_available == False


def test_ticket_seller_order_management():
    """Тест управления заказами"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    box_office = BoxOffice(1, "Главный зал")
    seller.assign_to_box_office(box_office)
    seller.start_shift()

    # Создаем заказ
    order = seller.create_order("Иван Петров")
    assert order.customer_name == "Иван Петров"
    assert order.order_number.startswith("ORD")
    assert seller.get_current_order() == order

    # Пытаемся создать второй заказ (должна быть ошибка)
    with pytest.raises(ValueError, match="уже есть активный заказ"):
        seller.create_order("Мария Иванова")


def test_ticket_seller_ticket_operations():
    """Тест операций с билетами"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    box_office = BoxOffice(1, "Главный зал")
    seller.assign_to_box_office(box_office)
    seller.start_shift()

    # Создаем билеты
    ticket1 = Ticket("T001", "Гамлет", 1500.0, "A1")
    ticket2 = Ticket("T002", "Гамлет", 1500.0, "A2")
    seller.add_available_tickets([ticket1, ticket2])

    # Ищем доступные билеты
    available = seller.find_available_tickets("Гамлет")
    assert len(available) == 2

    # Создаем заказ и добавляем билеты
    order = seller.create_order("Иван Петров")
    seller.add_ticket_to_order(ticket1)
    seller.add_ticket_to_order(ticket2)

    assert len(order.get_tickets()) == 2
    assert order.total_amount == 3000.0

    # После добавления в заказ билеты все еще доступны для поиска
    available_after_add = seller.find_available_tickets("Гамлет")
    assert len(available_after_add) == 2

    # Оформляем продажу - теперь билеты должны стать недоступными
    seller.process_sale("Карта")

    # Проверяем, что билеты теперь недоступны
    available_after_sale = seller.find_available_tickets("Гамлет")
    assert len(available_after_sale) == 0


def test_ticket_seller_sale_processing():
    """Тест обработки продаж"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    box_office = BoxOffice(1, "Главный зал")
    seller.assign_to_box_office(box_office)
    seller.start_shift()

    # Создаем билеты и заказ
    ticket = Ticket("T001", "Гамлет", 1500.0, "A1")
    seller.add_available_tickets([ticket])

    order = seller.create_order("Иван Петров")
    seller.add_ticket_to_order(ticket)

    # Оформляем продажу
    sale = seller.process_sale("Карта")
    assert sale.sale_number.startswith("SALE")
    assert sale.amount == 1500.0
    assert sale.seller_name == seller.name
    assert sale.payment_method == "Карта"

    # Проверяем статистику
    assert seller.sold_tickets_count == 1
    assert box_office.daily_revenue == 1500.0

    # Проверяем, что заказ завершен
    assert seller.get_current_order() is None


def test_ticket_seller_error_handling():
    """Тест обработки ошибок"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)

    # Ошибка при начале смены без кассы
    with pytest.raises(ValueError, match="должен быть назначен на кассу"):
        seller.start_shift()

    # Сначала делаем продавца недоступным
    seller.set_availability(False)

    # Ошибка при создании заказа когда продавец недоступен
    with pytest.raises(ValueError, match="Продавец недоступен"):
        seller.create_order("Иван Петров")

    # Ошибка при добавлении билета без заказа
    ticket = Ticket("T001", "Гамлет", 1500.0, "A1")
    with pytest.raises(ValueError, match="Нет активного заказа"):
        seller.add_ticket_to_order(ticket)

    # Ошибка при продаже без заказа
    with pytest.raises(ValueError, match="Нет активного заказа"):
        seller.process_sale("Карта")


def test_ticket_seller_shift_report():
    """Тест генерации отчета за смену"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    seller.set_workplace_number(5)

    report = seller.generate_shift_report()
    assert seller.name in report
    assert "Касса №5" in report
    assert "Продано билетов: 0" in report


def test_ticket_seller_budget_integration():
    """Тест интеграции с бюджетом"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    budget = Budget(2024, 100000.0)
    seller.assign_budget(budget)

    box_office = BoxOffice(1, "Главный зал")
    seller.assign_to_box_office(box_office)
    seller.start_shift()

    # Создаем и продаем билет
    ticket = Ticket("T001", "Гамлет", 1500.0, "A1")
    seller.add_available_tickets([ticket])

    order = seller.create_order("Иван Петров")
    seller.add_ticket_to_order(ticket)
    sale = seller.process_sale("Карта")

    # Проверяем, что доход добавлен в бюджет
    assert budget.get_total_revenues() == 1500.0
    assert budget.get_balance() == 100000.0 + 1500.0


def test_ticket_seller_ticket_reservation():
    """Тест резервирования билетов"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    box_office = BoxOffice(1, "Главный зал")
    seller.assign_to_box_office(box_office)
    seller.start_shift()

    ticket = Ticket("T001", "Гамлет", 1500.0, "A1")
    seller.add_available_tickets([ticket])

    # Резервируем билет
    seller.reserve_ticket(ticket, "Мария Иванова", 10)
    assert len(seller.get_reserved_tickets()) == 1

    # Проверяем, что зарезервированный билет все еще доступен для поиска
    available = seller.find_available_tickets("Гамлет")
    assert len(available) == 1

    # Отменяем резервирование
    seller.cancel_reservation(ticket)
    assert len(seller.get_reserved_tickets()) == 0


def test_ticket_seller_discount_application():
    """Тест применения скидок"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    box_office = BoxOffice(1, "Главный зал")
    seller.assign_to_box_office(box_office)
    seller.start_shift()

    ticket = Ticket("T001", "Гамлет", 2000.0, "A1")
    seller.add_available_tickets([ticket])

    order = seller.create_order("Иван Петров")
    seller.add_ticket_to_order(ticket)
    assert order.total_amount == 2000.0

    # Применяем скидку 10%
    seller.apply_discount(order, 10.0)
    assert order.total_amount == 1800.0


def test_ticket_seller_ticket_refund():
    """Тест возврата билетов"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    budget = Budget(2024, 100000.0)
    seller.assign_budget(budget)

    box_office = BoxOffice(1, "Главный зал")
    seller.assign_to_box_office(box_office)
    seller.start_shift()

    ticket = Ticket("T001", "Гамлет", 1500.0, "A1")
    seller.add_available_tickets([ticket])

    # Продаем билет
    order = seller.create_order("Иван Петров")
    seller.add_ticket_to_order(ticket)
    sale = seller.process_sale("Карта")

    assert seller.sold_tickets_count == 1
    assert budget.get_total_revenues() == 1500.0

    # Возвращаем билет
    seller.process_refund(ticket, "Передумал идти")

    assert seller.sold_tickets_count == 0
    # При возврате добавляем как расход
    assert budget.get_total_expenses() == 1500.0


def test_ticket_seller_payment_validation():
    """Тест валидации платежей"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)

    # Создаем платеж
    payment = Payment("PAY001", 1500.0, datetime.now())
    payment.set_recipient("Театр")
    payment.complete()

    # Валидируем платеж
    assert seller.validate_payment(payment, 1500.0)

    # Тест на неправильную сумму
    with pytest.raises(ValueError, match="Сумма платежа"):
        seller.validate_payment(payment, 1000.0)

    # Тест на незавершенный платеж
    incomplete_payment = Payment("PAY002", 1500.0, datetime.now())
    with pytest.raises(ValueError, match="Платеж не завершен"):
        seller.validate_payment(incomplete_payment, 1500.0)


def test_ticket_seller_sales_statistics():
    """Тест получения статистики продаж"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    seller.set_workplace_number(3)

    box_office = BoxOffice(3, "VIP зал")
    seller.assign_to_box_office(box_office)

    stats = seller.get_sales_statistics()

    assert stats["seller_name"] == "Ольга Сидорова"
    assert stats["workplace"] == 3
    assert stats["sold_tickets"] == 0
    assert stats["reserved_tickets"] == 0
    assert stats["available_tickets"] == 0


def test_ticket_seller_reservation_expiry():
    """Тест истечения резервирования"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    box_office = BoxOffice(1, "Главный зал")
    seller.assign_to_box_office(box_office)
    seller.start_shift()

    ticket = Ticket("T001", "Гамлет", 1500.0, "A1")
    seller.add_available_tickets([ticket])

    # Резервируем на 1 минуту
    seller.reserve_ticket(ticket, "Мария Иванова", 1)

    # Имитируем истечение времени (меняем reservation_time на прошедшее время)
    past_time = datetime.now() - timedelta(minutes=2)
    ticket._Ticket__reservation_time = past_time

    # При получении списка резервированных просроченные должны удаляться
    reserved = seller.get_reserved_tickets()
    assert len(reserved) == 0


def test_ticket_seller_bulk_operations():
    """Тест массовых операций"""
    seller = TicketSeller("Ольга Сидорова", 25, 2, 30000.0)
    box_office = BoxOffice(1, "Главный зал")
    budget = Budget(2024, 100000.0)
    seller.assign_to_box_office(box_office)
    seller.assign_budget(budget)
    seller.start_shift()

    # Создаем несколько билетов
    tickets = [
        Ticket("T001", "Гамлет", 1500.0, "A1"),
        Ticket("T002", "Гамлет", 1500.0, "A2"),
        Ticket("T003", "Отелло", 1200.0, "B1")
    ]
    seller.add_available_tickets(tickets)

    # Создаем заказ на несколько билетов
    order = seller.create_order("Семья Петровых")
    seller.add_ticket_to_order(tickets[0])
    seller.add_ticket_to_order(tickets[1])
    seller.add_ticket_to_order(tickets[2])

    assert order.total_amount == 4200.0

    # Применяем скидку для семьи
    seller.apply_discount(order, 15.0)  # 15% скидка
    assert order.total_amount == 3570.0

    # Оформляем продажу
    sale = seller.process_sale("Карта")

    assert seller.sold_tickets_count == 3
    assert budget.get_total_revenues() == 3570.0
    assert box_office.daily_revenue == 3570.0

