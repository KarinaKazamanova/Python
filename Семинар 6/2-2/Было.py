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

def product(number):
    c = 1
    if (number==1):
        return c*number
    else:
        return product(number-1)*number

massive_of_products = []
for i in range(1,client_input("Input your number: ")+1):
    massive_of_products.append(product(i))
print(massive_of_products)