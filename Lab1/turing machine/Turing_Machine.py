from Tape import Tape
from Command import CommandSet


class TuringMachine:
    def __init__(self):
        self.tape = Tape()
        self.commands = CommandSet()
        self.current_state = '0'  # начальное состояние
        self.halted = False
        self.log = []  # лог выполнения
        self.step_count = 0  # счетчик шагов

    def load_tape(self, tape_str):
        """Загружает данные на ленту"""
        self.tape = Tape(tape_str)

    def load_program(self, program_lines):
        """Загружает программу из списка строк"""
        for line in program_lines:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split()
                if len(parts) == 5:
                    state, symbol, new_state, new_symbol, direction = parts
                    self.commands.add_command(state, symbol, new_state, new_symbol, direction)

    def load_program_from_file(self, filename):
        """Загружает программу из файла"""
        self.commands.load_from_file(filename)

    def step(self):
        """Выполняет один шаг машины"""
        if self.halted:
            return False

        current_symbol = self.tape.read()
        cmd = self.commands.find_command(self.current_state, current_symbol)

        if cmd is None:
            self.halted = True
            # Логируем остановку
            self.log.append({
                'step': self.step_count,
                'state': self.current_state,
                'symbol': current_symbol,
                'new_state': 'HALT',
                'new_symbol': current_symbol,
                'direction': 'S',
                'position': self.tape.position,
                'tape_snapshot': self.tape.get_visible_tape()
            })
            return False

        # Выполняем команду
        old_state = self.current_state
        old_symbol = current_symbol
        self.tape.write(cmd.new_symbol)
        self.tape.move(cmd.direction)
        self.current_state = cmd.new_state

        # Логируем шаг
        self.log.append({
            'step': self.step_count,
            'state': old_state,
            'symbol': old_symbol,
            'new_state': cmd.new_state,
            'new_symbol': cmd.new_symbol,
            'direction': cmd.direction,
            'position': self.tape.position,
            'tape_snapshot': self.tape.get_visible_tape()
        })

        self.step_count += 1
        return True

    def run(self, max_steps=1000):
        """Запускает выполнение до остановки или достижения max_steps"""
        steps_executed = 0
        while self.step() and steps_executed < max_steps:
            steps_executed += 1
        return steps_executed

    def get_log(self):
        """Возвращает лог выполнения"""
        return self.log

    def reset(self):
        """Сбрасывает машину в начальное состояние"""
        self.current_state = '0'
        self.halted = False
        self.log = []
        self.step_count = 0

    def get_status(self):
        """Возвращает текущий статус машины"""
        return {
            'state': self.current_state,
            'position': self.tape.position,
            'symbol': self.tape.read(),
            'halted': self.halted,
            'steps': self.step_count,
            'tape_content': self.tape.get_full_tape()
        }