from random import choice
import os
Field = {
    'X': {1: 1, 2: 2, 3: 3},
    1: {1: 0, 2: 0, 3: 0},
    2: {1: 0, 2: 0, 3: 0},
    3: {1: 0, 2: 0, 3: 0}}
def print_field(d):
    for k, v in d.items():
        print(k, end=' | ')
        for k_1, v_1 in d[k].items():
            if d[k][k_1] == 0: 
                print(" ", end= " | ")
                
            else:
                print(d[k][k_1], end= " | ")
        print()
        print("----------------")
def win(d):
    if ((d[1][1] == d[1][2] == d[1][3] or
    d[1][1] == d[2][1] == d[3][1] or
    d[1][1] == d[2][2] == d[3][3]) and
    d[1][1] != 0):
        return False
    elif ((d[1][2] == d[2][2] == d[3][2] or
    d[2][1] == d[2][2] == d[2][3] or
    d[3][1] == d[2][2] == d[1][3]) and
    d[2][2] != 0):
        return False
    elif ((d[1][3] == d[2][3] == d[3][3] or
    d[3][1] == d[3][2] == d[3][3]) and
    d[3][3] != 0):
        return False
    # Пыталась добавить ничью простым способом, но пока не выходит
    # elif ((not (0 in d[1])) and (not (0 in d[2]))and (not (0 in d[3]))):
        # return False
    else:
        return True
def step (d, player, x, y):
    if player == 1:
        d[x][y] = 'X'
    elif player == 0:
        d[x][y] = 'O'  
    return d
def turn(player):
    if player == 1:
        player = 0
        return player
    else:
        player = 1
        return player
def clear():
    
name_1 = input("Введите Ваше имя: ")
name_2 = input("Введите Ваше имя: ")
count = 0
names = [name_1, name_2]
players = [0, 1]
player = choice(players)
win_flag = True
print_field(Field)
while win_flag:
    clear = lambda: os.system('cls') # Хотела ввести очистку консоли, пока не потестила
    clear()
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    step_control = 1
    while step_control:
        if Field[x][y] == 0: 
            Field = step(Field, player, x, y)
            player = turn(player)
            step_control = 0
        
        else:
            print("Данный ход уже был сделан.")
            x = int(input("Введите другую координату x: "))
            y = int(input("Введите другую координату y: "))
        win_flag = win(Field)
        print_field(Field)
        count += 1
if count < 9:
    if player:
        print(f"Победил {names[1]} !")
    else:
        print(f"Победил {names[0]} !")
else:
    print("Ничья !")
