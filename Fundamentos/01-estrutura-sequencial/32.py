def calcular(value):
    return (value * 3 + 1) + (value * 2 - 1)

valor = int(input("Numero: "))
result = calcular(valor)
print("A soma do sucessor do triplo com o antecessor do dobro é {}".format(result))