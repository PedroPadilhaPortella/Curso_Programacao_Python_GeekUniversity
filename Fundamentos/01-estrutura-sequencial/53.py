def calcularArea(c, l):
    return c * l

def calcularPrecoTerreno(c, l, p):
    area = calcularArea(c, l)
    return area * p

comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))
valor = float(input("Valor do metro quadrado: "))

total = calcularPrecoTerreno(comprimento, largura, valor)
print("Total R$ {:.2f}".format(total))