class Tape:
    def __init__(self, initial_data=""):
        # Словарь для хранения символов: ключ - позиция, значение - символ
        self.tape = {}
        self.position = 0

        # Инициализируем ленту начальными данными
        for i, symbol in enumerate(initial_data):
            self.tape[i] = symbol

    def read(self):
        # Если в текущей позиции есть символ - возвращаем его, иначе возвращаем пустой символ '_'
        return self.tape.get(self.position, '_')

    def write(self, symbol):
        if symbol == '_':
            # Если пишем пустой символ, удаляем позицию из словаря
            if self.position in self.tape:
                del self.tape[self.position]
        else:
            # Иначе сохраняем символ в текущей позиции
            self.tape[self.position] = symbol

    def move(self, direction):
        if direction == 'L':
            self.position -= 1
        elif direction == 'R':
            self.position += 1
        # 'S' - остается на месте

    def get_visible_tape(self, width=10):
        """Возвращает видимую часть ленты вокруг текущей позиции"""
        if not self.tape:
            return "[_] (пустая лента)"

        # Находим границы ленты
        min_pos = min(self.tape.keys()) if self.tape else 0
        max_pos = max(self.tape.keys()) if self.tape else 0

        # Расширяем границы для отображения
        start = min(min_pos, self.position - width)
        end = max(max_pos, self.position + width) + 1

        symbols = []
        for i in range(start, end):
            symbol = self.tape.get(i, '_')
            symbols.append(symbol)

        tape_str = ''.join(symbols)

        return f"[{tape_str}] (позиция {self.position})"

    def get_full_tape(self):
        """Возвращает полное содержимое ленты в виде строки"""
        if not self.tape:
            return ""

        min_pos = min(self.tape.keys())
        max_pos = max(self.tape.keys())

        symbols = []
        for i in range(min_pos, max_pos + 1):
            symbols.append(self.tape.get(i, '_'))

        return ''.join(symbols)