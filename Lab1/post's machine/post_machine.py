
from tape import Tape

class PostMachine:
    def __init__(self):
        self.tape = Tape()
        self.program = []
        self.current_line = 1
        self.halted = False
        self.step_count = 0
        self.log = []


    def load_tape(self, tape_string):
        self.tape = Tape(tape_string)

    def load_program(self, program_lines):

        for line_num, line in enumerate(program_lines, 1):
            line = line.strip()
            if not line:
                continue

            if line[0].isdigit() and '.' in line:
                line = line.split('. ', 1)[1]

            self.program.append((line_num, line))

    def load_program_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            program_lines = f.readlines()
        self.load_program(program_lines)

    def find_line(self, line_number):
        for num, cmd in self.program:
            if num == line_number:
                return cmd
        return None

    def execute_command(self, command):
        cmd_parts = command.strip().split()

        if not cmd_parts:
            self.halted = True
            return None

        operation = cmd_parts[0]

        if operation == '!':
            self.halted = True
            return None

        elif operation == '→' or operation == '->':
            if len(cmd_parts) >= 2:
                self.tape.move_right()
                return int(cmd_parts[1])

        elif operation == '←' or operation == '<-':
            if len(cmd_parts) >= 2:
                self.tape.move_left()
                return int(cmd_parts[1])

        elif operation == '0':

            if len(cmd_parts) >= 2:
                self.tape.write(0)
                return int(cmd_parts[1])

        elif operation == '1':
            if len(cmd_parts) >= 2:
                self.tape.write(1)
                return int(cmd_parts[1])

        elif operation == '?':
            if len(cmd_parts) >= 3:
                current_symbol = self.tape.read()
                line_if_0 = int(cmd_parts[1])
                line_if_1 = int(cmd_parts[2])

                if current_symbol == 0:
                    return line_if_0
                else:
                    return line_if_1

        self.halted = True
        return None

    def step(self):
        if self.halted == True or not self.current_line:
            return False

        command = self.find_line(self.current_line)
        if command is None:
            self.halted = True
            return False

        # Логируем начало шага
        old_line = self.current_line
        old_symbol = self.tape.read()
        old_position = self.tape.position


        next_line = self.execute_command(command)

        self.log.append({
            'step': self.step_count,
            'line': old_line,
            'command': command,
            'old_symbol': old_symbol,
            'new_symbol': self.tape.read(),
            'old_position': old_position,
            'new_position': self.tape.position,
            'next_line': next_line,
            'tape_content': self.tape.get_full_tape()
        })
        self.current_line = next_line
        self.step_count += 1

        return True

    def run(self, max_steps=1000):
        executed_steps = 0
        while not self.halted and executed_steps < max_steps:
            if not self.step():
                break
            executed_steps += 1
        return executed_steps

    def get_status(self):
        return {
            'current_line': self.current_line,
            'position': self.tape.position,
            'symbol': self.tape.read(),
            'halted': self.halted,
            'steps': self.step_count,
            'tape_content': self.tape.get_full_tape()
        }

    def reset(self):
        self.current_line = 1
        self.halted = False
        self.program = []
        self.log = []
        self.tape.position = 0
        self.step_count = 0
