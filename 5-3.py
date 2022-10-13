from random import choice
import os
Field = {
    'X': {1: 1, 2: 2, 3: 3},
    1: {1: 0, 2: 0, 3: 0},
    2: {1: 0, 2: 0, 3: 0},
    3: {1: 0, 2: 0, 3: 0}}

def client_input(a):
    result = -1
    while (result):
        try:
            result = int(input(a))
        except:
            
            result = -1
        finally:
            return result  
  
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
    # Пыталась добавить ничью простым способом, но пока вышло так
    elif d[1][1] != 0 and d[1][2] != 0 and d[1][3] != 0 and d[2][1] != 0 and d[2][2] != 0 and d[2][3] != 0 and d[3][1] != 0 and d[3][2] != 0 and d[3][3] != 0:
        return False
    else:
        return True
        
def step (d, player, x, y):
    clear()
    if x in range(1,4) and y in range(1,4):
        if Field[x][y] == 0:
            if player:
                d[x][y] = 'X'
                player = 0
                return (d, player)
            else:
                d[x][y] = 'O'
                player = 1
                return (d, player)
        else:
            print("Данный ход уже был сделан.")
            x = client_input("Введите другую координату x: ")
            y = client_input("Введите другую координату y: ")
            return step(d, player, x, y)
    else:
        print("Введенные координаты выходят за рамки игрового поля.")
        x = client_input("Введите другую координату x: ")
        y = client_input("Введите другую координату y: ")
        return step(d, player, x, y)

def clear():
    os.system('cls')
    
name_1 = input("Введите Ваше имя: ")
name_2 = input("Введите Ваше имя: ")
count = 0
names = [name_1, name_2]
players = [0, 1]
player = choice(players)
win_flag = True
print_field(Field)
while win_flag:
    x = client_input(f"{names[player]}, введите координату x: ")
    y = client_input(f"{names[player]}, введите координату y: ")
    Field, player = step(Field, player, x, y)
    win_flag = win(Field)
    print_field(Field)
    count += 1

if count < 9:
    if player:
        print(f"Победил {names[0]}!")
    else:
        print(f"Победил {names[1]}!")
else:
    print("Ничья!")
