"""Тесты для класса Costume"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from costumes.costume import Costume


def test_costume_creation_valid():
    """Тест создания костюма с валидными данными"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    assert costume.name == "Королевский наряд"
    assert costume.size == "M"
    assert costume.material == "Шелк"
    assert costume.condition == ""
    assert costume.is_available == True
    assert costume.actor_name is None
    assert costume.get_performances() == []


def test_costume_creation_invalid_name():
    """Тест создания костюма с невалидным названием"""
    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        Costume("", "M", "Шелк")

    with pytest.raises(ValueError, match="Название должно быть непустой строкой"):
        Costume(None, "M", "Шелк")


def test_costume_creation_invalid_size():
    """Тест создания костюма с невалидным размером"""
    with pytest.raises(ValueError, match="Размер должен быть непустой строкой"):
        Costume("Королевский наряд", "", "Шелк")

    with pytest.raises(ValueError, match="Размер должен быть непустой строкой"):
        Costume("Королевский наряд", None, "Шелк")


def test_costume_creation_invalid_material():
    """Тест создания костюма с невалидным материалом"""
    with pytest.raises(ValueError, match="Материал должен быть непустой строкой"):
        Costume("Королевский наряд", "M", "")

    with pytest.raises(ValueError, match="Материал должен быть непустой строкой"):
        Costume("Королевский наряд", "M", None)


def test_costume_add_performance_valid():
    """Тест добавления валидного спектакля"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.add_performance("Гамлет")
    assert "Гамлет" in costume.get_performances()
    assert len(costume.get_performances()) == 1


def test_costume_add_performance_invalid():
    """Тест добавления невалидного спектакля"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    with pytest.raises(TypeError, match="Название спектакля должно быть строкой"):
        costume.add_performance(123)

    with pytest.raises(TypeError, match="Название спектакля должно быть строкой"):
        costume.add_performance(None)


def test_costume_add_performance_duplicate():
    """Тест добавления дублированного спектакля"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.add_performance("Гамлет")
    costume.add_performance("Гамлет")  # Дубликат

    performances = costume.get_performances()
    assert performances.count("Гамлет") == 1  # Должен быть только один экземпляр
    assert len(performances) == 1


def test_costume_get_performances():
    """Тест получения списка спектаклей"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.add_performance("Гамлет")
    costume.add_performance("Отелло")

    performances = costume.get_performances()
    assert "Гамлет" in performances
    assert "Отелло" in performances
    assert len(performances) == 2

    # Проверяем, что возвращается копия, а не оригинал
    performances.append("Макбет")
    assert "Макбет" not in costume.get_performances()  # Оригинал не должен измениться


def test_costume_get_performances_empty():
    """Тест получения пустого списка спектаклей"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    performances = costume.get_performances()
    assert performances == []
    assert len(performances) == 0


def test_costume_set_condition_valid():
    """Тест установки валидного состояния"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.set_condition("Хорошее")
    assert costume.condition == "Хорошее"


def test_costume_set_condition_invalid():
    """Тест установки невалидного состояния"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    with pytest.raises(TypeError, match="Состояние должно быть строкой"):
        costume.set_condition(123)

    with pytest.raises(TypeError, match="Состояние должно быть строкой"):
        costume.set_condition(None)


def test_costume_assign_to_actor_valid():
    """Тест назначения валидного актера"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.assign_to_actor("Иван Иванов")

    assert costume.actor_name == "Иван Иванов"
    assert costume.is_available == False


def test_costume_assign_to_actor_invalid():
    """Тест назначения невалидного актера"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    with pytest.raises(TypeError, match="Имя актера должно быть строкой"):
        costume.assign_to_actor(123)

    with pytest.raises(TypeError, match="Имя актера должно быть строкой"):
        costume.assign_to_actor(None)


def test_costume_assign_to_actor_reassign():
    """Тест переназначения актера"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    costume.assign_to_actor("Иван Иванов")
    assert costume.actor_name == "Иван Иванов"
    assert not costume.is_available

    costume.assign_to_actor("Мария Петрова")
    assert costume.actor_name == "Мария Петрова"
    assert not costume.is_available


def test_costume_release():
    """Тест освобождения костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.assign_to_actor("Иван Иванов")

    assert costume.actor_name == "Иван Иванов"
    assert not costume.is_available

    costume.release()
    assert costume.actor_name is None
    assert costume.is_available == True


def test_costume_release_unused():
    """Тест освобождения неиспользуемого костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    # Освобождение неиспользуемого костюма
    costume.release()
    assert costume.actor_name is None
    assert costume.is_available == True


def test_costume_performances_property():
    """Тест свойства performances"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.add_performance("Гамлет")

    # Проверяем, что performances - это свойство, возвращающее список
    assert hasattr(costume, 'performances')
    assert isinstance(costume.performances, list)
    assert "Гамлет" in costume.performances


def test_costume_field_types():
    """Тест типов полей костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")
    costume.set_condition("Хорошее")
    costume.assign_to_actor("Иван Иванов")
    costume.add_performance("Гамлет")

    assert isinstance(costume.name, str)
    assert isinstance(costume.size, str)
    assert isinstance(costume.material, str)
    assert isinstance(costume.condition, str)
    assert isinstance(costume.is_available, bool)
    assert costume.actor_name is None or isinstance(costume.actor_name, str)
    assert isinstance(costume.get_performances(), list)


def test_costume_data_integrity():
    """Тест целостности данных костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    # Изменяем поля
    costume.add_performance("Гамлет")
    costume.add_performance("Отелло")
    costume.set_condition("Отличное")
    costume.assign_to_actor("Иван Иванов")

    # Проверяем, что основные поля остались неизменными
    assert costume.name == "Королевский наряд"
    assert costume.size == "M"
    assert costume.material == "Шелк"

    # Проверяем измененные поля
    assert len(costume.get_performances()) == 2
    assert costume.condition == "Отличное"
    assert costume.actor_name == "Иван Иванов"
    assert not costume.is_available


def test_costume_workflow():
    """Тест полного жизненного цикла костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    # Начальное состояние
    assert costume.is_available
    assert costume.actor_name is None
    assert len(costume.get_performances()) == 0

    # Добавление спектаклей
    costume.add_performance("Гамлет")
    costume.add_performance("Отелло")
    assert len(costume.get_performances()) == 2

    # Установка состояния
    costume.set_condition("Новое")
    assert costume.condition == "Новое"

    # Назначение актеру
    costume.assign_to_actor("Иван Иванов")
    assert not costume.is_available
    assert costume.actor_name == "Иван Иванов"

    # Освобождение
    costume.release()
    assert costume.is_available
    assert costume.actor_name is None

    # Повторное использование
    costume.assign_to_actor("Мария Петрова")
    assert not costume.is_available
    assert costume.actor_name == "Мария Петрова"


def test_costume_boundary_values():
    """Тест граничных значений для костюма"""
    # Однобуквенные значения
    costume1 = Costume("A", "S", "X")
    assert costume1.name == "A"
    assert costume1.size == "S"
    assert costume1.material == "X"

    # Длинные названия
    long_name = "Очень длинное название королевского костюма для главного героя"
    costume2 = Costume(long_name, "XL", "Дорогой шелк")
    assert costume2.name == long_name

    # Разные размеры
    sizes = ["XS", "S", "M", "L", "XL", "XXL", "42", "50"]
    for size in sizes:
        costume = Costume("Тест", size, "Ткань")
        assert costume.size == size


def test_costume_performances_management():
    """Тест управления спектаклями костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    # Добавляем спектакли
    performances_to_add = ["Гамлет", "Отелло", "Король Лир", "Макбет", "Ромео и Джульетта"]
    for performance in performances_to_add:
        costume.add_performance(performance)

    assert len(costume.get_performances()) == 5
    for performance in performances_to_add:
        assert performance in costume.get_performances()


def test_costume_condition_states():
    """Тест различных состояний костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    conditions = ["Новое", "Хорошее", "Удовлетворительное", "Требует ремонта", "Неисправное"]
    for condition in conditions:
        costume.set_condition(condition)
        assert costume.condition == condition


def test_costume_availability_transitions():
    """Тест переходов доступности костюма"""
    costume = Costume("Королевский наряд", "M", "Шелк")

    # Начальное состояние
    assert costume.is_available

    # Назначение актеру
    costume.assign_to_actor("Иван Иванов")
    assert not costume.is_available

    # Освобождение
    costume.release()
    assert costume.is_available

    # Повторное назначение
    costume.assign_to_actor("Мария Петрова")
    assert not costume.is_available

    # Освобождение снова
    costume.release()
    assert costume.is_available

