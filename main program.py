"""
main.py - точка входа в игру "Лабиринт Минотавра"
"""
from maze import (
    show_help,
    describe,
    move,
    random_noise,
    calculate_step_distance,
    get_items_in_room
)


def main():
    # Состояние игры
    room = "start"
    description = describe(room)
    has_sword = False
    has_thread = False
    total_distance = 0.0  # пройденная дистанция
    rooms_visited = 1  # счётчик посещённых комнат (включая стартовую)

    # Приветствие игрока
    print("=" * 50)
    print("   ЛАБИРИНТ МИНОТАВРА")
    print("   Найдите меч и выйдите из лабиринта!")
    print("   Введите 'help' для списка команд.")
    print("=" * 50)
    print(description)

    # Показать предметы в стартовой комнате
    items_here = get_items_in_room(room)
    if items_here:
        print("Здесь лежит: " + items_here)

    # Основной цикл игры
    while True:
        try:
            command = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nИгра прервана.")
            break

        if not command:
            continue

        # Разбор команды: действие и аргумент
        parts = command.split()
        action = parts[0]
        arg = parts[1] if len(parts) > 1 else ""

        # help — список команд
        if action == "help":
            show_help()

        # look — осмотреть комнату
        elif action == "look":
            print(describe(room))
            items_here = get_items_in_room(room)
            if items_here:
                print("Здесь лежит: " + items_here)

        # go <direction> — перемещение между комнатами
        elif action == "go":
            new_room, success = move(room, arg)

            if not success:
                print("Туда нельзя идти.")
                continue

            # Рассчитать расстояние и обновить статистику
            step_distance = calculate_step_distance(room, new_room)
            total_distance += step_distance
            rooms_visited += 1

            room = new_room
            description = describe(room)
            print(description)

            # Показать предметы в новой комнате
            items_here = get_items_in_room(room)
            if items_here:
                print("Здесь лежит: " + items_here)

            # Случайное событие
            event = random_noise()
            if event:
                print("\n! " + event)

            # Победа: выйти с мечом
            if room == "exit":
                if has_sword:
                    print("\n ПОБЕДА! Вы с мечом в руках покинули лабиринт Минотавра!")
                    print(" Статистика: посещено комнат: " + str(rooms_visited) +
                          ", пройдено дистанции: " + str(round(total_distance, 1)) + " ед.")
                    break
                else:
                    print("Без меча вы не чувствуете себя в безопасности. Вернитесь и найдите его.")

        # take <item> — взять предмет
        elif action == "take":
            items_here = get_items_in_room(room)

            if arg == "sword" and room == "trap" and not has_sword:
                has_sword = True
                print("Вы подобрали меч. Теперь вы вооружены!")
            elif arg == "thread" and room == "corridor2" and not has_thread:
                has_thread = True
                print("Вы взяли клубок нити.")
            elif arg == "sword" or arg == "thread":
                print("Здесь нечего брать.")
            else:
                print("Нет такого предмета.")

        # use <item> — использовать предмет
        elif action == "use":
            if arg == "thread" and has_thread:
                print("Нить помогает вам помнить путь, но не заменяет меч.")
            elif arg == "sword" and has_sword:
                print("Вы крепко сжимаете рукоять меча.")
            else:
                print("Вам нечего использовать.")

        # stats — показать статистику
        elif action == "stats":
            print("\n СТАТИСТИКА:")
            print("   Текущая комната: " + room)
            print("   Посещено комнат: " + str(rooms_visited))
            print("   Пройдено дистанции: " + str(round(total_distance, 1)) + " ед.")
            inv = ""
            if has_sword:
                inv = inv + "меч "
            if has_thread:
                inv = inv + "нить "
            if inv == "":
                inv = "пусто"
            print("   Инвентарь: " + inv)

        # exit — выйти из игры
        elif action == "exit":
            print("Вы покинули игру. До встречи!")
            break

        # Неизвестная команда
        else:
            print("Неизвестная команда. Введите 'help'.")


if __name__ == "__main__":
    main()