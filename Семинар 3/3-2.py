# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
from math import ceil
def Init():
    a = []
    for i in range(randint(1,10)):
        a.append(randint(1, 100))
    return a
def Product(a):
    b = []
    for i in range(0, ceil(len(a) / 2)):
        b.append(a[i] * a[len(a) - i -1])
    return b
a = Init()
t_product = Product(a)
print(a)
print(t_product)
