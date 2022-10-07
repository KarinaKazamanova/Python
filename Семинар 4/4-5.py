# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов




f_1 = open('polynominal_1.txt','r')
f_2 = open('polynominal_2.txt','r')
x_1 = str(f_1.readline())
x_2 = str(f_2.readline())

def Power(x):
    pow = []
    for i in range(1, len(x)):
        if x[i - 1] == '^':
            pow.append(int(x[i]))
    return pow

def Koefficient(x, p):
    koeff = str(x).replace(' = 0', '')
    for i in range(p[0], 0, -1):
        koeff = koeff.replace(f' * x^{i} + ', ' ')
    koeff = [float(i) for i in koeff.split()]
    return koeff 


pow_1 = Power(x_1)
pow_2 = Power(x_2)
koeff_1 = Koefficient(x_1, pow_1)
koeff_2 = Koefficient(x_2, pow_2)

pow_1.insert(len(pow_1), 0)
pow_2.insert(len(pow_2), 0)

polynominal_1 = {}
for i in range(0, len(pow_1)):
        polynominal_1[pow_1[i]] = koeff_1[i]
polynominal_2 = {}
for i in range(0, len(pow_2)):
    polynominal_2[pow_2[i]] = koeff_2[i]

polynominal_sum = {}
if  pow_1[0] > pow_2[0]:
    for i in range(pow_1[0], -1, -1):
        if i in pow_1 and i not in pow_2:
            polynominal_sum[i] = polynominal_1[i]
        elif i not in pow_1 and i in pow_2:
            polynominal_sum[i] = polynominal_2[i]
        elif i in pow_1 and i in pow_2:
            polynominal_sum[i] = polynominal_1[i] + polynominal_2[i]
        else:
            continue
final = open('polynominal_sum.txt','w')
for k, v in polynominal_sum.items():
    if k != 0:
        final.write(f'{v} * x^{k} + ')
    else:
        final.write(f'{v} = 0')
f_1.close()
f_2.close()
final.close()
