# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint
def Init():
    a = []
    for i in range(randint(1,10)):
        a.append(randint(1, 10))
    return a

def Uniq(a):
    uniq_values = [] 
    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j] == a[i]:
                count += 1
        if count == 1:
            uniq_values.append(a[i])
        count = 0
    return uniq_values 
a = Init()
result = Uniq(a)
print(f'Первоначальный массив: {a} ')
print()
print(f'Массив с уникальными значениям: {result} ')