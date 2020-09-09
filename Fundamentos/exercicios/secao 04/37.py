def desconto(preco):
    return preco - preco * 0.12

preco = float(input("Qual foi o total a pagar? R$ "))
print("O total com desconto de 12% foi {}".format(desconto(preco)))