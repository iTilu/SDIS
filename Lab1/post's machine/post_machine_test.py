import pytest
from post_machine import PostMachine
from tape import Tape


def test_tape_initialization_empty():
    """Тест инициализации пустой ленты"""
    tape = Tape()
    assert tape.position == 0
    assert tape.min_position == 0
    assert tape.max_position == 0
    assert tape.read() == 0
    assert tape.get_full_tape() == "0"


def test_tape_initialization_with_data():
    """Тест инициализации ленты с данными"""
    tape = Tape("101")
    assert tape.position == 0
    assert tape.min_position == 0
    assert tape.max_position == 2
    assert tape.read() == 1
    assert tape.get_full_tape() == "101"


def test_tape_write_zero():
    """Тест записи нуля (удаление символа)"""
    tape = Tape("1")
    tape.write(0)
    assert tape.read() == 0
    assert tape.get_full_tape() == "0"  # Пустая лента отображается как "0"


def test_tape_write_one():
    """Тест записи единицы"""
    tape = Tape()
    tape.write(1)
    assert tape.read() == 1
    assert tape.get_full_tape() == "1"


def test_tape_write_invalid_value():
    """Тест записи недопустимого значения"""
    tape = Tape()
    # Tape.write не проверяет входные значения, но read возвращает только 0 или 1
    tape.write(2)
    assert tape.read() == 0  # read возвращает 0 для любых значений кроме 1


def test_tape_move_right():
    """Тест движения вправо"""
    tape = Tape("10")
    tape.move_right()
    assert tape.position == 1
    assert tape.read() == 0
    assert tape.min_position == 0
    assert tape.max_position == 1


def test_tape_move_left():
    """Тест движения влево"""
    tape = Tape("10")
    tape.move_left()
    assert tape.position == -1
    assert tape.read() == 0  # Автоматически создается пустая позиция
    assert tape.min_position == -1
    assert tape.max_position == 1


def test_tape_read_uninitialized_position():
    """Тест чтения неинициализированной позиции"""
    tape = Tape()
    tape.move_right()
    tape.move_right()
    assert tape.read() == 0  # Возвращает 0 для неинициализированных позиций
    assert tape.position == 2


def test_tape_get_full_tape_empty():
    """Тест получения полного содержимого пустой ленты"""
    tape = Tape()
    assert tape.get_full_tape() == "0"


def test_tape_get_full_tape_with_gaps():
    """Тест получения полного содержимого ленты с пробелами"""
    tape = Tape()
    tape.write(1)
    tape.move_right()
    tape.move_right()
    tape.write(1)
    # Лента: позиция 0 = 1, позиция 2 = 1
    assert tape.get_full_tape() == "101"


def test_tape_expansion():
    """Тест расширения ленты при движении"""
    tape = Tape()
    tape.move_left()
    tape.move_left()
    tape.write(1)
    tape.move_right()
    tape.move_right()
    tape.move_right()
    tape.write(1)

    assert tape.min_position == -2
    assert tape.max_position == 1
    assert tape.get_full_tape() == "1001"


def test_post_machine_initialization():
    """Тест инициализации машины Поста"""
    machine = PostMachine()
    assert machine.current_line == 1
    assert machine.halted == False
    assert machine.step_count == 0
    assert machine.log == []
    assert len(machine.program) == 0


def test_post_machine_load_tape():
    """Тест загрузки ленты"""
    machine = PostMachine()
    machine.load_tape("101")
    assert machine.tape.get_full_tape() == "101"
    assert machine.tape.position == 0


def test_post_machine_load_program_empty():
    """Тест загрузки пустой программы"""
    machine = PostMachine()
    machine.load_program([])
    assert len(machine.program) == 0


def test_post_machine_load_program_basic():
    """Тест загрузки базовой программы"""
    machine = PostMachine()
    program = ["1. → 2", "2. !"]
    machine.load_program(program)

    assert len(machine.program) == 2
    assert machine.program[0] == (1, "→ 2")
    assert machine.program[1] == (2, "!")


def test_post_machine_load_program_with_numbering():
    """Тест загрузки программы с нумерацией строк"""
    machine = PostMachine()
    program = ["1. → 2", "2. 0 3", "3. !"]
    machine.load_program(program)

    assert len(machine.program) == 3
    assert machine.find_line(1) == "→ 2"
    assert machine.find_line(2) == "0 3"
    assert machine.find_line(3) == "!"


def test_post_machine_load_program_with_comments():
    """Тест загрузки программы с комментариями и пустыми строками"""
    machine = PostMachine()
    program = [
        "# Это комментарий",
        "",
        "1. → 2",
        "   ",
        "2. !",
        "# Еще комментарий"
    ]
    machine.load_program(program)

    # Видно, что комментарии тоже включаются как команды
    assert len(machine.program) == 4
    assert machine.find_line(1) == "# Это комментарий"
    assert machine.find_line(3) == "→ 2"
    assert machine.find_line(5) == "!"

def test_post_machine_execute_command_move_right():
    """Тест выполнения команды движения вправо"""
    machine = PostMachine()
    machine.load_tape("1")

    next_line = machine.execute_command("→ 2")
    assert next_line == 2
    assert machine.tape.position == 1
    assert not machine.halted


def test_post_machine_execute_command_move_left():
    """Тест выполнения команды движения влево"""
    machine = PostMachine()
    machine.load_tape("1")
    machine.tape.move_right()  # position = 1

    next_line = machine.execute_command("← 3")
    assert next_line == 3
    assert machine.tape.position == 0
    assert not machine.halted


def test_post_machine_execute_command_write_zero():
    """Тест выполнения команды записи нуля"""
    machine = PostMachine()
    machine.load_tape("1")

    next_line = machine.execute_command("0 4")
    assert next_line == 4
    assert machine.tape.read() == 0
    assert not machine.halted


def test_post_machine_execute_command_write_one():
    """Тест выполнения команды записи единицы"""
    machine = PostMachine()
    machine.load_tape("0")

    next_line = machine.execute_command("1 5")
    assert next_line == 5
    assert machine.tape.read() == 1
    assert not machine.halted


def test_post_machine_execute_command_halt():
    """Тест выполнения команды остановки"""
    machine = PostMachine()

    next_line = machine.execute_command("!")
    assert next_line is None
    assert machine.halted == True


def test_post_machine_execute_command_conditional_zero():
    """Тест условной команды при символе 0"""
    machine = PostMachine()
    machine.load_tape("0")

    next_line = machine.execute_command("? 2 3")
    assert next_line == 2
    assert not machine.halted


def test_post_machine_execute_command_conditional_one():
    """Тест условной команды при символе 1"""
    machine = PostMachine()
    machine.load_tape("1")

    next_line = machine.execute_command("? 2 3")
    assert next_line == 3
    assert not machine.halted


def test_post_machine_execute_command_invalid():
    """Тест выполнения недопустимой команды"""
    machine = PostMachine()

    next_line = machine.execute_command("invalid command")
    assert next_line is None
    assert machine.halted == True


def test_post_machine_execute_command_empty():
    """Тест выполнения пустой команды"""
    machine = PostMachine()

    next_line = machine.execute_command("")
    assert next_line is None
    assert machine.halted == True


def test_post_machine_step_halted():
    """Тест шага при остановленной машине"""
    machine = PostMachine()
    machine.halted = True

    result = machine.step()
    assert result == False


def test_post_machine_step_no_command():
    """Тест шага при отсутствии команды"""
    machine = PostMachine()
    machine.current_line = 99

    result = machine.step()
    assert result == False
    assert machine.halted == True


def test_post_machine_step_normal():
    """Тест нормального шага выполнения"""
    machine = PostMachine()
    machine.load_tape("1")
    program = ["1. → 2"]
    machine.load_program(program)

    result = machine.step()
    assert result == True
    assert machine.current_line == 2
    assert machine.step_count == 1
    assert len(machine.log) == 1


def test_post_machine_run_normal():
    """Тест нормального выполнения программы"""
    machine = PostMachine()
    program = ["1. → 2", "2. → 3", "3. !"]
    machine.load_program(program)

    steps = machine.run(max_steps=10)
    assert steps == 3
    assert machine.halted == True
    assert machine.current_line is None  # current_line становится None после остановки


def test_post_machine_run_max_steps():
    """Тест выполнения с ограничением шагов"""
    machine = PostMachine()
    program = ["1. → 2", "2. → 1"]  # Бесконечный цикл
    machine.load_program(program)

    steps = machine.run(max_steps=5)
    assert steps == 5
    assert not machine.halted


def test_post_machine_run_already_halted():
    """Тест выполнения уже остановленной машины"""
    machine = PostMachine()
    machine.halted = True

    steps = machine.run(max_steps=10)
    assert steps == 0


def test_post_machine_reset():
    """Тест сброса машины"""
    machine = PostMachine()
    program = ["1. → 2", "2. !"]
    machine.load_program(program)
    machine.load_tape("1")
    machine.step()

    assert machine.current_line == 2
    assert machine.step_count == 1
    assert len(machine.log) == 1

    machine.reset()
    assert machine.current_line == 1
    assert not machine.halted
    assert machine.step_count == 0
    assert machine.log == []
    assert machine.tape.position == 0


def test_post_machine_get_status():
    """Тест получения статуса машины"""
    machine = PostMachine()
    machine.load_tape("101")
    program = ["1. → 2"]
    machine.load_program(program)
    machine.step()

    status = machine.get_status()
    assert status['current_line'] == 2
    assert status['position'] == 1
    assert status['symbol'] == 0
    assert status['halted'] == False
    assert status['steps'] == 1
    assert status['tape_content'] == "101"


def test_post_machine_load_program_from_file(tmp_path):
    """Тест загрузки программы из файла"""
    # Создаем временный файл
    program_file = tmp_path / "program.txt"
    program_file.write_text("1. → 2\n2. !\n# Comment\n")

    machine = PostMachine()
    machine.load_program_from_file(str(program_file))

    assert len(machine.program) == 3  # Включая комментарий
    assert machine.find_line(1) == "→ 2"
    assert machine.find_line(2) == "!"
    assert machine.find_line(3) == "# Comment"


def test_post_machine_log_structure():
    """Тест структуры лога выполнения"""
    machine = PostMachine()
    machine.load_tape("1")
    program = ["1. → 2"]
    machine.load_program(program)

    machine.step()

    log_entry = machine.log[0]
    assert 'step' in log_entry
    assert 'line' in log_entry
    assert 'command' in log_entry
    assert 'old_symbol' in log_entry
    assert 'new_symbol' in log_entry
    assert 'old_position' in log_entry
    assert 'new_position' in log_entry
    assert 'next_line' in log_entry
    assert 'tape_content' in log_entry

    assert log_entry['step'] == 0
    assert log_entry['line'] == 1
    assert log_entry['command'] == "→ 2"
    assert log_entry['next_line'] == 2


def test_complex_program_invert():
    """Тест программы инвертирования бита под головкой"""
    machine = PostMachine()
    machine.load_tape("1")  # Один бит

    program = [
        "1. ? 2 3",    # Если 0, перейти к 2; если 1, к 3
        "2. 1 4",      # Записать 1, перейти к 4
        "3. 0 4",      # Записать 0, перейти к 4
        "4. !"         # Остановить
    ]
    machine.load_program(program)

    machine.run(max_steps=10)
    assert machine.tape.get_full_tape() == "0"  # 1 инвертируется в 0


def test_complex_program_copy():
    """Тест программы копирования символа"""
    machine = PostMachine()
    machine.load_tape("10")

    program = [
        "1. ? 2 3",    # Проверить текущий символ
        "2. 0 4",      # Если 0, записать 0 и перейти к 4
        "3. 1 4",      # Если 1, записать 1 и перейти к 4
        "4. ← 5",      # Двинуться влево
        "5. ?"         # Проверить следующий символ (без параметров - остановка)
    ]
    machine.load_program(program)

    machine.run(max_steps=10)
    # Программа должна остановиться на строке 5 из-за неправильного синтаксиса
    assert machine.halted == True


def test_edge_case_empty_program():
    """Тест работы с пустой программой"""
    machine = PostMachine()

    result = machine.step()
    assert result == False
    assert machine.halted == True


def test_edge_case_invalid_command_syntax():
    """Тест обработки команд с неправильным синтаксисом"""
    machine = PostMachine()

    # Неправильный синтаксис команды движения
    next_line = machine.execute_command("→")
    assert next_line is None
    assert machine.halted == True

    machine.reset()
    next_line = machine.execute_command("←")
    assert next_line is None
    assert machine.halted == True

    machine.reset()
    next_line = machine.execute_command("0")
    assert next_line is None
    assert machine.halted == True

    machine.reset()
    next_line = machine.execute_command("1")
    assert next_line is None
    assert machine.halted == True

    machine.reset()
    next_line = machine.execute_command("? 1")
    assert next_line is None
    assert machine.halted == True


def test_edge_case_tape_boundaries():
    """Тест работы с границами ленты"""
    machine = PostMachine()
    machine.load_tape("1")

    # Движение далеко вправо
    for _ in range(10):
        machine.tape.move_right()

    assert machine.tape.position == 10
    assert machine.tape.read() == 0

    # Движение далеко влево
    for _ in range(20):
        machine.tape.move_left()

    assert machine.tape.position == -10
    assert machine.tape.read() == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])