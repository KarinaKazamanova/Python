# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
def client_input(a):
    result = -1
    while (result):
        try:
            result = float (input(a))
        except:
            
            result = -1
        finally:
            return result

a = [float(i) for i in input("Введите координаты точки Х через пробел: ").split()]
b = [float(i) for i in input("Введите координаты точки Y через пробел: ").split()]
while (a and b):
    if (len(a) == len (b) == 2):
        distance = math.sqrt((math.pow((b[0] - a[0]),2) + math.pow((b[1] - a[1]),2)))//1 + math.sqrt((math.pow((b[0] - a[0]),2) + math.pow((b[1] - a[1]),2)))*100%100//1/100
        print(f"Расстояние между Х и У = {distance}")
        a = 0
        b = 0
    else:
        print ("Введите две координаты")
        a = [float(i) for i in input("Введите координаты точки Х через пробел: ").split()]
        b = [float(i) for i in input("Введите координаты точки Y через пробел: ").split()]      
       
