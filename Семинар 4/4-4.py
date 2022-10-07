# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint
def client_input(a):
    while True:
        string = input(a)
        try:
            result = int(string)
            return result
        except:
            print("Введено не число")
            result = -1
k = client_input("Введите степень многочлена: ")
f = open('polynominal.txt', 'w')
for i in range(k, -1, -1):
    if 0 < i < k:
        koeff = randint(0, 100)/randint(0, 100)
        if koeff != 0:
            f.write(f' + {koeff} * x^{i}')  
    elif i == 0:
        koeff = randint(1, 100)/randint(0, 100)
        if koeff != 0:
            f.write(f' + {koeff} = 0')
    else: 
        koeff = randint(1, 100)/randint(0, 100)
        if koeff != 0:
            f.write(f'{koeff} * x^{i}')
f.close()