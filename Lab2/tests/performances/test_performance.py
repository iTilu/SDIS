"""Тесты для класса Performance"""
import pytest
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from performances.performance import Performance


def test_performance_creation_valid():
    """Тест создания спектакля с валидными данными"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    assert perf.name == "Гамлет"
    assert perf.duration_minutes == 180
    assert perf.genre == "Драма"
    assert perf.ticket_price == 1500.0
    assert perf.is_active == True
    assert perf.total_shows == 0
    assert perf.premiere_date is None
    assert perf.get_actors() == []


def test_performance_creation_invalid_name():
    """Тест создания спектакля с невалидным названием"""
    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        Performance("", 180, "Драма", 1500.0)

    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        Performance(None, 180, "Драма", 1500.0)


def test_performance_creation_invalid_duration():
    """Тест создания спектакля с невалидной длительностью"""
    with pytest.raises(ValueError, match="Длительность должна быть положительным целым числом"):
        Performance("Гамлет", 0, "Драма", 1500.0)

    with pytest.raises(ValueError, match="Длительность должна быть положительным целым числом"):
        Performance("Гамлет", -60, "Драма", 1500.0)

    with pytest.raises(ValueError, match="Длительность должна быть положительным целым числом"):
        Performance("Гамлет", "180", "Драма", 1500.0)


def test_performance_creation_invalid_genre():
    """Тест создания спектакля с невалидным жанром"""
    with pytest.raises(ValueError, match="Жанр должен быть непустой строкой"):
        Performance("Гамлет", 180, "", 1500.0)

    with pytest.raises(ValueError, match="Жанр должен быть непустой строкой"):
        Performance("Гамлет", 180, None, 1500.0)


def test_performance_add_actor_valid():
    """Тест добавления валидного актера"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.add_actor("Иван Иванов")
    assert "Иван Иванов" in perf.get_actors()
    assert len(perf.get_actors()) == 1


def test_performance_add_actor_invalid():
    """Тест добавления невалидного актера"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    with pytest.raises(TypeError, match="Имя актера должно быть строкой"):
        perf.add_actor(123)

    with pytest.raises(TypeError, match="Имя актера должно быть строкой"):
        perf.add_actor(None)


def test_performance_add_duplicate_actor():
    """Тест добавления дублированного актера"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.add_actor("Иван Иванов")
    perf.add_actor("Иван Иванов")  # Дубликат

    actors = perf.get_actors()
    assert actors.count("Иван Иванов") == 1  # Должен быть только один экземпляр
    assert len(actors) == 1


def test_performance_remove_actor_existing():
    """Тест удаления существующего актера"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.add_actor("Иван Иванов")
    perf.add_actor("Мария Петрова")

    perf.remove_actor("Иван Иванов")
    actors = perf.get_actors()
    assert "Иван Иванов" not in actors
    assert "Мария Петрова" in actors
    assert len(actors) == 1


def test_performance_remove_actor_nonexistent():
    """Тест удаления несуществующего актера"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.add_actor("Иван Иванов")

    perf.remove_actor("Мария Петрова")  # Несуществующий актер
    actors = perf.get_actors()
    assert "Иван Иванов" in actors  # Существующий актер должен остаться
    assert len(actors) == 1


def test_performance_get_actors():
    """Тест получения списка актеров"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.add_actor("Иван Иванов")
    perf.add_actor("Мария Петрова")

    actors = perf.get_actors()
    assert "Иван Иванов" in actors
    assert "Мария Петрова" in actors
    assert len(actors) == 2

    # Проверяем, что возвращается копия, а не оригинал
    actors.append("Новый актер")
    assert "Новый актер" not in perf.get_actors()  # Оригинал не должен измениться


def test_performance_get_actors_empty():
    """Тест получения пустого списка актеров"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    actors = perf.get_actors()
    assert actors == []
    assert len(actors) == 0


def test_performance_set_premiere_date_valid():
    """Тест установки валидной даты премьеры"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    date = datetime(2024, 1, 15, 19, 30)
    perf.set_premiere_date(date)
    assert perf.premiere_date == date


def test_performance_set_premiere_date_invalid():
    """Тест установки невалидной даты премьеры"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    with pytest.raises(TypeError, match="Дата должна быть объектом datetime"):
        perf.set_premiere_date("2024-01-15")

    with pytest.raises(TypeError, match="Дата должна быть объектом datetime"):
        perf.set_premiere_date(None)


def test_performance_increment_shows():
    """Тест увеличения счетчика показов"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    assert perf.total_shows == 0

    perf.increment_shows()
    assert perf.total_shows == 1

    perf.increment_shows()
    assert perf.total_shows == 2


def test_performance_set_active_valid():
    """Тест установки валидной активности"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    perf.set_active(False)
    assert perf.is_active == False

    perf.set_active(True)
    assert perf.is_active == True


def test_performance_set_active_invalid():
    """Тест установки невалидной активности"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    with pytest.raises(TypeError, match="Активность должна быть булевым значением"):
        perf.set_active("true")

    with pytest.raises(TypeError, match="Активность должна быть булевым значением"):
        perf.set_active(1)


def test_performance_assign_actor_valid():
    """Тест назначения валидного актера"""
    from unittest.mock import Mock
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    # Создаем mock объект для Actor
    actor = Mock()
    actor.name = "Иван Иванов"

    perf.assign_actor(actor)
    assert "Иван Иванов" in perf.get_actors()


def test_performance_assign_actor_invalid():
    """Тест назначения невалидного актера"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    with pytest.raises(AttributeError):
        perf.assign_actor(None)  # None не имеет атрибута name


def test_performance_assign_director_valid():
    """Тест назначения валидного режиссера"""
    from unittest.mock import Mock
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    # Создаем mock объект для Director
    director = Mock()
    director.name = "Петр Сидоров"
    director.is_available = True
    director.get_performances.return_value = []
    director.add_performance = Mock()

    perf.assign_director(director)
    director.add_performance.assert_called_once_with("Гамлет")


def test_performance_assign_director_invalid():
    """Тест назначения невалидного режиссера"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    with pytest.raises(ValueError, match="Режиссер не может быть None"):
        perf.assign_director(None)


def test_performance_assign_director_unavailable():
    """Тест назначения недоступного режиссера"""
    from unittest.mock import Mock
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    # Создаем mock объект для Director
    director = Mock()
    director.name = "Петр Сидоров"
    director.is_available = False

    with pytest.raises(ValueError, match="Режиссер недоступен"):
        perf.assign_director(director)


def test_performance_set_ticket_price():
    """Тест установки цены билета"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.ticket_price = 2000.0  # Прямое присваивание для тестирования
    assert perf.ticket_price == 2000.0


def test_performance_field_types():
    """Тест типов полей спектакля"""
    test_date = datetime(2024, 1, 15, 19, 30)
    perf = Performance("Гамлет", 180, "Драма", 1500.0)
    perf.set_premiere_date(test_date)
    perf.add_actor("Иван Иванов")

    assert isinstance(perf.name, str)
    assert isinstance(perf.duration_minutes, int)
    assert isinstance(perf.genre, str)
    assert isinstance(perf.ticket_price, float)
    assert isinstance(perf.is_active, bool)
    assert isinstance(perf.total_shows, int)
    assert isinstance(perf.premiere_date, datetime) or perf.premiere_date is None
    assert isinstance(perf.get_actors(), list)


def test_performance_data_integrity():
    """Тест целостности данных спектакля"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    # Изменяем некоторые поля
    perf.add_actor("Иван Иванов")
    perf.add_actor("Мария Петрова")
    perf.set_premiere_date(datetime(2024, 1, 15))
    perf.increment_shows()
    perf.set_active(False)

    # Проверяем, что основные поля остались неизменными
    assert perf.name == "Гамлет"
    assert perf.duration_minutes == 180
    assert perf.genre == "Драма"
    assert perf.ticket_price == 1500.0

    # Проверяем измененные поля
    assert not perf.is_active
    assert perf.total_shows == 1
    assert perf.premiere_date == datetime(2024, 1, 15)
    assert len(perf.get_actors()) == 2


def test_performance_boundary_values():
    """Тест граничных значений для спектакля"""
    # Минимальная длительность
    perf1 = Performance("Короткий спектакль", 1, "Эксперимент", 0.0)
    assert perf1.duration_minutes == 1
    assert perf1.ticket_price == 0.0

    # Большая длительность и цена
    perf2 = Performance("Длинный спектакль", 1000, "Эпопея", 1000000.0)
    assert perf2.duration_minutes == 1000
    assert perf2.ticket_price == 1000000.0


def test_performance_actors_management():
    """Тест управления актерами"""
    perf = Performance("Гамлет", 180, "Драма", 1500.0)

    # Добавляем актеров
    actors_to_add = ["Гамлет", "Гертруда", "Клавдий", "Офелия"]
    for actor in actors_to_add:
        perf.add_actor(actor)

    assert len(perf.get_actors()) == 4
    for actor in actors_to_add:
        assert actor in perf.get_actors()

    # Удаляем некоторых актеров
    perf.remove_actor("Клавдий")
    perf.remove_actor("Офелия")

    assert len(perf.get_actors()) == 2
    assert "Гамлет" in perf.get_actors()
    assert "Гертруда" in perf.get_actors()
    assert "Клавдий" not in perf.get_actors()
    assert "Офелия" not in perf.get_actors()


def test_performance_zero_price():
    """Тест спектакля с нулевой ценой билета"""
    perf = Performance("Бесплатный спектакль", 120, "Эксперимент", 0.0)
    assert perf.ticket_price == 0.0


def test_performance_very_long_duration():
    """Тест спектакля с очень большой длительностью"""
    perf = Performance("Марафон", 1440, "Марафон", 500.0)  # 24 часа
    assert perf.duration_minutes == 1440

