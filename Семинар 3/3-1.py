# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint
a = []
for i in range(randint(1,10)):
    a.append(randint(1, 100))
def Result(a):
    sum = 0
    for i in range(1, len(a), 2):
        sum += a[i]
    return sum
t_sum = Result(a)
print(a)
print(t_sum)
