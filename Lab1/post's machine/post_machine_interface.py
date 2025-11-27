from post_machine import PostMachine


def show_status(machine):
    status = machine.get_status()
    current_cmd = machine.find_line(status['current_line']) if not status['halted'] else "ОСТАНОВ"

    print(f"\nТекущая строка: {status['current_line']}")
    print(f"Команда: {current_cmd}")
    print(f"Символ: {status['symbol']}")
    print(f"Позиция: {status['position']}")
    print(f"Лента: {status['tape_content']}")
    print(f"Шагов: {status['steps']}")

    if status['halted']:
        print("\nМашина остановлена")
        print(f"Результат: {status['tape_content']}")


def show_log(machine):
    log = machine.get_log()
    if not log:
        print("\nЛог пуст")
        return

    print("\n--- ЛОГ ВЫПОЛНЕНИЯ ---")
    for entry in log:
        print(f"Шаг {entry['step']}: строка {entry['line']} - {entry['command']}")
        print(f"  Символ: {entry['symbol']}, Следующая строка: {entry['next_line']}")
        print(f"  Позиция: {entry['position']}, Лента: {entry['tape']}")


def main():
    machine = PostMachine()

    print("=== МАШИНА ПОСТА ===")

    # Загрузка ленты
    tape_input = input("Начальная лента (0 и 1, Enter для '0'): ").strip()
    machine.load_tape(tape_input if tape_input else "0")

    # Загрузка программы
    choice = input("Загрузить программу из файла? (y/n): ").strip().lower()
    if choice == 'y':
        filename = input("Имя файла: ").strip()
        try:
            machine.load_program_from_file(filename)
            print("Программа загружена")
        except FileNotFoundError:
            print("Файл не найден")
            return
    else:
        print("Введите программу построчно (пустая строка - конец):")
        print("Формат: → n, ← n, 0 n, 1 n, ? m n, !")
        program = []
        line_num = 1
        while True:
            line = input(f"{line_num}. ").strip()
            if not line:
                break
            program.append(f"{line_num}. {line}")
            line_num += 1
        machine.load_program(program)

    # Основной цикл
    while True:
        show_status(machine)

        if machine.halted:
            print("\nКоманды: r-рестарт, l-логи, q-выход")
        else:
            print("\nКоманды: n-шаг, r-запуск, l-логи, s-сброс, q-выход")

        cmd = input("> ").strip().lower()

        if cmd == 'n' and not machine.halted:
            machine.step()
        elif cmd == 'r' and not machine.halted:
            steps = machine.run(1000)
            print(f"Выполнено шагов: {steps}")
        elif cmd == 'r' and machine.halted:
            machine.reset()
        elif cmd == 's':
            machine.reset()
            print("Машина сброшена")
        elif cmd == 'l':
            show_log(machine)
        elif cmd == 'q':
            break


if __name__ == "__main__":
    main()