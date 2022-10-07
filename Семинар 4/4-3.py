# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint
def Init():
    a = []
    for i in range(randint(1,100)):
        a.append(round(randint(1, 10) / randint(1, 10), 3))
    return a

def Uniq(a):
    uniq_values = [] 
    for i in a:
        if i not in uniq_values:
           uniq_values.append(i)
    return uniq_values 
a = Init()
result = Uniq(a)
print(f'Первоначальный массив: {a} ')
print()
print(f'Массив с уникальными значениям: {result} ')