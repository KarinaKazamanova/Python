# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def sum_dig(number):
    sum_of_digits = 0
    while number % 1 != 0:
        number = number * 10
    while (number):
        sum_of_digits += number%10
        number = number//10
    return sum_of_digits

a = abs(float((input("Введите число: "))))
b = int(sum_dig(a))
print(b)