def imposto(preco, estado):
    if(estado.upper() == "MG"):
        return preco * 1.07
    elif(estado.upper() == "SP"):
        return preco * 1.12
    elif(estado.upper() == "RJ"):
        return preco * 1.15
    elif(estado.upper() == "MS"):
        return preco * 1.08
    else:
        print("Erro, dados Inválidos ou Estado Inválido")
        exit()


preco = float(input("Preço: "))
estado = str(input("Estado: "))

preco = imposto(preco, estado)
print("Total = R${:.2f}".format(preco))