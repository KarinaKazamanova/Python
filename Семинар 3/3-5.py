# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def client_input(a):
    while True:
        string = input(a)
        try:
            result = int(string)
            return result
        except:
            print("Введено не число")
            result = -1
    
def Fibonachi(a):
    a_1 = []
    for k in range(0, a + 1):
        if k == 0 or k == 1:
            a_1.append(1)
        else:
            a_1.append(Fibonachi(k-2)[len(Negafibonachi(k-2))-1] + Fibonachi(k-1)[len(Negafibonachi(k-1))-1])
    return a_1
def Negafibonachi(a):
    a_2 = []
    for k in range(0, a + 1):
        if k == 0:
            a_2.append(0)
        elif k == 1:
            a_2.append(1)
        else:
            a_2.append(Negafibonachi(k-2)[len(Negafibonachi(k-2))-1] - Negafibonachi(k-1)[len(Negafibonachi(k-1))-1])
    return a_2
a = client_input("Введите число: ")
total_result = Negafibonachi(a)[::-1] + Fibonachi(a)
print(total_result[:len(total_result)-1:])

