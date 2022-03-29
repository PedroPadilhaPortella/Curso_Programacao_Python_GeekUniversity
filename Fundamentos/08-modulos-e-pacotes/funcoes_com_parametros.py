if __name__ == 'main':
    print("Metodo Main")

def somar_impares(lista):
    soma = 0
    for i in lista:
        if i % 2 != 0:
            soma += i
    return soma

def somar_pares(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma