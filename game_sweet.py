# Условие игры: На столе лежит 117 конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Добавьте игру против бота.

from random import randint as ri

total_sweet = 117
take_sweet = 0
player_sweet = 0
boot_sweet = 0
def start_game():
    print("На столе лежит 117 конфет. Играют два игрока делая ход друг после друга. \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход")
    who_is_first()
def who_is_first():
    random_number = ri(1, 2)
    if random_number == 1:
        player_turn()
    else:
        boot_turn()

def player_turn():
    global total_sweet
    global take_sweet
    global player_sweet
    print (f"Ваш ход сейчас на столе {total_sweet} конфет")
    take_sweet = int(input("Сколько конфет вы хотите взять?"))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
        take_sweet = int(input("Вы взяли слишком много конфет, можно взять только 28. Попробуйте снова: "))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        boot_turn()
    else:
        print("УРА!!! Вы победили!")

def boot_turn():
    global total_sweet
    global take_sweet
    global boot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1, 28)
    total_sweet <= take_sweet
    boot_sweet += take_sweet
    print(f"Бот взял {take_sweet} конфет. На столе осталось {total_sweet} конфет.")
    if total_sweet > 0:
        player_turn()
    else:
        print("Бот победил!")
