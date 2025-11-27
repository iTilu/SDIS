import pytest
from Tape import Tape
from Command import Command, CommandSet
from Turing_Machine import TuringMachine


def test_tape_initialization():
    tape = Tape()
    assert tape.position == 0
    assert tape.read() == '_'

    tape = Tape("101")
    assert tape.tape == {0: '1', 1: '0', 2: '1'}
    assert tape.position == 0


def test_tape_read_write():
    tape = Tape()
    assert tape.read() == '_'

    tape.write('1')
    assert tape.read() == '1'

    tape.write('_')
    assert tape.read() == '_'


def test_tape_move():
    tape = Tape("101")
    assert tape.position == 0

    tape.move('R')
    assert tape.position == 1
    assert tape.read() == '0'

    tape.move('L')
    assert tape.position == 0
    assert tape.read() == '1'

    tape.move('S')
    assert tape.position == 0


def test_tape_get_visible_tape():
    tape = Tape("101")
    visible = tape.get_visible_tape(5)
    assert "101" in visible
    assert "позиция 0" in visible

    tape.move('R')
    visible = tape.get_visible_tape(2)
    assert "101" in visible


def test_tape_get_full_tape():
    tape = Tape("101")
    assert tape.get_full_tape() == "101"

    tape = Tape()
    assert tape.get_full_tape() == ""


def test_tape_expansion():
    tape = Tape()
    tape.write('A')
    assert tape.read() == 'A'

    tape.move('R')
    tape.write('B')
    assert tape.read() == 'B'

    tape.move('L')
    tape.move('L')
    tape.write('C')
    assert tape.read() == 'C'

    assert tape.get_full_tape() == "CAB"


def test_command_creation():
    cmd = Command('0', '1', '1', '0', 'R')
    assert cmd.state == '0'
    assert cmd.symbol == '1'
    assert cmd.new_state == '1'
    assert cmd.new_symbol == '0'
    assert cmd.direction == 'R'


def test_command_matches():
    cmd = Command('0', '1', '1', '0', 'R')
    assert cmd.matches('0', '1') == True
    assert cmd.matches('0', '0') == False
    assert cmd.matches('1', '1') == False


def test_command_set_add_and_find():
    cmd_set = CommandSet()
    cmd_set.add_command('0', '1', '1', '0', 'R')
    cmd_set.add_command('0', '0', '0', '1', 'R')

    cmd = cmd_set.find_command('0', '1')
    assert cmd is not None
    assert cmd.new_state == '1'
    assert cmd.new_symbol == '0'

    cmd = cmd_set.find_command('0', '0')
    assert cmd is not None
    assert cmd.new_state == '0'
    assert cmd.new_symbol == '1'

    cmd = cmd_set.find_command('1', '0')
    assert cmd is None


def test_command_set_empty():
    cmd_set = CommandSet()
    cmd = cmd_set.find_command('0', '1')
    assert cmd is None


def test_turing_machine_initialization():
    tm = TuringMachine()
    assert tm.current_state == '0'
    assert tm.halted == False
    assert tm.step_count == 0
    assert len(tm.log) == 0


def test_turing_machine_load_tape():
    tm = TuringMachine()
    tm.load_tape("101")
    assert tm.tape.get_full_tape() == "101"


def test_turing_machine_load_program():
    tm = TuringMachine()
    program = [
        "0 1 0 0 R",
        "0 0 0 1 R",
        "0 _ 1 _ L"
    ]
    tm.load_program(program)

    cmd = tm.commands.find_command('0', '1')
    assert cmd is not None
    assert cmd.new_symbol == '0'


def test_turing_machine_load_program_with_comments():
    tm = TuringMachine()
    program = [
        "# Это комментарий",
        "0 1 0 0 R",
        "",
        "0 0 0 1 R",
        "   ",
        "# Еще комментарий",
        "0 _ 1 _ L"
    ]
    tm.load_program(program)

    cmd = tm.commands.find_command('0', '1')
    assert cmd is not None
    cmd = tm.commands.find_command('0', '0')
    assert cmd is not None
    cmd = tm.commands.find_command('0', '_')
    assert cmd is not None


def test_turing_machine_step_no_command():
    tm = TuringMachine()
    tm.load_tape("1")

    # Нет команды для состояния '0' и символа '1'
    result = tm.step()
    assert result == False
    assert tm.halted == True
    assert len(tm.log) == 1
    assert tm.log[0]['state'] == '0'
    assert tm.log[0]['symbol'] == '1'


def test_turing_machine_step_with_command():
    tm = TuringMachine()
    tm.load_tape("1")
    program = [
        "0 1 1 0 R"
    ]
    tm.load_program(program)

    result = tm.step()
    assert result == True
    assert tm.current_state == '1'
    assert tm.tape.read() == '_'  # Двинулись вправо
    assert tm.step_count == 1
    assert len(tm.log) == 1
    assert tm.log[0]['state'] == '0'
    assert tm.log[0]['new_state'] == '1'


def test_turing_machine_step_write_blank():
    tm = TuringMachine()
    tm.load_tape("1")
    program = [
        "0 1 1 _ R"
    ]
    tm.load_program(program)

    result = tm.step()
    assert result == True
    assert tm.tape.read() == '_'


def test_turing_machine_run():
    tm = TuringMachine()
    tm.load_tape("11")
    program = [
        "0 1 0 0 R",
        "0 _ 1 _ L"
    ]
    tm.load_program(program)

    steps = tm.run(max_steps=10)
    assert steps == 3  # 2 шага вправо + 1 шаг остановки
    assert tm.halted == True


def test_turing_machine_run_max_steps():
    tm = TuringMachine()
    tm.load_tape("111")
    program = [
        "0 1 0 0 R"
    ]
    tm.load_program(program)

    steps = tm.run(max_steps=2)
    assert steps == 2
    assert tm.halted == False  # Не остановилась, достигнут лимит шагов


def test_turing_machine_reset():
    tm = TuringMachine()
    tm.load_tape("1")
    program = ["0 1 1 0 R"]
    tm.load_program(program)

    tm.step()
    assert tm.current_state == '1'
    assert tm.step_count == 1

    tm.reset()
    assert tm.current_state == '0'
    assert tm.halted == False
    assert tm.step_count == 0
    assert len(tm.log) == 0


def test_turing_machine_get_status():
    tm = TuringMachine()
    tm.load_tape("101")

    status = tm.get_status()
    assert status['state'] == '0'
    assert status['position'] == 0
    assert status['symbol'] == '1'
    assert status['halted'] == False
    assert status['steps'] == 0
    assert status['tape_content'] == "101"


def test_turing_machine_inversion_program():
    """Тест программы инвертирования битов"""
    tm = TuringMachine()
    tm.load_tape("101")

    program = [
        "0 1 0 0 R",
        "0 0 0 1 R",
        "0 _ 1 _ L",
        "1 0 1 0 L",
        "1 1 1 1 L",
        "1 _ 2 _ R"
    ]
    tm.load_program(program)

    # Запускаем выполнение
    steps = tm.run(max_steps=100)
    assert tm.halted == True
    assert tm.get_status()['tape_content'] == "010"  # Инвертированная строка


def test_turing_machine_movement_program():
    """Тест программы, которая просто движется по ленте"""
    tm = TuringMachine()
    tm.load_tape("111")

    program = [
        "0 1 0 1 R",
        "0 _ 1 _ L"
    ]
    tm.load_program(program)

    steps = tm.run(max_steps=10)
    assert tm.halted == True
    # Должны были дойти до конца и вернуться к началу
    assert tm.tape.position == 2


def test_turing_machine_already_halted():
    tm = TuringMachine()
    tm.load_tape("1")
    tm.halted = True

    result = tm.step()
    assert result == False


def test_turing_machine_empty_tape():
    tm = TuringMachine()
    tm.load_tape("")
    program = ["0 _ 1 _ R"]
    tm.load_program(program)

    result = tm.step()
    assert result == True
    assert tm.current_state == '1'


def test_turing_machine_single_state_program():
    tm = TuringMachine()
    tm.load_tape("1")
    program = ["0 1 0 1 S"]  # Бесконечный цикл в одном состоянии
    tm.load_program(program)

    steps = tm.run(max_steps=5)
    assert steps == 5  # Остановились по max_steps
    assert tm.halted == False


def test_turing_machine_immediate_halt():
    tm = TuringMachine()
    tm.load_tape("1")
    # Нет команд вообще
    result = tm.step()
    assert result == False
    assert tm.halted == True


def test_turing_machine_log_structure():
    tm = TuringMachine()
    tm.load_tape("1")
    program = ["0 1 1 0 R"]
    tm.load_program(program)

    tm.step()
    log_entry = tm.log[0]

    assert 'step' in log_entry
    assert 'state' in log_entry
    assert 'symbol' in log_entry
    assert 'new_state' in log_entry
    assert 'new_symbol' in log_entry
    assert 'direction' in log_entry
    assert 'position' in log_entry
    assert 'tape_snapshot' in log_entry


def test_complex_program():
    """Тест более сложной программы"""
    tm = TuringMachine()
    tm.load_tape("101010")

    program = [
        "0 1 0 0 R",
        "0 0 0 1 R",
        "0 _ 1 _ L",
        "1 0 1 0 L",
        "1 1 1 1 L",
        "1 _ 2 _ R"
    ]
    tm.load_program(program)

    steps = tm.run(max_steps=1000)
    assert tm.halted == True
    assert tm.get_status()['tape_content'] == "010101"  # Инвертированная строка