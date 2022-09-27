# Реализуйте алгоритм перемешивания списка. Без функции suffle из модуля random.

import random
my_massiv = []
for i in range (int(input("Введите длину массива: "))):
    my_massiv.append(i)
print(my_massiv)
for i in range (len(my_massiv)-1):
    j = random.randint(i, (len(my_massiv)-1))
    temp = 0
    temp = my_massiv [i] 
    my_massiv [i] = my_massiv[j]
    my_massiv[j] = temp
print(my_massiv)

# прочитала в учебнике "Алгоритмы. Теория и практическое применение"