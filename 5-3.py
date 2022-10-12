from random import choice
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
    d[3][1] == d[2][2] == d[3][3]) and
    d[2][2] != 0):
        return False
    elif ((d[1][3] == d[2][3] == d[3][3] or
    d[3][1] == d[3][2] == d[3][3]) and
    d[3][3] != 0):
        return False
    else:
        return True
def step (d, player, x, y, players):
    if player == 1:
        d[x][y] = 'X'
    elif player == 0:
        d[x][y] = 'O'  
    return d
players = [0, 1]
player = choice(players)
win_flag = True
while win_flag:
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    while True:
        if Field[x][y] == 0: 
            if player == 1:
                Field = step(Field, player, x, y, players)
                player = players[0]
            else:
                Field = step(Field, player, x, y, players)
                player = players[1]
        else:
            print("Данный ход уже был сделан.")
            x = int(input("Введите другую координату x: "))
            y = int(input("Введите другую координату y: "))
        win_flag = win(Field)
        print_field(Field)
print(win_flag)