import pytest
from post_machine import PostMachine
from tape import Tape


def test_tape_basic_operations():
    """Тест основных операций ленты"""
    tape = Tape()
    assert tape.read() == 0

    tape.write(1)
    assert tape.read() == 1

    tape.move_right()
    assert tape.position == 1
    assert tape.read() == 0

    tape.write(1)
    assert tape.get_full_tape() == "11"


def test_tape_initialization():
    """Тест инициализации ленты"""
    tape = Tape("101")
    assert tape.get_full_tape() == "101"
    assert tape.position == 0
    assert tape.read() == 1


def test_machine_initialization():
    """Тест инициализации машины"""
    machine = PostMachine()
    assert machine.current_line == 1
    assert machine.halted == False
    assert machine.step_count == 0
    assert machine.log == []


def test_machine_load_program():
    """Тест загрузки программы"""
    machine = PostMachine()
    program = ["1. → 2", "2. !"]
    machine.load_program(program)

    assert len(machine.program) == 2
    assert machine.find_line(1) == "→ 2"
    assert machine.find_line(2) == "!"


def test_machine_step_operations():
    """Тест пошагового выполнения команд"""
    machine = PostMachine()
    machine.load_tape("1")
    program = [
        "1. → 2",  # Движение вправо
        "2. 0 3",  # Запись 0
        "3. ? 4 5",  # Условный переход (символ 0 -> строка 4)
        "4. 1 6",  # Запись 1
        "5. 0 6",  # Запись 0
        "6. !"  # Остановка
    ]
    machine.load_program(program)

    # Шаг 1: движение вправо
    assert machine.step() == True
    assert machine.current_line == 2
    assert machine.tape.position == 1

    # Шаг 2: запись 0
    assert machine.step() == True
    assert machine.current_line == 3
    assert machine.tape.read() == 0

    # Шаг 3: условный переход (символ 0 -> строка 4)
    assert machine.step() == True
    assert machine.current_line == 4

    # Шаг 4: запись 1
    assert machine.step() == True
    assert machine.current_line == 6
    assert machine.tape.read() == 1

    # Шаг 5: остановка
    assert machine.step() == True  # Команда остановки выполняется как шаг
    assert machine.halted == True

    # Следующий шаг после остановки должен вернуть False
    assert machine.step() == False


def test_machine_run():
    """Тест автоматического выполнения"""
    machine = PostMachine()
    program = ["1. → 2", "2. → 3", "3. → 4", "4. !"]
    machine.load_program(program)

    steps = machine.run(max_steps=10)

    assert steps == 4  # Исправлено: 4 шага вместо 3
    assert machine.halted == True
    assert machine.tape.position == 3


def test_machine_reset():
    """Тест сброса машины"""
    machine = PostMachine()
    program = ["1. → 2", "2. !"]
    machine.load_program(program)

    machine.step()
    assert machine.current_line == 2
    assert machine.step_count == 1

    machine.reset()
    assert machine.current_line == 1
    assert machine.halted == False
    assert machine.step_count == 0
    assert machine.log == []
    assert machine.tape.position == 0


def test_conditional_logic():
    """Тест условной логики"""
    # Тест когда символ 0
    machine = PostMachine()
    machine.load_tape("0")
    program = ["1. ? 2 3", "2. 1 4", "3. 0 4", "4. !"]
    machine.load_program(program)

    machine.run(max_steps=10)
    assert machine.tape.get_full_tape() == "1"  # Должна записаться 1

    # Тест когда символ 1
    machine = PostMachine()
    machine.load_tape("1")
    machine.load_program(program)

    machine.run(max_steps=10)
    assert machine.tape.get_full_tape() == "0"  # Должна записаться 0


def test_halt_condition():
    """Тест условий остановки"""
    machine = PostMachine()

    # Остановка по команде !
    program = ["1. !"]
    machine.load_program(program)
    assert machine.step() == True  # Команда остановки выполняется как шаг
    assert machine.halted == True
    assert machine.step() == False  # Следующий шаг возвращает False

    # Остановка при отсутствии команды
    machine = PostMachine()
    program = ["1. → 99"]  # Переход на несуществующую строку
    machine.load_program(program)
    machine.step()  # Движение вправо
    assert machine.step() == False  # Попытка найти строку 99
    assert machine.halted == True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])