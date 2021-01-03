def inverterNumero(num):
    return num[::-1]

numero = input("Numero:")
invertido = inverterNumero(numero)
print("Numero Invertido: {}".format(invertido))