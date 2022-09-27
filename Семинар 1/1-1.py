# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

def client_input(a):
    result = -1
    while (result):
        try:
            result = int (input(a))
        except:
            
            result = -1
        finally:
            return result

a = client_input("Введите число от 1 до 7: ")
while (a):
    if (a in(6,7)):
        print("Да")
        break
    elif (a in range (1,6)):
        print ("Нет")
        break
    else:
        print("Немного промахнулись. Ну ничего, всегда можно попробовать еще раз, для этого вся жизнь впереди :)")
        a = client_input("Введите число от 1 до 7: ")
