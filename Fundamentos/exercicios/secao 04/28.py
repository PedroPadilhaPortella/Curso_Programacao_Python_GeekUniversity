import math


def somaDosQuadrados(n1, n2, n3):
    return math.pow(n1, 2) + math.pow(n2, 2) + math.pow(n3, 2)

valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
valor3 = int(input('Valor 3: '))
resultado = somaDosQuadrados(valor1, valor2, valor3)
print(f"A soma do quadrado dos valores foi {resultado}")