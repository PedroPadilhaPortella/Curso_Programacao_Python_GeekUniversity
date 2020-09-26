from math import pow


def calcular():
    resultado = []
    for i in range(1000, 10000):
        n = str(i)
        value = pow(int(n[0:2]) + int(n[2:]), 2)
        if(value == i):
            resultado.append(i)
    return resultado


resultado = calcular()
print(resultado)