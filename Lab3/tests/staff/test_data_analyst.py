"""Тесты для DataAnalyst"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from staff.data_analyst import DataAnalyst


def test_data_analyst_creation_valid():
    """Тест создания аналитика данных с валидными данными"""
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", ["Python", "R"])
    assert analyst.employee_id == "DA001"
    assert analyst.name == "Bob Johnson"
    assert analyst.specialization == "Statistics"
    assert analyst.tools == ["Python", "R"]
    assert analyst.reports_generated == 0
    assert analyst.department == "data_science"
    assert analyst.get_analyzed_data() == []


def test_data_analyst_creation_invalid_employee_id():
    """Тест создания аналитика с невалидным ID сотрудника"""
    with pytest.raises(ValueError, match="ID сотрудника должен быть непустой строкой"):
        DataAnalyst("", "Bob Johnson", "Statistics", ["Python"])

    with pytest.raises(ValueError, match="ID сотрудника должен быть непустой строкой"):
        DataAnalyst(None, "Bob Johnson", "Statistics", ["Python"])


def test_data_analyst_creation_invalid_name():
    """Тест создания аналитика с невалидным именем"""
    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        DataAnalyst("DA001", "", "Statistics", ["Python"])

    with pytest.raises(ValueError, match="Имя должно быть непустой строкой"):
        DataAnalyst("DA001", None, "Statistics", ["Python"])


def test_data_analyst_creation_invalid_specialization():
    """Тест создания аналитика с невалидной специализацией"""
    with pytest.raises(TypeError, match="Специализация должна быть строкой"):
        DataAnalyst("DA001", "Bob Johnson", 123, ["Python"])


def test_data_analyst_creation_invalid_tools():
    """Тест создания аналитика с невалидными инструментами"""
    with pytest.raises(TypeError, match="Инструменты должны быть списком"):
        DataAnalyst("DA001", "Bob Johnson", "Statistics", "Python")


def test_data_analyst_add_analyzed_data_valid():
    """Тест добавления валидных проанализированных данных"""
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", ["Python", "R"])
    mock_data = type('MockWeatherData', (), {'data_id': 'WD001'})()
    analyst.add_analyzed_data(mock_data)
    assert len(analyst.get_analyzed_data()) == 1


def test_data_analyst_add_analyzed_data_invalid():
    """Тест добавления невалидных данных"""
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", ["Python", "R"])

    with pytest.raises(ValueError, match="Данные не могут быть None"):
        analyst.add_analyzed_data(None)


def test_data_analyst_get_analyzed_data():
    """Тест получения списка проанализированных данных"""
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", ["Python", "R"])
    mock_data1 = type('MockWeatherData', (), {'data_id': 'WD001'})()
    mock_data2 = type('MockWeatherData', (), {'data_id': 'WD002'})()

    analyst.add_analyzed_data(mock_data1)
    analyst.add_analyzed_data(mock_data2)

    data = analyst.get_analyzed_data()
    assert len(data) == 2
    assert data[0].data_id == 'WD001'
    assert data[1].data_id == 'WD002'


def test_data_analyst_generate_report():
    """Тест генерации отчета"""
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", ["Python", "R"])
    initial_reports = analyst.reports_generated

    analyst.generate_report()
    assert analyst.reports_generated == initial_reports + 1


def test_data_analyst_get_tools():
    """Тест получения списка инструментов"""
    tools = ["Python", "R", "SQL", "Tableau"]
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", tools)

    retrieved_tools = analyst.get_tools()
    assert retrieved_tools == tools
    assert len(retrieved_tools) == 4


def test_data_analyst_field_types():
    """Тест типов полей аналитика данных"""
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", ["Python", "R"])
    mock_data = type('MockWeatherData', (), {'data_id': 'WD001'})()
    analyst.add_analyzed_data(mock_data)
    analyst.generate_report()

    assert isinstance(analyst.employee_id, str)
    assert isinstance(analyst.name, str)
    assert isinstance(analyst.specialization, str)
    assert isinstance(analyst.tools, list)
    assert isinstance(analyst.reports_generated, int)
    assert isinstance(analyst.department, str)
    assert isinstance(analyst.get_analyzed_data(), list)


def test_data_analyst_data_integrity():
    """Тест целостности данных аналитика"""
    analyst = DataAnalyst("DA001", "Bob Johnson", "Statistics", ["Python", "R"])

    # Изменяем поля
    mock_data1 = type('MockWeatherData', (), {'data_id': 'WD001'})()
    mock_data2 = type('MockWeatherData', (), {'data_id': 'WD002'})()
    analyst.add_analyzed_data(mock_data1)
    analyst.add_analyzed_data(mock_data2)
    analyst.generate_report()
    analyst.generate_report()

    # Проверяем, что основные поля остались неизменными
    assert analyst.employee_id == "DA001"
    assert analyst.name == "Bob Johnson"
    assert analyst.specialization == "Statistics"
    assert analyst.tools == ["Python", "R"]

    # Проверяем измененные поля
    assert len(analyst.get_analyzed_data()) == 2
    assert analyst.reports_generated == 2


def test_data_analyst_specializations():
    """Тест различных специализаций аналитиков"""
    specializations = [
        "Statistics",
        "Machine Learning",
        "Data Visualization",
        "Big Data",
        "Predictive Analytics",
        "Time Series Analysis"
    ]

    for spec in specializations:
        analyst = DataAnalyst("TEST", "Test Analyst", spec, ["Python"])
        assert analyst.specialization == spec


def test_data_analyst_tools():
    """Тест различных инструментов аналитика"""
    tools_combinations = [
        ["Python", "R"],
        ["Python", "SQL", "Tableau"],
        ["R", "SAS", "SPSS"],
        ["Python", "Java", "Scala", "Hadoop"],
        ["Excel", "Power BI", "Qlik"]
    ]

    for tools in tools_combinations:
        analyst = DataAnalyst("TEST", "Test Analyst", "Statistics", tools)
        assert analyst.get_tools() == tools
        assert len(analyst.get_tools()) == len(tools)


def test_data_analyst_multiple_data_analysis():
    """Тест анализа множественных данных"""
    analyst = DataAnalyst("DA001", "Data Analyst", "Statistics", ["Python", "R"])

    # Добавляем несколько наборов данных
    for i in range(10):
        mock_data = type('MockWeatherData', (), {'data_id': f'WD{i+1:03d}'})()
        analyst.add_analyzed_data(mock_data)

    # Генерируем несколько отчетов
    for _ in range(5):
        analyst.generate_report()

    assert len(analyst.get_analyzed_data()) == 10
    assert analyst.reports_generated == 5


def test_data_analyst_workflow():
    """Тест полного жизненного цикла аналитика данных"""
    # Создание аналитика
    analyst = DataAnalyst("ANALYST001", "Alice Smith", "Machine Learning", ["Python", "TensorFlow", "PyTorch"])

    # Анализ данных
    mock_data1 = type('MockWeatherData', (), {'data_id': 'TEMP001'})()
    mock_data2 = type('MockWeatherData', (), {'data_id': 'HUM001'})()
    analyst.add_analyzed_data(mock_data1)
    analyst.add_analyzed_data(mock_data2)

    # Генерация отчетов
    analyst.generate_report()
    analyst.generate_report()
    analyst.generate_report()

    # Проверки
    assert analyst.employee_id == "ANALYST001"
    assert analyst.name == "Alice Smith"
    assert analyst.specialization == "Machine Learning"
    assert len(analyst.get_tools()) == 3
    assert len(analyst.get_analyzed_data()) == 2
    assert analyst.reports_generated == 3
    assert analyst.department == "data_science"


def test_data_analyst_productivity_metrics():
    """Тест метрик продуктивности аналитика"""
    analyst = DataAnalyst("PROD001", "Productive Analyst", "Statistics", ["Python", "R"])

    # Симуляция работы
    for i in range(20):  # 20 наборов данных
        mock_data = type('MockWeatherData', (), {'data_id': f'DATA{i+1:03d}'})()
        analyst.add_analyzed_data(mock_data)

    for i in range(15):  # 15 отчетов
        analyst.generate_report()

    # Проверки продуктивности
    assert len(analyst.get_analyzed_data()) == 20
    assert analyst.reports_generated == 15


def test_data_analyst_error_handling():
    """Тест обработки ошибок"""
    analyst = DataAnalyst("TEST", "Test Analyst", "Test", ["Python"])

    # Попытка добавления None данных
    with pytest.raises(ValueError):
        analyst.add_analyzed_data(None)

    # Попытка создания с неправильными типами
    with pytest.raises(ValueError):
        DataAnalyst("", "Test", "Test", ["Python"])

    with pytest.raises(ValueError):
        DataAnalyst("TEST", "", "Test", ["Python"])

    with pytest.raises(TypeError):
        DataAnalyst("TEST", "Test", 123, ["Python"])

    with pytest.raises(TypeError):
        DataAnalyst("TEST", "Test", "Test", "Python")


def test_data_analyst_departments():
    """Тест различных отделов"""
    analyst = DataAnalyst("DEPT001", "Dept Analyst", "Statistics", ["Python"])
    assert analyst.department == "data_science"  # Проверяем значение по умолчанию


def test_data_analyst_state_consistency():
    """Тест согласованности состояний"""
    analyst = DataAnalyst("STATE", "State Analyst", "Statistics", ["Python", "R"])

    # Начальное состояние
    assert len(analyst.get_analyzed_data()) == 0
    assert analyst.reports_generated == 0
    assert analyst.specialization == "Statistics"

    # После анализа данных
    mock_data = type('MockWeatherData', (), {'data_id': 'STATE001'})()
    analyst.add_analyzed_data(mock_data)
    assert len(analyst.get_analyzed_data()) == 1

    # После генерации отчета
    analyst.generate_report()
    assert analyst.reports_generated == 1

    # Проверка неизменности основных полей
    assert analyst.employee_id == "STATE"
    assert analyst.name == "State Analyst"


