from random import choice
name_1 = input("Введите Ваше имя: ")
name_2 = input("Введите Ваше имя: ")
players_names = [name_1, name_2]
players = [0, 1]
sweets = int(input("Введите количество конфет: "))
max_sweets = int(input("Введите максимальное количеество конфет, которое можно взять за один ход: "))
player = choice(players)
while sweets // max_sweets:
    if player:
        step = int(input(f"{players_names[1]}, введите колчество конфет, которое хотите взять: "))
        while step:
             if 0 < step <= max_sweets:
                sweets = sweets - step
                player = players[0]
                prev_player_step += step
                step = 0
            elif step > max_sweets:
                step = int(input(f"Вы ввели слишком много конфет. Введите не более {max_sweets}: "))
            else:
                step = int(input(f"Так не годится. Нужно взять хотя бы одну конфету: "))
    else:
        step = int(input(f"{players_names[0]}, введите колчество конфет, которое хотите взять: "))
        while step:
            if step <= max_sweets:
                sweets = sweets - step
                player = players[1]
                step = 0
            else:
                step = int(input(f"Вы ввели слишком много конфет"))
if player:
    print(f"Победил, {players_names[1]}")
else:
    print(f"Победил, {players_names[0]}")
