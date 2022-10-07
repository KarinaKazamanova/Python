import math
a = int(input("Ввеидте коэффициент при Х^2: "))
b = int(input("Ввеидте коэффициент при Х: "))
c = int(input("Ввеидте свободный член многочлена: "))

d = math.pow(b, 2) - 4 * a * c
if a != 0:
    if d < 0:
        print("Корней нет")
    elif d == 0:
        x = -b/(2*a)
        print(f"X = {x}")
    else:
        x_1 = (-b + math.sqrt(d))/(2*a)
        x_2 = (-b - math.sqrt(d))/(2*a)
        print(f"X1 = {x_1}, X2 = {x_2}")
else:
    x = -c / b
    print(f"X = {x}")