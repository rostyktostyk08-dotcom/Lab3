"""
Модуль maze.py - карта лабиринта и игровые функции
"""
import random
import math


def show_help():
    """Показать список доступных команд"""
    print("\n" + "=" * 50)
    print("ДОСТУПНЫЕ КОМАНДЫ:")
    print("  help                  - показать этот список")
    print("  look                  - осмотреть комнату")
    print("  go <направление>      - двигаться (north/south/east/west)")
    print("  take <предмет>        - взять предмет")
    print("  use <предмет>         - использовать предмет")
    print("  stats                 - показать статистику")
    print("  exit                  - выйти из игры")
    print("=" * 50)


def describe(room):
    """Вернуть описание комнаты через if/elif"""
    if room == "start":
        return "Вы находитесь у входа в лабиринт. Стены покрыты мхом."
    elif room == "corridor1":
        return "Длинный коридор. Паутина свисает с потолка."
    elif room == "corridor2":
        return "Перекрёсток."
    elif room == "trap":
        return "Опасное место! На полу блестит меч."
    elif room == "hall":
        return "Огромный зал с колоннами. Впереди виднеется выход."
    elif room == "exit":
        return "Выход из лабиринта. Дневной свет слепит глаза."
    return "Неизвестная комната."


def move(room, direction):
    """
    Попытка переместиться в направлении direction из комнаты room.
    Возвращает (новая_комната, успех) через if/elif
    """
    if room == "start" and direction == "north":
        return "corridor1", True
    elif room == "corridor1":
        if direction == "south":
            return "start", True
        elif direction == "east":
            return "corridor2", True
    elif room == "corridor2":
        if direction == "west":
            return "corridor1", True
        elif direction == "north":
            return "trap", True
        elif direction == "south":
            return "hall", True
    elif room == "trap" and direction == "south":
        return "corridor2", True
    elif room == "hall":
        if direction == "west":
            return "corridor2", True
        elif direction == "east":
            return "exit", True
    elif room == "exit" and direction == "west":
        return "hall", True

    return room, False


def get_room_coordinates(room):
    """Вернуть координаты комнаты (x, y) для расчёта расстояния"""
    if room == "start":
        return 0, 0
    elif room == "corridor1":
        return 0, 1
    elif room == "corridor2":
        return 1, 1
    elif room == "trap":
        return 1, 2
    elif room == "hall":
        return 1, 0
    elif room == "exit":
        return 2, 0
    return 0, 0


def calculate_step_distance(room1, room2):
    """
    Рассчитать расстояние между двумя комнатами.
    Использует math.sqrt для евклидова расстояния.
    """
    x1, y1 = get_room_coordinates(room1)
    x2, y2 = get_room_coordinates(room2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_items_in_room(room):
    """Вернуть строку с предметами в комнате"""
    if room == "corridor2":
        return "thread"
    elif room == "trap":
        return "sword"
    return ""


def random_noise():
    """
    Случайное событие с вероятностью 20%.
    Возвращает текст события или пустую строку.
    Использует random.randint
    """
    if random.random() < 0.2:  # 20% шанс
        event_num = random.randint(0, 5)
        if event_num == 0:
            return "Вы слышите шорох за стеной... Кто-то наблюдает за вами."
        elif event_num == 1:
            return "Небольшой обвал! Путь позади вас частично завален камнями."
        elif event_num == 2:
            return "На стене найдена древняя подсказка: 'Минотавр боится света'."
        elif event_num == 3:
            return "Вы чувствуете холодное дыхание из темноты."
        elif event_num == 4:
            return "Где-то вдалеке раздаётся тяжёлый шаг."
        else:
            return "Вы находите старый факел, но он уже не горит."
    return ""