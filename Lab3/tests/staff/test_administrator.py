"""Тесты для Administrator"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from staff.administrator import Administrator


def test_administrator_creation_valid():
    """Тест создания администратора с валидными данными"""
    admin = Administrator("A001", "Admin User", "IT", "Full")
    assert admin.employee_id == "A001"
    assert admin.name == "Admin User"
    assert admin.department == "IT"
    assert admin.access_level == "Full"
    assert admin.system_access == True
    assert admin.get_networks() == []


def test_administrator_creation_invalid_employee_id():
    """Тест создания администратора с невалидным ID сотрудника"""
    with pytest.raises(ValueError, match="ID сотрудника должен быть непустой строкой"):
        Administrator("", "Admin User", "IT", "Full")

    with pytest.raises(ValueError, match="ID сотрудника должен быть непустой строкой"):
        Administrator(None, "Admin User", "IT", "Full")


def test_administrator_creation_invalid_name():
    """Тест создания администратора с невалидным именем"""
    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Administrator("A001", "", "IT", "Full")

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        Administrator("A001", None, "IT", "Full")


def test_administrator_creation_invalid_department():
    """Тест создания администратора с невалидным отделом"""
    with pytest.raises(TypeError, match="Отдел должен быть строкой"):
        Administrator("A001", "Admin User", 123, "Full")


def test_administrator_creation_invalid_access_level():
    """Тест создания администратора с невалидным уровнем доступа"""
    with pytest.raises(TypeError, match="Уровень доступа должен быть строкой"):
        Administrator("A001", "Admin User", "IT", 123)


def test_administrator_add_network_valid():
    """Тест добавления валидной сети"""
    admin = Administrator("A001", "Admin User", "IT", "Full")
    mock_network = type('MockNetwork', (), {'network_id': 'N001'})()
    admin.add_network(mock_network)
    assert len(admin.get_networks()) == 1


def test_administrator_add_network_invalid():
    """Тест добавления невалидной сети"""
    admin = Administrator("A001", "Admin User", "IT", "Full")

    with pytest.raises(ValueError, match="Сеть не может быть None"):
        admin.add_network(None)


def test_administrator_get_networks():
    """Тест получения списка управляемых сетей"""
    admin = Administrator("A001", "Admin User", "IT", "Full")
    mock_network1 = type('MockNetwork', (), {'network_id': 'N001'})()
    mock_network2 = type('MockNetwork', (), {'network_id': 'N002'})()

    admin.add_network(mock_network1)
    admin.add_network(mock_network2)

    networks = admin.get_networks()
    assert len(networks) == 2
    assert networks[0].network_id == 'N001'
    assert networks[1].network_id == 'N002'


def test_administrator_revoke_access():
    """Тест отзыва доступа"""
    admin = Administrator("A001", "Admin User", "IT", "Full")
    assert admin.system_access == True

    admin.revoke_access()
    assert admin.system_access == False


def test_administrator_grant_access():
    """Тест предоставления доступа"""
    admin = Administrator("A001", "Admin User", "IT", "Full")
    admin.revoke_access()
    assert admin.system_access == False

    admin.grant_access()
    assert admin.system_access == True


def test_administrator_field_types():
    """Тест типов полей администратора"""
    admin = Administrator("A001", "Admin User", "IT", "Full")
    mock_network = type('MockNetwork', (), {'network_id': 'N001'})()
    admin.add_network(mock_network)

    assert isinstance(admin.employee_id, str)
    assert isinstance(admin.name, str)
    assert isinstance(admin.department, str)
    assert isinstance(admin.access_level, str)
    assert isinstance(admin.system_access, bool)
    assert isinstance(admin.get_networks(), list)


def test_administrator_data_integrity():
    """Тест целостности данных администратора"""
    admin = Administrator("A001", "Admin User", "IT", "Full")

    # Изменяем поля
    mock_network = type('MockNetwork', (), {'network_id': 'N001'})()
    admin.add_network(mock_network)
    admin.revoke_access()

    # Проверяем, что основные поля остались неизменными
    assert admin.employee_id == "A001"
    assert admin.name == "Admin User"
    assert admin.department == "IT"
    assert admin.access_level == "Full"

    # Проверяем измененные поля
    assert len(admin.get_networks()) == 1
    assert admin.system_access == False


def test_administrator_access_levels():
    """Тест различных уровней доступа"""
    access_levels = ["Read", "Write", "Admin", "Full", "Super", "Root"]

    for level in access_levels:
        admin = Administrator("TEST", "Test Admin", "Security", level)
        assert admin.access_level == level


def test_administrator_departments():
    """Тест различных отделов"""
    departments = ["IT", "HR", "Finance", "Operations", "Security", "Maintenance"]

    for dept in departments:
        admin = Administrator("TEST", "Test Admin", dept, "Full")
        assert admin.department == dept


def test_administrator_multiple_networks():
    """Тест управления множественными сетями"""
    admin = Administrator("A001", "Network Admin", "IT", "Full")

    # Добавляем несколько сетей
    networks = []
    for i in range(5):
        mock_network = type('MockNetwork', (), {'network_id': f'N{i+1:03d}'})()
        networks.append(mock_network)
        admin.add_network(mock_network)

    managed_networks = admin.get_networks()
    assert len(managed_networks) == 5
    for i, network in enumerate(managed_networks):
        assert network.network_id == f'N{i+1:03d}'


def test_administrator_workflow():
    """Тест полного жизненного цикла администратора"""
    # Создание администратора
    admin = Administrator("ADMIN001", "John System", "IT Security", "Super")

    # Добавление сетей
    mock_network1 = type('MockNetwork', (), {'network_id': 'NET001'})()
    mock_network2 = type('MockNetwork', (), {'network_id': 'NET002'})()
    admin.add_network(mock_network1)
    admin.add_network(mock_network2)

    # Управление доступом
    admin.revoke_access()
    assert not admin.system_access

    admin.grant_access()
    assert admin.system_access

    # Проверки
    assert admin.employee_id == "ADMIN001"
    assert admin.name == "John System"
    assert admin.department == "IT Security"
    assert admin.access_level == "Super"
    assert len(admin.get_networks()) == 2
    assert admin.system_access == True


def test_administrator_security_scenarios():
    """Тест сценариев безопасности"""
    # Администратор с полным доступом
    full_admin = Administrator("FULL001", "Full Admin", "Security", "Full")

    # Администратор с ограниченным доступом
    limited_admin = Administrator("LIMIT001", "Limited Admin", "Operations", "Read")

    # Проверки доступа
    assert full_admin.access_level == "Full"
    assert limited_admin.access_level == "Read"

    # Отзыв доступа
    full_admin.revoke_access()
    assert not full_admin.system_access


def test_administrator_error_handling():
    """Тест обработки ошибок"""
    admin = Administrator("TEST", "Test Admin", "Test", "Full")

    # Попытка добавления None сети
    with pytest.raises(ValueError):
        admin.add_network(None)

    # Попытка создания с неправильными типами
    with pytest.raises(ValueError):
        Administrator("", "Test", "Test", "Full")

    with pytest.raises(ValueError):
        Administrator("TEST", "", "Test", "Full")

    with pytest.raises(TypeError):
        Administrator("TEST", "Test", 123, "Full")

    with pytest.raises(TypeError):
        Administrator("TEST", "Test", "Test", 123)


def test_administrator_state_transitions():
    """Тест переходов состояний"""
    admin = Administrator("STATE", "State Admin", "State", "Full")

    # Начальное состояние
    assert admin.system_access == True
    assert len(admin.get_networks()) == 0

    # Добавление сети
    mock_network = type('MockNetwork', (), {'network_id': 'STATE001'})()
    admin.add_network(mock_network)
    assert len(admin.get_networks()) == 1

    # Отзыв доступа
    admin.revoke_access()
    assert admin.system_access == False

    # Предоставление доступа
    admin.grant_access()
    assert admin.system_access == True


