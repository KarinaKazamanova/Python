# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def client_input(a):
    while True:
        string = input(a)
        try:
            result = int(string)
            return result
        except:
            print("Введено не число")
            result = -1
while True:
    N = client_input("Введите положительное число: ")
    simple_multiplyers = []
    count = 0
    if N > 0:
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1
            if count == 2 and N % i == 0:
                simple_multiplyers.append(i)
            count = 0
        print(simple_multiplyers)
        break
    else:
        N = client_input("Введите положительное число: ")

