from math import log10


def logaritmo(n):
    return log10(n)


numero = int(input("Numero: "))
if(numero <= 0):
    print("Numero Inválido")
else:
    log = logaritmo(numero)
    print("Logaritmo de {} é {}".format(numero, log))