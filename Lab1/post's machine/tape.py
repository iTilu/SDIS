
class Tape:
    def __init__(self, initial_data = ''):
        self.tape = {}
        self.position = 0
        self.min_position = 0
        self.max_position = 0

        for i, item in enumerate(initial_data):
            self.tape[i] = 1 if item == '1' else 0

        if initial_data:
            self.max_position = len(initial_data) - 1

    def read(self):
        if self.position not in self.tape:
            self.max_position = max(self.max_position, self.position)
            self.min_position = min(self.min_position, self.position)
        return self.tape.get(self.position, 0)


    def write(self, value):
        if value == 1:
            self.tape[self.position] = value
        elif value == 0:
            if self.position in self.tape:
                del self.tape[self.position]
        self.max_position = max(self.max_position, self.position)
        self.min_position = min(self.min_position, self.position)

    def move_left(self):
        self.position -= 1
        self.max_position = max(self.max_position, self.position)
        self.min_position = min(self.min_position, self.position)

    def move_right(self):
        self.position += 1
        self.max_position = max(self.max_position, self.position)
        self.min_position = min(self.min_position, self.position)

    def get_full_tape(self):
        if not self.tape:
            return '0'

        symbols = []
        for i in range(self.min_position, self.max_position+1):
            symbol = self.tape.get(i, 0)
            symbols.append('1' if symbol == 1 else '0')

        return ''.join(symbols)
