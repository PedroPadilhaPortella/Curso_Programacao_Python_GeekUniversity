def resultados(total, metodo):
    desconto = total * 0.9
    parcelas = desconto / 3
    comissao = 0
    if(metodo.lower() == "a vista"):
        comissao = desconto * 0.05
    elif(metodo.lower() == "parcelado"):
        comissao = total * 0.05
    else:
        print("Forma de pagamento Inválida!!")
        exit()
    return [desconto, parcelas, comissao]


total = float(input("Valor total da Compra: R$ "))
metodo = input("A vista ou Parcelado? ")
[desconto, parcelas, comissao] = resultados(total, metodo)
print("total com desconto: R$ {:.2f}".format(desconto))
print("3 x de R$ {:.2f}".format(parcelas))
print("Comissão do vendedor: R$ {:.2f}".format(comissao))