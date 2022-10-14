from math import factorial as f
def client_input(a):
    result = -1
    while (result):
        try:
            result = int (input(a))
        except:
            
            result = -1
        finally:
            return result
a = [int(i) for i in range(1, client_input("Число! ") + 1)]
print(list(map(lambda x: f(x), a)))