# Напишите программу, которая будет преобразовывать десятичное число в двоичное
def client_input(a):
    while True:
        string = input(a)
        try:
            result = int(string)
            return result
        except:
            print("Введено не число")
            result = -1
    

a = client_input("Введите число: ")
binar = bin(a)[2::] 
print(binar)