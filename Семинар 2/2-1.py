# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def sum_dig(number):
    sum_of_digits = 0
    while (number):
        sum_of_digits += number%10
        number = number//10
    return sum_of_digits
print(sum_dig(int(input("Введите число: "))))