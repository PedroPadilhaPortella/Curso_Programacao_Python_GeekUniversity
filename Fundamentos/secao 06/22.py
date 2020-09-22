valor = 10
soma = 0
quant = 0
while(valor >= 10 and valor <= 20):
    valor = float(input("Valor entre 10 e 20: "))
    soma += valor
    quant += 1
media = soma / quant
print("Média das Notas: {:.2f}".format(media))