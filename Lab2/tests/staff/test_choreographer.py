"""Тесты для класса Choreographer"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from staff.choreographer import Choreographer


def test_choreographer_creation_valid():
    """Тест создания хореографа с валидными данными"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)
    assert choreographer.name == "Елена Соколова"
    assert choreographer.age == 38
    assert choreographer.experience_years == 12
    assert choreographer.salary == 65000.0
    assert choreographer.is_available == True
    assert choreographer.dance_style == ""
    assert choreographer.get_choreographies() == []


def test_choreographer_creation_invalid_name():
    """Тест создания хореографа с невалидным именем"""
    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Choreographer("", 38, 12, 65000.0)

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Choreographer(None, 38, 12, 65000.0)


def test_choreographer_creation_invalid_age():
    """Тест создания хореографа с невалидным возрастом"""
    with pytest.raises(ValueError, match="Возраст должен быть неотрицательным целым числом"):
        Choreographer("Елена Соколова", -5, 12, 65000.0)


def test_choreographer_creation_invalid_experience():
    """Тест создания хореографа с невалидным опытом"""
    with pytest.raises(ValueError, match="Опыт должен быть неотрицательным целым числом"):
        Choreographer("Елена Соколова", 38, -1, 65000.0)


def test_choreographer_creation_invalid_salary():
    """Тест создания хореографа с невалидной зарплатой"""
    with pytest.raises(ValueError, match="Зарплата должна быть неотрицательным числом"):
        Choreographer("Елена Соколова", 38, 12, -1000.0)


def test_choreographer_add_choreography_valid():
    """Тест добавления валидной хореографии"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)
    choreographer.add_choreography("Лебединое озеро")
    assert "Лебединое озеро" in choreographer.get_choreographies()
    assert len(choreographer.get_choreographies()) == 1


def test_choreographer_add_choreography_invalid():
    """Тест добавления невалидной хореографии"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)

    with pytest.raises(TypeError, match="Название хореографии должно быть строкой"):
        choreographer.add_choreography(123)


def test_choreographer_add_choreography_duplicate():
    """Тест добавления дублированной хореографии"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)
    choreographer.add_choreography("Лебединое озеро")
    choreographer.add_choreography("Лебединое озеро")  # Дубликат

    choreographies = choreographer.get_choreographies()
    assert choreographies.count("Лебединое озеро") == 1
    assert len(choreographies) == 1


def test_choreographer_get_choreographies():
    """Тест получения списка хореографий"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)
    choreographer.add_choreography("Лебединое озеро")
    choreographer.add_choreography("Щелкунчик")

    choreographies = choreographer.get_choreographies()
    assert "Лебединое озеро" in choreographies
    assert "Щелкунчик" in choreographies
    assert len(choreographies) == 2


def test_choreographer_set_dance_style_valid():
    """Тест установки валидного стиля танца"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)
    choreographer.set_dance_style("балет")
    assert choreographer.dance_style == "балет"


def test_choreographer_set_dance_style_invalid():
    """Тест установки невалидного стиля танца"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)

    with pytest.raises(TypeError, match="Стиль должен быть строкой"):
        choreographer.set_dance_style(123)


def test_choreographer_calculate_monthly_earnings():
    """Тест расчета месячного заработка"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)
    earnings = choreographer.calculate_monthly_earnings()
    assert earnings == 65000.0


def test_choreographer_field_types():
    """Тест типов полей хореографа"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)
    choreographer.add_choreography("Лебединое озеро")
    choreographer.set_dance_style("балет")

    assert isinstance(choreographer.name, str)
    assert isinstance(choreographer.age, int)
    assert isinstance(choreographer.experience_years, int)
    assert isinstance(choreographer.salary, float)
    assert isinstance(choreographer.is_available, bool)
    assert isinstance(choreographer.dance_style, str)
    assert isinstance(choreographer.get_choreographies(), list)


def test_choreographer_data_integrity():
    """Тест целостности данных хореографа"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)

    # Изменяем поля
    choreographer.add_choreography("Лебединое озеро")
    choreographer.add_choreography("Щелкунчик")
    choreographer.set_dance_style("балет")
    choreographer.is_available = False

    # Проверяем, что основные поля остались неизменными
    assert choreographer.name == "Елена Соколова"
    assert choreographer.age == 38
    assert choreographer.experience_years == 12
    assert choreographer.salary == 65000.0

    # Проверяем измененные поля
    assert len(choreographer.get_choreographies()) == 2
    assert choreographer.dance_style == "балет"
    assert not choreographer.is_available


def test_choreographer_boundary_values():
    """Тест граничных значений для хореографа"""
    # Нулевой возраст и опыт
    choreographer1 = Choreographer("Молодой хореограф", 0, 0, 0.0)
    assert choreographer1.age == 0
    assert choreographer1.experience_years == 0
    assert choreographer1.salary == 0.0

    # Большой опыт
    choreographer2 = Choreographer("Опытный хореограф", 70, 50, 150000.0)
    assert choreographer2.experience_years == 50


def test_choreographer_dance_styles():
    """Тест различных стилей танца"""
    dance_styles = ["балет", "современный", "джаз", "хип-хоп", "народный", "бальный"]

    for style in dance_styles:
        choreographer = Choreographer("Тест", 30, 10, 50000.0)
        choreographer.set_dance_style(style)
        assert choreographer.dance_style == style


def test_choreographer_multiple_choreographies():
    """Тест множественных хореографий"""
    choreographer = Choreographer("Елена Соколова", 38, 12, 65000.0)

    choreographies = [
        "Лебединое озеро",
        "Щелкунчик",
        "Спящая красавица",
        "Дон Кихот",
        "Жизель"
    ]

    for choreography in choreographies:
        choreographer.add_choreography(choreography)

    assert len(choreographer.get_choreographies()) == 5
    for choreography in choreographies:
        assert choreography in choreographer.get_choreographies()


def test_choreographer_workflow():
    """Тест полного жизненного цикла хореографа"""
    # Создание хореографа
    choreographer = Choreographer("Мария Петрова", 35, 15, 70000.0)

    # Добавление хореографий
    choreographer.add_choreography("Ромео и Джульетта")
    choreographer.add_choreography("Кармен")

    # Установка стиля
    choreographer.set_dance_style("классический балет")

    # Расчет заработка
    earnings = choreographer.calculate_monthly_earnings()

    # Проверки
    assert choreographer.name == "Мария Петрова"
    assert choreographer.age == 35
    assert len(choreographer.get_choreographies()) == 2
    assert choreographer.dance_style == "классический балет"
    assert earnings == 70000.0
    assert choreographer.is_available == True


def test_choreographer_experience_levels():
    """Тест различных уровней опыта хореографов"""
    # Начинающий хореограф
    junior = Choreographer("Начинающий", 25, 3, 40000.0)

    # Средний уровень
    mid = Choreographer("Средний", 40, 15, 65000.0)

    # Мастер
    master = Choreographer("Мастер", 55, 30, 90000.0)

    # Проверки
    assert junior.experience_years == 3
    assert mid.experience_years == 15
    assert master.experience_years == 30

    assert junior.calculate_monthly_earnings() == 40000.0
    assert mid.calculate_monthly_earnings() == 65000.0
    assert master.calculate_monthly_earnings() == 90000.0


def test_choreographer_seasonal_work():
    """Тест сезонной работы хореографа"""
    choreographer = Choreographer("Сезонный хореограф", 42, 18, 55000.0)

    # Зимний сезон (балет)
    choreographer.set_dance_style("балет")
    choreographer.add_choreography("Щелкунчик")
    choreographer.add_choreography("Лебединое озеро")

    # Летний сезон (современные танцы)
    choreographer.set_dance_style("современный")
    choreographer.add_choreography("Летние мотивы")
    choreographer.add_choreography("Пляжные ритмы")

    assert choreographer.dance_style == "современный"  # Последняя установка
    assert len(choreographer.get_choreographies()) == 4


def test_choreographer_error_handling():
    """Тест обработки ошибок"""
    choreographer = Choreographer("Тестовый хореограф", 30, 10, 50000.0)

    # Попытка добавления неправильного типа хореографии
    with pytest.raises(TypeError):
        choreographer.add_choreography(12345)

    # Попытка установки неправильного типа стиля
    with pytest.raises(TypeError):
        choreographer.set_dance_style(67890)


def test_choreographer_state_consistency():
    """Тест согласованности состояний"""
    choreographer = Choreographer("Согласованный хореограф", 40, 20, 60000.0)

    # Начальное состояние
    assert choreographer.is_available == True
    assert choreographer.dance_style == ""
    assert len(choreographer.get_choreographies()) == 0

    # После добавления хореографий
    choreographer.add_choreography("Тестовая хореография")
    assert len(choreographer.get_choreographies()) == 1

    # После установки стиля
    choreographer.set_dance_style("тестовый стиль")
    assert choreographer.dance_style == "тестовый стиль"

    # После изменения доступности
    choreographer.is_available = False
    assert not choreographer.is_available

