# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
a = [float(i) for i in input().split()]
b = [round(val % 1, 10) for val in a if val % 1 != 0 and isinstance]
print(max(b) - min(b))