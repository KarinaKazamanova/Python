# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
x = open('file.txt','r')
position_1 = int(x.readline())
position_1 = int(x.readline(1))
n = int(input("Введите число: "))
massive = []
for i in range (-n,n+1):
    massive.append(i)
print (massive)
print (massive[position_1-1]*massive[position_1-1])