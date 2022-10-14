#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

import math
n = [int(i) for i in range(1, int(input("Введите число: ")))]
print("Сумма", list(map(lambda x: float(round(math.pow((1 + 1/x),x),3)), n)), "=", sum(list(map(lambda x: float(round(math.pow((1 + 1/x),x),3)), n))))
