def custos():
    fabricacao = float(input("Custo de Fábricação: "))
    custo = 0
    if(fabricacao < 12000):
        custo = fabricacao + fabricacao * 0.05 + fabricacao * 0
    elif(fabricacao <= 25000 and fabricacao >= 12000):
        custo = fabricacao + fabricacao * 0.1 + fabricacao * 0.15
    elif(fabricacao > 25000):
        custo = fabricacao + fabricacao * 0.15 + fabricacao * 0.2
    print("Custo ao Cliente: R${:.2f}".format(custo))

custos()