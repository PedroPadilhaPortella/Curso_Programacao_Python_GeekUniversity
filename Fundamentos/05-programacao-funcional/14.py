def calcular_economia_carro(km, litro):
    kmL = km / litro
    if(kmL < 8):
        return "Venda o Carro!"
    elif(kmL > 8 and kmL <= 14):
        return "Economico"
    elif(kmL > 14):
        return "Super Economico"


km = int(input("Qual a distancia percorrida? "))
litro = int(input("Quantos litros foram gastos? "))
message = calcular_economia_carro(km, litro)
print(message)