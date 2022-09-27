# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def client_input(a):
    result = -1
    while (result):
        try:
            result = int (input(a))
        except:
            
            result = -1
        finally:
            return result

a = client_input("Введите число от 1 до 4: ")
while (a):
    if (a in range (1,5)):
        b = ['(0 - +inf;0 - +inf)', '(0 - +inf;0 - -inf)','(0 - -inf;0 - -inf)', '(0 - -inf;0 - +inf)']
        print (f"Для введенной честверти х и у принимают значения: {b[a-1]}")
        a = 0
    else:
        print("Немного промахнулись. Ну ничего, всегда можно попробовать еще раз, для этого вся жизнь впереди :)")
        a = client_input("Введите число от 1 до 4: ")