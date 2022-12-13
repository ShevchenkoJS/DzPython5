# Создайте программу для игры в ""Крестики-нолики"".
def check_winner(player: str, table: list) -> bool:
    """Проверка выигрыша конкретного игрока"""
    if table[0] == table[3] == table[6] == player or \
            table[1] == table[4] == table[7] == player or \
            table[2] == table[5] == table[8] == player or \
            table[0] == table[1] == table[2] == player or \
            table[3] == table[4] == table[5] == player or \
            table[6] == table[7] == table[8] == player or \
            table[0] == table[4] == table[8] == player or \
            table[2] == table[4] == table[6] == player:
        return True
    return False


def game_over(table: list) -> int:
    """Определение конца партии: -1 - не окончена, 0 - ничья, 1 - выиграл первый игрок, 2 - выиграл второй игрок"""
    if check_winner('x', table):
        return 1
    elif check_winner('o', table):
        return 2
    elif table.count('x') + table.count('o') == 9:
        return 0
    return -1


def check_step(pos: str, table: list) -> bool:
    """Проверка возможности хода"""
    if not pos.isdigit():
        return False
    pos = int(pos)
    if pos not in range(9):
        return False
    elif table[pos] == 'x' or table[pos] == 'o':
        return False
    return True


def mark_pos(item: str) -> str:
    """Выделить позицию в таблице цветом"""
    if item == 'x':
        return '\033[1m\033[31mx\033[0m'
    elif item == 'o':
        return '\033[1m\033[32mo\033[0m'
    else:
        return item


def print_table(table: list):
    """Печать игрового поля"""
    for i in range(len(table)):
        print(mark_pos(table[i]) + ' ', end='')
        if (i + 1) % 3 == 0:
            print()


def minmax(table: list, player: str) -> int:
    """Алгоритм минимума и максимума"""
    if game_over(table) == 1:
        return -10
    elif game_over(table) == 2:
        return 10
    elif game_over(table) == 0:
        return 0

    if player == 'o':  # компьютер
        max_score = -100
        for pos in range(len(table)):
            if table[pos] != 'x' and table[pos] != 'o':
                temp_table = table.copy()
                temp_table[pos] = 'o'
                score = minmax(temp_table, 'x')
                if max_score < score:
                    max_score = score
            pos += 1
        return max_score

    if player == 'x':  # человек
        min_score = 100
        for pos in range(len(table)):
            if table[pos] != 'x' and table[pos] != 'o':
                temp_table = table.copy()
                temp_table[pos] = 'x'
                score = minmax(temp_table, 'o')
                if min_score > score:
                    min_score = score
            pos += 1
        return min_score


# Основной блок запуска игры
table = [str(i) for i in range(9)]
print_table(table)
step = 1
while game_over(table) < 0:
    player = 'x' if step % 2 == 1 else 'o'
    if player == 'x':  # ход человека
        pos = '-'
        while not check_step(pos, table):
            pos = input(f'\033[1m\033[34mХод {step}\033[0m. Выберите позицию для хода: ')
            if not check_step(pos, table):
                print('Неверная позиция. Повторите ввод.')
        table[int(pos)] = player
    else:  # ход компьютера
        best_score = -100
        best_pos = -1
        for pos in range(len(table)):
            if table[pos] != 'x' and table[pos] != 'o':
                temp_table = table.copy()
                temp_table[pos] = 'o'
                score = minmax(temp_table, 'x')
                if best_score < score:
                    best_score = score
                    best_pos = pos
            pos += 1
        print(f'\033[1m\033[34mХод {step}\033[0m. Компьютер сделал ход {best_pos}')
        table[best_pos] = player

    print_table(table)
    step += 1
end = game_over(table)
if end == 0:
    print('Ничья')
elif end == 1:
    print('Вы выиграли!')
else:
    print('Выиграл компьютер!')

