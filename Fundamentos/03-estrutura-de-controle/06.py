quant = 10
soma = 0
while(quant > 0):
    soma += int(input(f"Nota {11 - quant}: "))
    quant -= 1
media = soma / 10
print("A media das notas foi = {:.2f}".format(media))