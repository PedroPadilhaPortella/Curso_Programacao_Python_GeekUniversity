import math


def calcular(n):
    if(n >= 0):
        print("Raiz de {}: {}".format(n, math.sqrt(n)))
    else:
        print("{} ao quadrado: {}".format(n, math.pow(n, 2)))

numero = float(input('Numero: '))
calcular(numero)