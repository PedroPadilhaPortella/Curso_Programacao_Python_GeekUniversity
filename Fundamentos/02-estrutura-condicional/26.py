def consumo(d, litros):
    consumo = d / litros
    print("Consumo: {} litro/km".format(consumo))
    if(consumo <= 8 ):
        print("Venda o Carro")
    elif(consumo > 8 and consumo >=14):
        print("Economico")
    else:
        print("Muito Economico!")


dist = float(input("Distancia do Percurso: "))
litros = float(input("Quantos Litros gastos: "))
consumo(dist, litros)