def comissao(venda):
    comissao = 0
    if(venda < 20000.00):
        comissao = 400 + venda * 0.14
    elif(venda < 40000.00 and venda >= 20000.00):
        comissao = 500 + venda * 0.14
    elif(venda < 60000.00 and venda >= 40000.00):
        comissao = 550 + venda * 0.14
    elif(venda < 80000.00 and venda >= 60000.00):
        comissao = 600 + venda * 0.14
    elif(venda < 100000.00 and venda >= 80000.00):
        comissao = 650 + venda * 0.14
    elif(venda < 100000.00):
        comissao = 700 + venda * 0.16
    return comissao



venda = float(input("Total da Venda: R$"))
total = comissao(venda)
print("A comissão do funcionário será de R${:.2f}".format(total))