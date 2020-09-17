quant = 10
soma = 0
while(quant > 0):
    soma += int(input(f"Valor {quant}: "))
    quant -= 1
print("A soma dos valores foi = {}".format(soma))