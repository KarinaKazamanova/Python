#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def client_input(a):
    result = -1
    while (result):
        try:
            result = int (input(a))
        except:
            
            result = -1
        finally:
            return result

def product(a):
    c = 1
    if (a==1):
        return c*a
    else:
        return product(a-1)*a

b = []
for i in range(1,client_input("Input your number: ")+1):
    b.append(product(i))
print(b)