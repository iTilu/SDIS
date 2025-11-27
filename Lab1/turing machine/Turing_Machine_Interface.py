from Turing_Machine import TuringMachine


def show_status(tm):
    status = tm.get_status()
    print(f"\nТекущее состояние: {status['state']}")
    print(f"Текущий символ: '{status['symbol']}'")
    print(f"Позиция: {status['position']}")
    print(f"Шагов выполнено: {status['steps']}")
    print(f"Лента: {tm.tape.get_visible_tape()}")
    if status['halted']:
        print("Статус: ОСТАНОВЛЕНА")
    else:
        print("Статус: ВЫПОЛНЯЕТСЯ")


def show_log(tm):
    log = tm.get_log()
    if not log:
        print("Лог пуст")
        return

    print("\n--- ЛОГ ВЫПОЛНЕНИЯ ---")
    for entry in log:
        print(f"Шаг {entry['step']}: "
              f"Состояние {entry['state']} -> {entry['new_state']}, "
              f"Символ '{entry['symbol']}' -> '{entry['new_symbol']}', "
              f"Движение: {entry['direction']}")
        print(f"   Позиция: {entry['position']}, Лента: {entry['tape_snapshot']}")


def save_log_to_file(tm, filename):
    """Сохраняет лог в файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        for entry in tm.get_log():
            f.write(f"Шаг {entry['step']}: "
                    f"Состояние {entry['state']} -> {entry['new_state']}, "
                    f"Символ '{entry['symbol']}' -> '{entry['new_symbol']}', "
                    f"Движение: {entry['direction']}\n")
            f.write(f"   Позиция: {entry['position']}, Лента: {entry['tape_snapshot']}\n\n")
    print(f"Лог сохранен в файл: {filename}")


def main():
    tm = TuringMachine()

    print("=== МАШИНА ТЬЮРИНГА ===")

    # Загрузка начальной ленты
    tape_input = input("Введите начальную ленту (или Enter для пустой): ").strip()
    tm.load_tape(tape_input)

    # Загрузка программы
    choice = input("Загрузить программу из файла? (y/n): ").strip().lower()
    if choice == 'y':
        filename = input("Имя файла с программой: ").strip()
        try:
            tm.load_program_from_file(filename)
            print("Программа загружена")
        except FileNotFoundError:
            print("Файл не найден, программа не загружена")
            return
    else:
        print("Введите команды построчно (пустая строка для завершения):")
        print("Формат: <состояние> <символ> <новое_состояние> <новый_символ> <направление>")
        print("Направление: L-влево, R-вправо, S-остаться")
        program = []
        while True:
            line = input("> ").strip()
            if not line:
                break
            program.append(line)
        tm.load_program(program)

    # Основной цикл
    while True:
        show_status(tm)

        if tm.halted:
            print("\nМашина остановилась!")
            final_content = tm.get_status()['tape_content']
            print(f"Результат на ленте: {final_content}")
            break

        cmd = input("\nКоманды: n-шаг, r-запуск, l-лог, s-сохранить лог, q-выход: ").strip().lower()

        if cmd == 'n':
            if not tm.step():
                print("Машина остановилась!")
                final_content = tm.get_status()['tape_content']
                print(f"Результат на ленте: {final_content}")
        elif cmd == 'r':
            max_steps = input("Максимальное число шагов (по умолчанию 1000): ").strip()
            try:
                max_steps = int(max_steps) if max_steps else 1000
            except ValueError:
                max_steps = 1000

            steps = tm.run(max_steps)
            print(f"Выполнено шагов: {steps}")

            if tm.halted:
                final_content = tm.get_status()['tape_content']
                print(f"Результат на ленте: {final_content}")
        elif cmd == 'l':
            show_log(tm)
        elif cmd == 's':
            filename = input("Имя файла для сохранения лога: ").strip()
            save_log_to_file(tm, filename)
        elif cmd == 'q':
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()