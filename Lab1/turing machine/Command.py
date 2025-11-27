class Command:
    def __init__(self, state, symbol, new_state, new_symbol, direction):
        self.state = state
        self.symbol = symbol
        self.new_state = new_state
        self.new_symbol = new_symbol
        self.direction = direction

    def matches(self, state, symbol):
        return self.state == state and self.symbol == symbol


class CommandSet:
    def __init__(self):
        self.commands = []

    def add_command(self, state, symbol, new_state, new_symbol, direction):
        self.commands.append(Command(state, symbol, new_state, new_symbol, direction))

    def find_command(self, state, symbol):
        for cmd in self.commands:
            if cmd.matches(state, symbol):
                return cmd
        return None

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    if len(parts) == 5:
                        state, symbol, new_state, new_symbol, direction = parts
                        self.add_command(state, symbol, new_state, new_symbol, direction)