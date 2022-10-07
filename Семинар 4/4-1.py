# Вычислить число c заданной точностью d
from math import log10
def client_input(a):
    while True:
        string = input(a)
        try:
            result = float(string)
            return result
        except:
            print("Введено не число")
            result = -1
while True:
    d = client_input("Введите точность (10^{-1} ≤ d ≤10^{-10}): ")
    if  float(d) * (10 ** (len(str(d)) - 2)) == 1:
        n = client_input("Введите число, которое надо рассчитать: ")
        print(round(n, int(-log10(d))))
        d = -1
    else:
        print("Некорректно введена точность")
        d = client_input("Введите точность (10^{-1} ≤ d ≤10^{-10}): ")