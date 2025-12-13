"""Тесты для класса Audience"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from staff.audience import Audience


def test_audience_creation_valid():
    """Тест создания зрителя с валидными данными"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    assert audience.name == "Анна Иванова"
    assert audience.age == 25
    assert audience.email == "anna@example.com"
    assert audience.loyalty_points == 0
    assert audience.is_member is False
    assert audience.membership_type == ""
    assert audience.get_tickets_purchased() == []


def test_audience_creation_invalid_name():
    """Тест создания зрителя с невалидным именем"""
    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Audience("", 25, "anna@example.com")

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Audience(None, 25, "anna@example.com")

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Audience(123, 25, "anna@example.com")


def test_audience_creation_invalid_age():
    """Тест создания зрителя с невалидным возрастом"""
    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Audience("Анна Иванова", -5, "anna@example.com")

    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Audience("Анна Иванова", "25", "anna@example.com")


def test_audience_creation_invalid_email():
    """Тест создания зрителя с невалидным email"""
    with pytest.raises(ValueError, match="Email должен быть непустой строкой"):
        Audience("Анна Иванова", 25, "")

    with pytest.raises(ValueError, match="Email должен быть непустой строкой"):
        Audience("Анна Иванова", 25, None)


def test_audience_purchase_ticket_valid():
    """Тест покупки валидного билета"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.purchase_ticket("T001")
    assert "T001" in audience.get_tickets_purchased()
    assert audience.loyalty_points == 10


def test_audience_purchase_ticket_invalid():
    """Тест покупки билета с невалидными данными"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")

    with pytest.raises(TypeError, match="Номер билета должен быть строкой"):
        audience.purchase_ticket(123)

    with pytest.raises(TypeError, match="Номер билета должен быть строкой"):
        audience.purchase_ticket(None)


def test_audience_purchase_ticket_duplicate():
    """Тест покупки дублированного билета"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.purchase_ticket("T001")
    audience.purchase_ticket("T001")  # Дубликат

    tickets = audience.get_tickets_purchased()
    assert tickets.count("T001") == 1  # Должен быть только один экземпляр
    assert audience.loyalty_points == 10  # Баллы не должны удваиваться


def test_audience_get_tickets_purchased():
    """Тест получения списка купленных билетов"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.purchase_ticket("T001")
    audience.purchase_ticket("T002")

    tickets = audience.get_tickets_purchased()
    assert "T001" in tickets
    assert "T002" in tickets
    assert len(tickets) == 2

    # Проверяем, что возвращается копия, а не оригинал
    tickets.append("T003")
    assert "T003" not in audience.get_tickets_purchased()  # Оригинал не должен измениться


def test_audience_get_tickets_purchased_empty():
    """Тест получения пустого списка билетов"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    tickets = audience.get_tickets_purchased()
    assert tickets == []
    assert len(tickets) == 0


def test_audience_add_loyalty_points_valid():
    """Тест добавления валидных баллов лояльности"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.add_loyalty_points(50)
    assert audience.loyalty_points == 50

    audience.add_loyalty_points(25)
    assert audience.loyalty_points == 75


def test_audience_add_loyalty_points_invalid():
    """Тест добавления невалидных баллов лояльности"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")

    with pytest.raises(ValueError, match="Баллы должны быть неотрицательным целым числом"):
        audience.add_loyalty_points(-10)

    with pytest.raises(ValueError, match="Баллы должны быть неотрицательным целым числом"):
        audience.add_loyalty_points("50")


def test_audience_become_member_valid():
    """Тест становления членом с валидными данными"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.become_member("Gold")
    assert audience.is_member is True
    assert audience.membership_type == "Gold"


def test_audience_become_member_invalid():
    """Тест становления членом с невалидными данными"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")

    with pytest.raises(TypeError, match="Тип членства должен быть строкой"):
        audience.become_member(123)

    with pytest.raises(TypeError, match="Тип членства должен быть строкой"):
        audience.become_member(None)


def test_audience_field_types():
    """Тест типов полей зрителя"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")
    audience.purchase_ticket("T001")
    audience.add_loyalty_points(50)
    audience.become_member("Silver")

    assert isinstance(audience.name, str)
    assert isinstance(audience.age, int)
    assert isinstance(audience.email, str)
    assert isinstance(audience.loyalty_points, int)
    assert isinstance(audience.is_member, bool)
    assert isinstance(audience.membership_type, str)
    assert isinstance(audience.get_tickets_purchased(), list)


def test_audience_data_integrity():
    """Тест целостности данных зрителя"""
    audience = Audience("Анна Иванова", 25, "anna@example.com")

    # Изменяем поля
    audience.purchase_ticket("T001")
    audience.purchase_ticket("T002")
    audience.add_loyalty_points(100)
    audience.become_member("Platinum")

    # Проверяем, что основные поля остались неизменными
    assert audience.name == "Анна Иванова"
    assert audience.age == 25
    assert audience.email == "anna@example.com"

    # Проверяем измененные поля
    assert len(audience.get_tickets_purchased()) == 2
    assert audience.loyalty_points == 120  # 20 от билетов (2*10) + 100 добавленных = 120
    assert audience.is_member is True
    assert audience.membership_type == "Platinum"


def test_audience_boundary_values():
    """Тест граничных значений для зрителя"""
    # Нулевой возраст
    audience1 = Audience("Младенец", 0, "baby@example.com")
    assert audience1.age == 0

    # Очень большой возраст
    audience2 = Audience("Старик", 150, "old@example.com")
    assert audience2.age == 150

    # Нулевые баллы лояльности
    audience3 = Audience("Новый зритель", 20, "new@example.com")
    assert audience3.loyalty_points == 0


def test_audience_multiple_operations():
    """Тест множественных операций со зрителем"""
    audience = Audience("Активный зритель", 30, "active@example.com")

    # Множественные покупки билетов
    tickets = ["T001", "T002", "T003", "T004", "T005"]
    for ticket in tickets:
        audience.purchase_ticket(ticket)

    # Множественные добавления баллов
    audience.add_loyalty_points(50)
    audience.add_loyalty_points(75)
    audience.add_loyalty_points(25)

    assert len(audience.get_tickets_purchased()) == 5
    assert audience.loyalty_points == 50 + 75 + 25 + (5 * 10)  # 5 билетов * 10 баллов + дополнительные


def test_audience_loyalty_program():
    """Тест программы лояльности"""
    audience = Audience("Лояльный зритель", 35, "loyal@example.com")

    # Начальный статус
    assert not audience.is_member
    assert audience.membership_type == ""

    # Накопление баллов
    for i in range(10):  # 10 билетов = 100 баллов
        audience.purchase_ticket(f"T{i+1:03d}")

    # Становление членом
    audience.become_member("Gold")

    assert audience.is_member
    assert audience.membership_type == "Gold"
    assert audience.loyalty_points == 100  # 10 * 10


def test_audience_workflow():
    """Тест полного жизненного цикла зрителя"""
    # Регистрация
    audience = Audience("Мария Петрова", 28, "maria@example.com")

    # Покупка билетов
    audience.purchase_ticket("PREMIERE001")
    audience.purchase_ticket("SHOW002")

    # Накопление баллов
    audience.add_loyalty_points(50)  # Бонусные баллы

    # Становление членом
    audience.become_member("VIP")

    # Проверки
    assert audience.name == "Мария Петрова"
    assert audience.email == "maria@example.com"
    assert len(audience.get_tickets_purchased()) == 2
    assert audience.loyalty_points == 70  # 20 от билетов + 50 бонусных
    assert audience.is_member
    assert audience.membership_type == "VIP"


def test_audience_seasonal_behavior():
    """Тест сезонного поведения зрителя"""
    # Летний зритель (активный)
    summer_audience = Audience("Летний зритель", 22, "summer@example.com")
    for i in range(5):
        summer_audience.purchase_ticket(f"SUMMER{i+1:03d}")

    # Зимний зритель (менее активный)
    winter_audience = Audience("Зимний зритель", 45, "winter@example.com")
    for i in range(2):
        winter_audience.purchase_ticket(f"WINTER{i+1:03d}")

    assert len(summer_audience.get_tickets_purchased()) == 5
    assert summer_audience.loyalty_points == 50

    assert len(winter_audience.get_tickets_purchased()) == 2
    assert winter_audience.loyalty_points == 20


def test_audience_membership_types():
    """Тест различных типов членства"""
    audience = Audience("Зритель", 30, "member@example.com")

    membership_types = ["Bronze", "Silver", "Gold", "Platinum", "VIP", "Diamond"]

    for membership in membership_types:
        audience.become_member(membership)
        assert audience.membership_type == membership
        assert audience.is_member is True


def test_audience_email_formats():
    """Тест различных форматов email"""
    valid_emails = [
        "user@example.com",
        "user.name@domain.org",
        "user+tag@gmail.com",
        "test.email@subdomain.example.net"
    ]

    for email in valid_emails:
        audience = Audience("Тестовый пользователь", 25, email)
        assert audience.email == email


def test_audience_age_groups():
    """Тест различных возрастных групп"""
    age_groups = [
        ("Ребенок", 5),
        ("Подросток", 15),
        ("Молодой", 25),
        ("Взрослый", 45),
        ("Пожилой", 75)
    ]

    for name, age in age_groups:
        audience = Audience(name, age, f"{name.lower()}@example.com")
        assert audience.age == age
        assert audience.name == name


def test_audience_ticket_patterns():
    """Тест паттернов покупки билетов"""
    audience = Audience("Паттерн-зритель", 30, "pattern@example.com")

    # Разные типы билетов
    ticket_types = ["PREMIERE", "REGULAR", "VIP", "STUDENT", "SENIOR"]
    for ticket_type in ticket_types:
        audience.purchase_ticket(f"{ticket_type}001")

    tickets = audience.get_tickets_purchased()
    assert len(tickets) == 5
    assert all(ticket.endswith("001") for ticket in tickets)
    assert audience.loyalty_points == 50  # 5 * 10


def test_audience_loyalty_milestones():
    """Тест вех программы лояльности"""
    audience = Audience("Веха-зритель", 28, "milestone@example.com")

    # Накопление до различных вех
    milestones = [50, 100, 200, 500, 1000]

    for milestone in milestones:
        current_points = audience.loyalty_points
        points_needed = milestone - current_points
        if points_needed > 0:
            audience.add_loyalty_points(points_needed)
        assert audience.loyalty_points == milestone


def test_audience_error_handling():
    """Тест обработки ошибок"""
    audience = Audience("Тестовый зритель", 25, "test@example.com")

    # Попытка покупки билета с неправильным типом
    with pytest.raises(TypeError):
        audience.purchase_ticket(12345)

    # Попытка добавления отрицательных баллов
    with pytest.raises(ValueError):
        audience.add_loyalty_points(-50)

    # Попытка становления членом с неправильным типом
    with pytest.raises(TypeError):
        audience.become_member(123)


def test_audience_state_consistency():
    """Тест согласованности состояний"""
    audience = Audience("Согласованный зритель", 35, "consistent@example.com")

    # Начальное состояние
    assert not audience.is_member
    assert audience.membership_type == ""
    assert audience.loyalty_points == 0

    # После покупки билетов
    audience.purchase_ticket("T001")
    assert audience.loyalty_points == 10
    assert not audience.is_member

    # После становления членом
    audience.become_member("Gold")
    assert audience.is_member
    assert audience.membership_type == "Gold"

    # После добавления баллов
    audience.add_loyalty_points(100)
    assert audience.loyalty_points == 110

