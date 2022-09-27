#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#Пример:

#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
import math
def fraction(a):
    return int(round(math.pow((1 + 1/a),a),0))
b = []
a = 0
for i in range(1,int(input ("Введите число: "))+1):
    b.append(fraction(i))
    a = a + b[i-1]
print(f"Для n = {i}:", b, "=>",a)