#!/usr/bin/env python3
"""
Скрипт для анализа классов Python и подсчета полей, методов и ассоциаций.
"""

import ast
import os
import re
from typing import Dict, List, Set, Tuple
from pathlib import Path


class ClassAnalyzer(ast.NodeVisitor):
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.classes: Dict[str, Dict] = {}
        self.current_class = None
        self.imports: Set[str] = set()
        self.all_class_names: Set[str] = set()

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.add(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module:
            self.imports.add(node.module)
        for alias in node.names:
            self.imports.add(alias.name)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.all_class_names.add(node.name)
        self.current_class = {
            'name': node.name,
            'fields': set(),
            'methods': set(),
            'associations': set(),
            'base_classes': []
        }

        # Анализируем базовые классы
        for base in node.bases:
            if isinstance(base, ast.Name):
                self.current_class['base_classes'].append(base.id)
                if base.id in self.all_class_names:
                    self.current_class['associations'].add(base.id)
            elif isinstance(base, ast.Attribute):
                # Обработка qualified names типа module.Class
                base_name = base.attr
                self.current_class['base_classes'].append(base_name)
                if base_name in self.all_class_names:
                    self.current_class['associations'].add(base_name)

        self.classes[node.name] = self.current_class
        self.generic_visit(node)
        self.current_class = None

    def visit_FunctionDef(self, node):
        if self.current_class:
            # Все функции в классе считаем методами, включая __init__
            self.current_class['methods'].add(node.name)

            # Анализируем тело метода на ассоциации
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    # Вызовы функций/конструкторов
                    if isinstance(child.func, ast.Name):
                        func_name = child.func.id
                        # Если это имя класса из импортов или известных классов
                        if func_name in self.all_class_names or func_name in self.imports:
                            self.current_class['associations'].add(func_name)
                    elif isinstance(child.func, ast.Attribute) and isinstance(child.func.value, ast.Name):
                        # self.some_method() - это метод, уже учтен
                        pass
                elif isinstance(child, ast.Attribute) and isinstance(child.value, ast.Name):
                    # self.some_attr - потенциальное поле
                    if child.value.id == 'self':
                        self.current_class['fields'].add(child.attr)
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        # Аннотированные присваивания в классе
        if self.current_class and isinstance(node.target, ast.Name):
            self.current_class['fields'].add(node.target.id)
        self.generic_visit(node)

    def visit_Assign(self, node):
        # Присваивания в классе
        if self.current_class:
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.current_class['fields'].add(target.id)
                elif isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name):
                    if target.value.id == 'self':
                        self.current_class['fields'].add(target.attr)
        self.generic_visit(node)


def analyze_file(file_path: str) -> Dict[str, Dict]:
    """Анализирует Python файл и возвращает информацию о классах."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()

        tree = ast.parse(source_code, filename=file_path)
        analyzer = ClassAnalyzer(source_code)
        analyzer.visit(tree)

        # Дополнительный анализ ассоциаций из TYPE_CHECKING импортов и комментариев
        for class_name, class_info in analyzer.classes.items():
            # Ищем TYPE_CHECKING импорты
            type_checking_pattern = r'if TYPE_CHECKING:\s*\n(?:\s*from\s+[\w.]+\s+import\s+(.+?)\n?)+'
            type_matches = re.findall(type_checking_pattern, source_code, re.MULTILINE)
            for match in type_matches:
                imports = [imp.strip() for imp in match.split(',')]
                for imp in imports:
                    class_name_from_import = imp.split()[-1]  # Берем последнее слово после 'as' или само имя
                    class_info['associations'].add(class_name_from_import)

            # Ищем ассоциации в комментариях типа "# ассоциация с Class"
            pattern = r'#.*ассоциация.*с\s+(\w+)'
            matches = re.findall(pattern, source_code, re.IGNORECASE)
            class_info['associations'].update(matches)

            # Ищем ассоциации в docstrings методов
            for match in re.finditer(r'"""(.*?)"""', source_code, re.DOTALL):
                docstring = match.group(1)
                for other_class in analyzer.classes.keys():
                    if other_class != class_name and other_class in docstring:
                        class_info['associations'].add(other_class)

        return analyzer.classes

    except Exception as e:
        print(f"Ошибка анализа файла {file_path}: {e}")
        return {}


def analyze_directory(directory: str) -> Dict[str, Dict]:
    """Анализирует все Python файлы в директории."""
    all_classes = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and not file.startswith('test_'):
                file_path = os.path.join(root, file)
                classes = analyze_file(file_path)
                all_classes.update(classes)

    return all_classes


def format_class_info(class_name: str, info: Dict) -> str:
    """Форматирует информацию о классе в требуемом формате."""
    fields_count = len(info['fields'])
    methods_count = len(info['methods'])
    associations = sorted(list(info['associations']))

    if associations:
        associations_str = ' -> ' + ', '.join(associations)
    else:
        associations_str = ''

    return f"{class_name} {fields_count} {methods_count}{associations_str}"


def main():
    # Анализ Lab1
    print("Анализ Lab1...")
    lab1_classes = {}

    # Post machine
    post_machine_dir = "/home/itiluvm/SDIS/Lab1/post's machine"
    lab1_classes.update(analyze_directory(post_machine_dir))

    # Turing machine
    turing_machine_dir = "/home/itiluvm/SDIS/Lab1/turing machine"
    lab1_classes.update(analyze_directory(turing_machine_dir))

    # Создание README для Lab1
    lab1_readme = []
    for class_name in sorted(lab1_classes.keys()):
        lab1_readme.append(format_class_info(class_name, lab1_classes[class_name]))

    with open('/home/itiluvm/SDIS/Lab1/README.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lab1_readme))
        f.write('\n')

    print("Lab1 README создан")

    # Анализ Lab2
    print("Анализ Lab2...")
    lab2_classes = analyze_directory("/home/itiluvm/SDIS/Lab2")

    # Создание README для Lab2
    lab2_readme = []
    for class_name in sorted(lab2_classes.keys()):
        lab2_readme.append(format_class_info(class_name, lab2_classes[class_name]))

    with open('/home/itiluvm/SDIS/Lab2/README.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lab2_readme))
        f.write('\n')

    print("Lab2 README создан")


if __name__ == "__main__":
    main()
