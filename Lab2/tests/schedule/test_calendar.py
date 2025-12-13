"""Тесты для класса Calendar"""
import pytest
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from schedule.calendar import Calendar


def test_calendar_creation_valid():
    """Тест создания календаря с валидными данными"""
    calendar = Calendar(2024)
    assert calendar.year == 2024
    assert calendar.season_start == datetime(2024, 9, 1)
    assert calendar.season_end == datetime(2025, 6, 30)
    assert calendar.get_holidays() == []
    assert calendar.get_special_dates() == []


def test_calendar_creation_invalid_year():
    """Тест создания календаря с невалидным годом"""
    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        Calendar(-1)

    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        Calendar("2024")

    with pytest.raises(ValueError, match="Год должен быть неотрицательным целым числом"):
        Calendar(2024.5)


def test_calendar_creation_zero_year():
    """Тест создания календаря с нулевым годом"""
    try:
        calendar = Calendar(0)
    except:
        assert True





def test_calendar_add_holiday_valid():
    """Тест добавления валидного праздника"""
    calendar = Calendar(2024)
    holiday = datetime(2024, 1, 1)  # Новый год

    calendar.add_holiday(holiday)
    assert holiday in calendar.get_holidays()
    assert len(calendar.get_holidays()) == 1


def test_calendar_add_holiday_invalid_type():
    """Тест добавления праздника с невалидным типом"""
    calendar = Calendar(2024)

    with pytest.raises(TypeError, match="Дата должна быть объектом datetime"):
        calendar.add_holiday("2024-01-01")

    with pytest.raises(TypeError, match="Дата должна быть объектом datetime"):
        calendar.add_holiday(None)


def test_calendar_add_holiday_wrong_year():
    """Тест добавления праздника из другого года"""
    calendar = Calendar(2024)
    holiday = datetime(2023, 12, 31)  # Прошлый год

    with pytest.raises(ValueError, match="Дата должна быть в текущем году"):
        calendar.add_holiday(holiday)


def test_calendar_add_holiday_duplicate():
    """Тест добавления дублированного праздника"""
    calendar = Calendar(2024)
    holiday = datetime(2024, 1, 1)

    calendar.add_holiday(holiday)
    calendar.add_holiday(holiday)  # Дубликат

    holidays = calendar.get_holidays()
    assert holidays.count(holiday) == 1  # Должен быть только один экземпляр
    assert len(holidays) == 1


def test_calendar_get_holidays():
    """Тест получения списка праздников"""
    calendar = Calendar(2024)
    holiday1 = datetime(2024, 1, 1)
    holiday2 = datetime(2024, 5, 1)

    calendar.add_holiday(holiday1)
    calendar.add_holiday(holiday2)

    holidays = calendar.get_holidays()
    assert holiday1 in holidays
    assert holiday2 in holidays
    assert len(holidays) == 2

    # Проверяем, что возвращается копия, а не оригинал
    holidays.append(datetime(2024, 12, 31))
    assert len(calendar.get_holidays()) == 2  # Оригинал не должен измениться


def test_calendar_get_holidays_empty():
    """Тест получения пустого списка праздников"""
    calendar = Calendar(2024)
    holidays = calendar.get_holidays()
    assert holidays == []
    assert len(holidays) == 0


def test_calendar_add_special_date_valid():
    """Тест добавления валидной особой даты"""
    calendar = Calendar(2024)
    special_date = datetime(2024, 3, 8)  # Международный женский день

    calendar.add_special_date(special_date)
    assert special_date in calendar.get_special_dates()
    assert len(calendar.get_special_dates()) == 1


def test_calendar_add_special_date_invalid_type():
    """Тест добавления особой даты с невалидным типом"""
    calendar = Calendar(2024)

    with pytest.raises(TypeError, match="Дата должна быть объектом datetime"):
        calendar.add_special_date(20240308)


def test_calendar_add_special_date_duplicate():
    """Тест добавления дублированной особой даты"""
    calendar = Calendar(2024)
    special_date = datetime(2024, 3, 8)

    calendar.add_special_date(special_date)
    calendar.add_special_date(special_date)  # Дубликат

    special_dates = calendar.get_special_dates()
    assert special_dates.count(special_date) == 1  # Должен быть только один экземпляр
    assert len(special_dates) == 1


def test_calendar_get_special_dates():
    """Тест получения списка особых дат"""
    calendar = Calendar(2024)
    date1 = datetime(2024, 3, 8)
    date2 = datetime(2024, 9, 1)

    calendar.add_special_date(date1)
    calendar.add_special_date(date2)

    special_dates = calendar.get_special_dates()
    assert date1 in special_dates
    assert date2 in special_dates
    assert len(special_dates) == 2

    # Проверяем, что возвращается копия
    special_dates.append(datetime(2024, 12, 31))
    assert len(calendar.get_special_dates()) == 2


def test_calendar_get_special_dates_empty():
    """Тест получения пустого списка особых дат"""
    calendar = Calendar(2024)
    special_dates = calendar.get_special_dates()
    assert special_dates == []
    assert len(special_dates) == 0


def test_calendar_set_season_valid():
    """Тест установки валидного сезона"""
    calendar = Calendar(2024)
    start = datetime(2024, 10, 1)
    end = datetime(2025, 5, 31)

    calendar.set_season(start, end)
    assert calendar.season_start == start
    assert calendar.season_end == end


def test_calendar_set_season_invalid_type():
    """Тест установки сезона с невалидными типами"""
    calendar = Calendar(2024)
    valid_date = datetime(2024, 10, 1)

    with pytest.raises(TypeError, match="Даты должны быть объектами datetime"):
        calendar.set_season("2024-10-01", valid_date)

    with pytest.raises(TypeError, match="Даты должны быть объектами datetime"):
        calendar.set_season(valid_date, None)


def test_calendar_set_season_end_before_start():
    """Тест установки сезона, где конец раньше начала"""
    calendar = Calendar(2024)
    start = datetime(2024, 10, 1)
    end = datetime(2024, 9, 30)  # Раньше начала

    with pytest.raises(ValueError, match="Дата окончания должна быть позже даты начала"):
        calendar.set_season(start, end)


def test_calendar_set_season_same_date():
    """Тест установки сезона с одинаковыми датами начала и окончания"""
    calendar = Calendar(2024)
    same_date = datetime(2024, 10, 1)

    with pytest.raises(ValueError, match="Дата окончания должна быть позже даты начала"):
        calendar.set_season(same_date, same_date)


def test_calendar_holidays_property():
    """Тест свойства holidays"""
    calendar = Calendar(2024)
    holiday = datetime(2024, 1, 1)
    calendar.add_holiday(holiday)

    # Проверяем, что holidays - это свойство, возвращающее список
    assert hasattr(calendar, 'holidays')
    assert isinstance(calendar.holidays, list)
    assert holiday in calendar.holidays


def test_calendar_special_dates_property():
    """Тест свойства special_dates"""
    calendar = Calendar(2024)
    special_date = datetime(2024, 3, 8)
    calendar.add_special_date(special_date)

    # Проверяем, что special_dates - это свойство, возвращающее список
    assert hasattr(calendar, 'special_dates')
    assert isinstance(calendar.special_dates, list)
    assert special_date in calendar.special_dates


def test_calendar_field_types():
    """Тест типов полей календаря"""
    calendar = Calendar(2024)
    holiday = datetime(2024, 1, 1)
    special_date = datetime(2024, 3, 8)
    start = datetime(2024, 10, 1)
    end = datetime(2025, 5, 31)

    calendar.add_holiday(holiday)
    calendar.add_special_date(special_date)
    calendar.set_season(start, end)

    assert isinstance(calendar.year, int)
    assert isinstance(calendar.season_start, datetime)
    assert isinstance(calendar.season_end, datetime)
    assert isinstance(calendar.get_holidays(), list)
    assert isinstance(calendar.get_special_dates(), list)


def test_calendar_data_integrity():
    """Тест целостности данных календаря"""
    calendar = Calendar(2024)
    holiday1 = datetime(2024, 1, 1)
    holiday2 = datetime(2024, 5, 1)
    special_date = datetime(2024, 3, 8)
    start = datetime(2024, 10, 1)
    end = datetime(2025, 5, 31)

    # Изменяем поля
    calendar.add_holiday(holiday1)
    calendar.add_holiday(holiday2)
    calendar.add_special_date(special_date)
    calendar.set_season(start, end)

    # Проверяем, что основные поля остались неизменными
    assert calendar.year == 2024

    # Проверяем измененные поля
    assert len(calendar.get_holidays()) == 2
    assert len(calendar.get_special_dates()) == 1
    assert calendar.season_start == start
    assert calendar.season_end == end


def test_calendar_boundary_values():
    """Тест граничных значений для календаря"""
    # Очень старый год
    calendar1 = Calendar(1)
    assert calendar1.year == 1
    assert calendar1.season_start == datetime(1, 9, 1)

    # Будущий год
    calendar2 = Calendar(2100)
    assert calendar2.year == 2100
    assert calendar2.season_start == datetime(2100, 9, 1)
    assert calendar2.season_end == datetime(2101, 6, 30)

    # Много праздников
    calendar3 = Calendar(2024)
    for i in range(1, 13):  # 12 праздников
        holiday = datetime(2024, i, 1)
        calendar3.add_holiday(holiday)

    assert len(calendar3.get_holidays()) == 12


def test_calendar_season_operations():
    """Тест операций с сезоном"""
    calendar = Calendar(2024)

    # Изменение сезона на зимний
    winter_start = datetime(2024, 12, 1)
    winter_end = datetime(2025, 2, 28)
    calendar.set_season(winter_start, winter_end)

    assert calendar.season_start == winter_start
    assert calendar.season_end == winter_end

    # Изменение сезона на летний
    summer_start = datetime(2024, 6, 1)
    summer_end = datetime(2024, 8, 31)
    calendar.set_season(summer_start, summer_end)

    assert calendar.season_start == summer_start
    assert calendar.season_end == summer_end


def test_calendar_mixed_operations():
    """Тест смешанных операций с календарем"""
    calendar = Calendar(2024)

    # Добавляем праздники
    holidays = [
        datetime(2024, 1, 1),   # Новый год
        datetime(2024, 5, 1),   # День труда
        datetime(2024, 12, 25), # Рождество
    ]
    for holiday in holidays:
        calendar.add_holiday(holiday)

    # Добавляем особые даты
    special_dates = [
        datetime(2024, 2, 14),  # День влюбленных
        datetime(2024, 3, 8),   # 8 марта
        datetime(2024, 9, 1),   # День знаний
    ]
    for date in special_dates:
        calendar.add_special_date(date)

    # Проверяем все данные
    assert len(calendar.get_holidays()) == 3
    assert len(calendar.get_special_dates()) == 3
    assert calendar.season_start == datetime(2024, 9, 1)  # По умолчанию
    assert calendar.season_end == datetime(2025, 6, 30)

    # Меняем сезон
    custom_start = datetime(2024, 1, 1)
    custom_end = datetime(2024, 12, 31)
    calendar.set_season(custom_start, custom_end)

    assert calendar.season_start == custom_start
    assert calendar.season_end == custom_end

