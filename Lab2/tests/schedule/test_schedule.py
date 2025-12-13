"""Тесты для класса Schedule"""
import pytest
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from schedule.schedule import Schedule


def test_schedule_creation_valid():
    """Тест создания расписания с валидными данными"""
    schedule = Schedule(1, 2024)
    assert schedule.month == 1
    assert schedule.year == 2024
    assert schedule.is_published == False
    assert isinstance(schedule.last_updated, datetime)
    assert schedule.get_events() == []
    assert schedule.get_performances() == []


def test_schedule_creation_invalid_month():
    """Тест создания расписания с невалидным месяцем"""
    with pytest.raises(ValueError, match="Месяц должен быть числом от 1 до 12"):
        Schedule(0, 2024)

    with pytest.raises(ValueError, match="Месяц должен быть числом от 1 до 12"):
        Schedule(13, 2024)

    with pytest.raises(ValueError, match="Месяц должен быть числом от 1 до 12"):
        Schedule("1", 2024)


def test_schedule_creation_invalid_year():
    """Тест создания расписания с невалидным годом"""
    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        Schedule(1, -1)

    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        Schedule(1, "2024")


def test_schedule_add_event_valid():
    """Тест добавления валидного события"""
    schedule = Schedule(1, 2024)
    schedule.add_event("Премьера Гамлета")
    assert "Премьера Гамлета" in schedule.get_events()
    assert len(schedule.get_events()) == 1


def test_schedule_add_event_invalid():
    """Тест добавления невалидного события"""
    schedule = Schedule(1, 2024)

    with pytest.raises(TypeError, match="Название события должно быть строкой"):
        schedule.add_event(123)

    with pytest.raises(TypeError, match="Название события должно быть строкой"):
        schedule.add_event(None)


def test_schedule_add_event_duplicate():
    """Тест добавления дублированного события"""
    schedule = Schedule(1, 2024)
    schedule.add_event("Премьера")
    schedule.add_event("Премьера")  # Дубликат

    events = schedule.get_events()
    assert events.count("Премьера") == 1  # Должен быть только один экземпляр
    assert len(events) == 1


def test_schedule_get_events():
    """Тест получения списка событий"""
    schedule = Schedule(1, 2024)
    schedule.add_event("Премьера")
    schedule.add_event("Репетиция")

    events = schedule.get_events()
    assert "Премьера" in events
    assert "Репетиция" in events
    assert len(events) == 2

    # Проверяем, что возвращается копия, а не оригинал
    events.append("Новое событие")
    assert "Новое событие" not in schedule.get_events()  # Оригинал не должен измениться


def test_schedule_get_events_empty():
    """Тест получения пустого списка событий"""
    schedule = Schedule(1, 2024)
    events = schedule.get_events()
    assert events == []
    assert len(events) == 0


def test_schedule_add_performance_valid():
    """Тест добавления валидного спектакля"""
    schedule = Schedule(1, 2024)
    schedule.add_performance("Гамлет")
    assert "Гамлет" in schedule.get_performances()
    assert len(schedule.get_performances()) == 1


def test_schedule_add_performance_invalid():
    """Тест добавления невалидного спектакля"""
    schedule = Schedule(1, 2024)

    with pytest.raises(TypeError, match="Название спектакля должно быть строкой"):
        schedule.add_performance(456)

    with pytest.raises(TypeError, match="Название спектакля должно быть строкой"):
        schedule.add_performance(None)


def test_schedule_add_performance_duplicate():
    """Тест добавления дублированного спектакля"""
    schedule = Schedule(1, 2024)
    schedule.add_performance("Гамлет")
    schedule.add_performance("Гамлет")  # Дубликат

    performances = schedule.get_performances()
    assert performances.count("Гамлет") == 1  # Должен быть только один экземпляр
    assert len(performances) == 1


def test_schedule_get_performances():
    """Тест получения списка спектаклей"""
    schedule = Schedule(1, 2024)
    schedule.add_performance("Гамлет")
    schedule.add_performance("Отелло")

    performances = schedule.get_performances()
    assert "Гамлет" in performances
    assert "Отелло" in performances
    assert len(performances) == 2

    # Проверяем, что возвращается копия, а не оригинал
    performances.append("Макбет")
    assert "Макбет" not in schedule.get_performances()  # Оригинал не должен измениться


def test_schedule_get_performances_empty():
    """Тест получения пустого списка спектаклей"""
    schedule = Schedule(1, 2024)
    performances = schedule.get_performances()
    assert performances == []
    assert len(performances) == 0


def test_schedule_publish():
    """Тест публикации расписания"""
    schedule = Schedule(1, 2024)
    assert not schedule.is_published

    schedule.publish()
    assert schedule.is_published == True


def test_schedule_events_property():
    """Тест свойства events"""
    schedule = Schedule(1, 2024)
    schedule.add_event("Премьера")

    # Проверяем, что events - это свойство, возвращающее список
    assert hasattr(schedule, 'events')
    assert isinstance(schedule.events, list)
    assert "Премьера" in schedule.events


def test_schedule_performances_property():
    """Тест свойства performances"""
    schedule = Schedule(1, 2024)
    schedule.add_performance("Гамлет")

    # Проверяем, что performances - это свойство, возвращающее список
    assert hasattr(schedule, 'performances')
    assert isinstance(schedule.performances, list)
    assert "Гамлет" in schedule.performances


def test_schedule_field_types():
    """Тест типов полей расписания"""
    schedule = Schedule(1, 2024)
    schedule.add_event("Событие")
    schedule.add_performance("Спектакль")

    assert isinstance(schedule.month, int)
    assert isinstance(schedule.year, int)
    assert isinstance(schedule.is_published, bool)
    assert isinstance(schedule.last_updated, datetime)
    assert isinstance(schedule.get_events(), list)
    assert isinstance(schedule.get_performances(), list)


def test_schedule_data_integrity():
    """Тест целостности данных расписания"""
    schedule = Schedule(1, 2024)

    # Изменяем поля
    schedule.add_event("Премьера")
    schedule.add_event("Репетиция")
    schedule.add_performance("Гамлет")
    schedule.add_performance("Отелло")
    schedule.publish()

    # Проверяем, что основные поля остались неизменными
    assert schedule.month == 1
    assert schedule.year == 2024

    # Проверяем измененные поля
    assert len(schedule.get_events()) == 2
    assert len(schedule.get_performances()) == 2
    assert schedule.is_published == True


def test_schedule_boundary_values():
    """Тест граничных значений для расписания"""
    # Граничные значения месяцев
    schedule1 = Schedule(1, 2024)  # Первый месяц
    assert schedule1.month == 1

    schedule2 = Schedule(12, 2024)  # Последний месяц
    assert schedule2.month == 12

    # Нулевой год
    schedule3 = Schedule(1, 0)
    assert schedule3.year == 0


def test_schedule_multiple_operations():
    """Тест множественных операций с расписанием"""
    schedule = Schedule(1, 2024)

    # Добавляем множественные события и спектакли
    events = ["Премьера", "Репетиция", "Концерт", "Выставка"]
    performances = ["Гамлет", "Отелло", "Король Лир", "Макбет"]

    for event in events:
        schedule.add_event(event)

    for performance in performances:
        schedule.add_performance(performance)

    assert len(schedule.get_events()) == 4
    assert len(schedule.get_performances()) == 4

    # Публикуем расписание
    schedule.publish()
    assert schedule.is_published


def test_schedule_workflow():
    """Тест полного жизненного цикла расписания"""
    # Создание расписания
    schedule = Schedule(3, 2024)  # Март 2024

    # Добавление событий
    schedule.add_event("Международный день театра")
    schedule.add_event("День рождения театра")

    # Добавление спектаклей
    schedule.add_performance("Вишневый сад")
    schedule.add_performance("Чайка")

    # Публикация
    schedule.publish()

    # Проверки
    assert schedule.month == 3
    assert schedule.year == 2024
    assert len(schedule.get_events()) == 2
    assert len(schedule.get_performances()) == 2
    assert schedule.is_published == True
    assert isinstance(schedule.last_updated, datetime)


def test_schedule_seasonal_schedules():
    """Тест расписаний для разных сезонов"""
    # Весеннее расписание
    spring = Schedule(4, 2024)
    spring.add_event("Весенний фестиваль")
    spring.add_performance("Ромео и Джульетта")

    # Летнее расписание
    summer = Schedule(7, 2024)
    summer.add_event("Летний сезон")
    summer.add_performance("Сон в летнюю ночь")

    # Осеннее расписание
    autumn = Schedule(10, 2024)
    autumn.add_event("Осенний марафон")
    autumn.add_performance("Ревизор")

    # Зимнее расписание
    winter = Schedule(12, 2024)
    winter.add_event("Новогодние праздники")
    winter.add_performance("Щелкунчик")

    # Проверки
    assert spring.month == 4 and len(spring.get_events()) == 1
    assert summer.month == 7 and len(summer.get_performances()) == 1
    assert autumn.month == 10 and autumn.get_events()[0] == "Осенний марафон"
    assert winter.month == 12 and winter.get_performances()[0] == "Щелкунчик"

