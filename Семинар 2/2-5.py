# Реализуйте алгоритм перемешивания списка. Без функции suffle из модуля random.

import random
my_massiv = []
for i in range (int(input("Введите длину массива: "))):
    my_massiv.append(i*3)
print(my_massiv)
for i in range (len(my_massiv)-1):
    j = random.randint(i, (len(my_massiv)-1)) 
    my_massiv [i], my_massiv[j] = my_massiv[j], my_massiv [i]
print(my_massiv)

# прочитала в учебнике "Алгоритмы. Теория и практическое применение"