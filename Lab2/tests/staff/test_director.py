"""Тесты для класса Director"""
import pytest
import sys
import os
from datetime import date
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from staff.director import Director


def test_director_creation_valid():
    """Тест создания режиссера с валидными данными"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    assert director.name == "Петр Петров"
    assert director.age == 45
    assert director.experience_years == 15
    assert director.salary == 80000.0
    assert director.is_available == True
    assert director.contract_end_date is None
    assert director.awards == []
    assert director.get_performances() == []


def test_director_creation_invalid_name():
    """Тест создания режиссера с невалидным именем"""
    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Director("", 45, 15, 80000.0)

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Director(None, 45, 15, 80000.0)

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Director(123, 45, 15, 80000.0)


def test_director_creation_invalid_age():
    """Тест создания режиссера с невалидным возрастом"""
    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Director("Петр Петров", -5, 15, 80000.0)

    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Director("Петр Петров", "45", 15, 80000.0)

    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Director("Петр Петров", 45.5, 15, 80000.0)


def test_director_creation_invalid_experience():
    """Тест создания режиссера с невалидным опытом"""
    with pytest.raises(ValueError, match="Опыт должен быть неотрицательным целым числом"):
        Director("Петр Петров", 45, -1, 80000.0)

    with pytest.raises(ValueError, match="Опыт должен быть неотрицательным целым числом"):
        Director("Петр Петров", 45, "15", 80000.0)


def test_director_creation_invalid_salary():
    """Тест создания режиссера с невалидной зарплатой"""
    with pytest.raises(ValueError, match="Зарплата должна быть неотрицательным числом"):
        Director("Петр Петров", 45, 15, -1000.0)

    with pytest.raises(ValueError, match="Зарплата должна быть неотрицательным числом"):
        Director("Петр Петров", 45, 15, "80000")

    # Проверяем конвертацию int в float
    director = Director("Петр Петров", 45, 15, 80000)  # int
    assert director.salary == 80000
    assert isinstance(director.salary, (int, float))


def test_director_creation_zero_values():
    """Тест создания режиссера с нулевыми значениями"""
    director = Director("Начинающий", 0, 0, 0.0)
    assert director.age == 0
    assert director.experience_years == 0
    assert director.salary == 0.0
    assert director.calculate_total_earnings(12) == 0.0


def test_director_add_performance_valid():
    """Тест добавления валидного спектакля"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_performance("Гамлет")
    assert "Гамлет" in director.get_performances()
    assert len(director.get_performances()) == 1


def test_director_add_performance_invalid():
    """Тест добавления невалидного спектакля"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    with pytest.raises(TypeError, match="Название спектакля должно быть строкой"):
        director.add_performance(123)

    with pytest.raises(TypeError, match="Название спектакля должно быть строкой"):
        director.add_performance(None)


def test_director_add_performance_duplicate():
    """Тест добавления дублированного спектакля"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_performance("Гамлет")
    director.add_performance("Гамлет")  # Дубликат

    performances = director.get_performances()
    assert performances.count("Гамлет") == 1  # Должен быть только один экземпляр
    assert len(performances) == 1


def test_director_remove_performance_existing():
    """Тест удаления существующего спектакля"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_performance("Гамлет")
    director.add_performance("Отелло")

    director.remove_performance("Гамлет")
    performances = director.get_performances()
    assert "Гамлет" not in performances
    assert "Отелло" in performances
    assert len(performances) == 1


def test_director_remove_performance_nonexistent():
    """Тест удаления несуществующего спектакля"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_performance("Гамлет")

    director.remove_performance("Отелло")  # Несуществующий спектакль
    performances = director.get_performances()
    assert "Гамлет" in performances  # Существующий спектакль должен остаться
    assert len(performances) == 1


def test_director_get_performances():
    """Тест получения списка спектаклей"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_performance("Гамлет")
    director.add_performance("Отелло")

    performances = director.get_performances()
    assert "Гамлет" in performances
    assert "Отелло" in performances
    assert len(performances) == 2

    # Проверяем, что возвращается копия, а не оригинал
    performances.append("Макбет")
    assert "Макбет" not in director.get_performances()  # Оригинал не должен измениться


def test_director_get_performances_empty():
    """Тест получения пустого списка спектаклей"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    performances = director.get_performances()
    assert performances == []
    assert len(performances) == 0


def test_director_add_award_valid():
    """Тест добавления валидной награды"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_award("Золотая маска")
    assert "Золотая маска" in director.awards
    assert len(director.awards) == 1


def test_director_add_award_invalid():
    """Тест добавления невалидной награды"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    with pytest.raises(TypeError, match="Награда должна быть строкой"):
        director.add_award(123)

    with pytest.raises(TypeError, match="Награда должна быть строкой"):
        director.add_award(None)


def test_director_add_award_duplicate():
    """Тест добавления дублированной награды"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_award("Золотая маска")
    director.add_award("Золотая маска")  # Дубликат

    assert director.awards.count("Золотая маска") == 1  # Должен быть только один экземпляр
    assert len(director.awards) == 1


def test_director_set_availability_valid():
    """Тест установки валидной доступности"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    director.set_availability(False)
    assert director.is_available == False

    director.set_availability(True)
    assert director.is_available == True


def test_director_set_availability_invalid():
    """Тест установки невалидной доступности"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    with pytest.raises(TypeError, match="Доступность должна быть булевым значением"):
        director.set_availability("true")

    with pytest.raises(TypeError, match="Доступность должна быть булевым значением"):
        director.set_availability(1)


def test_director_calculate_total_earnings_valid():
    """Тест расчета общего заработка с валидными данными"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    earnings = director.calculate_total_earnings(12)
    assert earnings == 960000.0

    earnings = director.calculate_total_earnings(1)
    assert earnings == 80000.0

    earnings = director.calculate_total_earnings(0)
    assert earnings == 0.0


def test_director_calculate_total_earnings_invalid():
    """Тест расчета общего заработка с невалидными данными"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    with pytest.raises(ValueError, match="Количество месяцев должно быть неотрицательным"):
        director.calculate_total_earnings(-1)

    with pytest.raises(ValueError, match="Количество месяцев должно быть неотрицательным"):
        director.calculate_total_earnings("12")


def test_director_calculate_total_earnings_zero_salary():
    """Тест расчета заработка с нулевой зарплатой"""
    director = Director("Бедный режиссер", 25, 2, 0.0)
    earnings = director.calculate_total_earnings(12)
    assert earnings == 0.0


def test_director_calculate_total_earnings_float_months():
    """Тест расчета заработка с дробным количеством месяцев"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    with pytest.raises(ValueError, match="Количество месяцев должно быть неотрицательным"):
        director.calculate_total_earnings(6.5)  # float не принимается


def test_director_direct_performance_valid():
    """Тест режиссирования валидного спектакля"""
    from unittest.mock import Mock
    director = Director("Петр Петров", 45, 15, 80000.0)

    # Создаем mock объект для Performance
    performance = Mock()
    performance.name = "Гамлет"
    performance.assign_director = Mock()

    director.direct_performance(performance)
    performance.assign_director.assert_called_once_with(director)
    assert "Гамлет" in director.get_performances()


def test_director_direct_performance_invalid():
    """Тест режиссирования невалидного спектакля"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    with pytest.raises(ValueError, match="Спектакль не может быть None"):
        director.direct_performance(None)


def test_director_direct_performance_unavailable():
    """Тест режиссирования спектакля недоступным режиссером"""
    from unittest.mock import Mock
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.set_availability(False)  # Режиссер недоступен

    performance = Mock()
    performance.name = "Гамлет"
    performance.assign_director = Mock()

    director.direct_performance(performance)
    performance.assign_director.assert_not_called()  # Метод не должен быть вызван
    assert "Гамлет" not in director.get_performances()


def test_director_conduct_rehearsal_valid():
    """Тест проведения валидной репетиции"""
    from unittest.mock import Mock
    director = Director("Петр Петров", 45, 15, 80000.0)

    # Создаем mock объект для Rehearsal
    rehearsal = Mock()
    rehearsal.title = "Репетиция Гамлета"

    # Метод conduct_rehearsal не должен выбрасывать исключение для валидной репетиции
    director.conduct_rehearsal(rehearsal)


def test_director_conduct_rehearsal_invalid():
    """Тест проведения невалидной репетиции"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    with pytest.raises(ValueError, match="Репетиция не может быть None"):
        director.conduct_rehearsal(None)


def test_director_conduct_rehearsal_unavailable():
    """Тест проведения репетиции недоступным режиссером"""
    from unittest.mock import Mock
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.set_availability(False)  # Режиссер недоступен

    rehearsal = Mock()
    rehearsal.title = "Репетиция Гамлета"

    with pytest.raises(ValueError, match="Режиссер недоступен для проведения репетиции"):
        director.conduct_rehearsal(rehearsal)


def test_director_manage_session_valid():
    """Тест управления валидным сеансом"""
    from unittest.mock import Mock
    director = Director("Петр Петров", 45, 15, 80000.0)

    # Создаем mock объект для Session
    session = Mock()
    session.id = "S001"

    # Метод manage_session не должен выбрасывать исключение для валидного сеанса
    director.manage_session(session)


def test_director_manage_session_invalid():
    """Тест управления невалидным сеансом"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    with pytest.raises(ValueError, match="Сеанс не может быть None"):
        director.manage_session(None)


def test_director_manage_session_unavailable():
    """Тест управления сеансом недоступным режиссером"""
    from unittest.mock import Mock
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.set_availability(False)  # Режиссер недоступен

    session = Mock()
    session.id = "S001"

    with pytest.raises(ValueError, match="Режиссер недоступен для управления сеансом"):
        director.manage_session(session)


def test_director_performances_property():
    """Тест свойства performances"""
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.add_performance("Гамлет")

    # Проверяем, что performances - это свойство, возвращающее список
    assert hasattr(director, 'performances')
    assert isinstance(director.performances, list)
    assert "Гамлет" in director.performances


def test_director_field_types():
    """Тест типов полей режиссера"""
    test_date = date(2025, 12, 31)
    director = Director("Петр Петров", 45, 15, 80000.0)
    director.contract_end_date = test_date
    director.add_award("Золотая маска")

    assert isinstance(director.name, str)
    assert isinstance(director.age, int)
    assert isinstance(director.experience_years, int)
    assert isinstance(director.salary, float)
    assert isinstance(director.is_available, bool)
    assert director.contract_end_date is None or isinstance(director.contract_end_date, date)
    assert isinstance(director.awards, list)
    assert isinstance(director.get_performances(), list)


def test_director_data_integrity():
    """Тест целостности данных режиссера"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    # Изменяем некоторые поля
    director.add_performance("Гамлет")
    director.add_performance("Отелло")
    director.add_award("Золотая маска")
    director.add_award("Государственная премия")
    director.set_availability(False)

    # Проверяем, что основные поля остались неизменными
    assert director.name == "Петр Петров"
    assert director.age == 45
    assert director.experience_years == 15
    assert director.salary == 80000.0

    # Проверяем измененные поля
    assert not director.is_available
    assert len(director.get_performances()) == 2
    assert len(director.awards) == 2


def test_director_boundary_values():
    """Тест граничных значений для режиссера"""
    # Максимально возможный возраст
    director1 = Director("Старый режиссер", 150, 70, 1000000.0)
    assert director1.age == 150

    # Нулевые значения
    director2 = Director("Начинающий", 0, 0, 0.0)
    assert director2.calculate_total_earnings(12) == 0.0

    # Очень большая зарплата
    director3 = Director("Звезда", 40, 20, 10000000.0)
    assert director3.calculate_total_earnings(1) == 10000000.0


def test_director_awards_management():
    """Тест управления наградами режиссера"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    # Добавляем награды
    awards_to_add = ["Золотая маска", "Государственная премия", "Театральная премия", "Международная награда"]
    for award in awards_to_add:
        director.add_award(award)

    assert len(director.awards) == 4
    for award in awards_to_add:
        assert award in director.awards


def test_director_performances_management():
    """Тест управления спектаклями режиссера"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    # Добавляем спектакли
    performances_to_add = ["Гамлет", "Отелло", "Король Лир", "Макбет", "Ромео и Джульетта"]
    for performance in performances_to_add:
        director.add_performance(performance)

    assert len(director.get_performances()) == 5
    for performance in performances_to_add:
        assert performance in director.get_performances()

    # Удаляем некоторые спектакли
    director.remove_performance("Отелло")
    director.remove_performance("Макбет")

    assert len(director.get_performances()) == 3
    assert "Гамлет" in director.get_performances()
    assert "Король Лир" in director.get_performances()
    assert "Ромео и Джульетта" in director.get_performances()
    assert "Отелло" not in director.get_performances()
    assert "Макбет" not in director.get_performances()


def test_director_associations():
    """Тест ассоциаций режиссера"""
    director = Director("Петр Петров", 45, 15, 80000.0)

    # Проверяем, что методы ассоциаций существуют и вызываются
    assert hasattr(director, 'direct_performance')
    assert hasattr(director, 'conduct_rehearsal')
    assert hasattr(director, 'manage_session')

    # Проверяем, что это callable методы
    assert callable(director.direct_performance)
    assert callable(director.conduct_rehearsal)
    assert callable(director.manage_session)

