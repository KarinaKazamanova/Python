# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
 
a = [int(i) for i in input().split()]
result = [int(i) for i in a if a.count(i) == 1]
print(f'Первоначальный массив: {a} ')
print()
print(f'Массив с уникальными значениям: {result} ')