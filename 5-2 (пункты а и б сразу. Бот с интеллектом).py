from random import choice, randint
name = input("Введите Ваше имя: ")
players = [0, 1] # 0 - бот, 1 - игрок
sweets = int(input("Введите количество конфет: "))
max_sweets = int(input("Введите максимальное количеество конфет, которое можно взять за один ход: "))
player = choice(players)
prev_player_step = 0
count_steps = 0 # Для отделения первого для бота хода от всех его ходов
while sweets // max_sweets:
    if player:
        step = int(input(f"{name}, введите колчество конфет, которое хотите взять: "))
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
        if count_steps == 0 and prev_player_step != sweets % (max_sweets + 1): # Если не начинает Бот и человек не знает, как правильно играть, и не угадал правильное количество конфет, с которого нужно начинать, то во время первого хода Бота после первого хода человека (для игры это уже второй ход из общего числа ходов Игроков), Бот должен выровнять количество оставшихся конфет, так, чтобы после него остаток нацело делился на максимальное количество конфет за 1 ход + 1 (как будто первого шага человека не было, а игра началась с Бота и с изначального количества конфет = изначальное количество конфет - то, что уже было взято человеком)  
            step = (sweets - prev_player_step) % (max_sweets + 1)
            print(f"Я взял {step} конфет. Теперь твоя очередь")
            sweets = sweets - step
            player = players[1]
            step = 0
            prev_player_step = 0
            count_steps += 1
        elif count_steps != 0:                                                                          # Тут Бот уже проигрывает, если человек в курсе стратегии. Если же человек просто угадал верный первый шаг, а адльше будет действовать не по выигрышной стратегии, то, возможно, можно выровнять количество оставшихся конфет для успеха Бота, но уже сложнее и может потребоваться несколько шагов, что не гарантирует успех Боту, если игра изначально имеет такие условия, при которых она завершится за очень маленькое количество шагов.
            step = (max_sweets + 1) - prev_player_step
            print(f"Я взял {step} конфет. Теперь твоя очередь")
            sweets = sweets - step
            player = players[1]
            step = 0
            prev_player_step = 0
            count_steps += 1
        else:
            step = randint(1, max_sweets)
            print(f"Я взял {step} конфет. Теперь твоя очередь")
            sweets = sweets - step
            player = players[1]
            step = 0
            prev_player_step = 0
            count_steps += 1
if player:
    print(f"Победил, {name}")
else:
    print(f"Победил, Бот")
