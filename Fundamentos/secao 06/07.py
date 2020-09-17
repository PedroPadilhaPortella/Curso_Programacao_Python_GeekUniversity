quant = 10
soma = 0
numeros = quant
while(quant > 0):
    num = int(input(f"Numero {quant}: "))
    soma += num
    quant -= 1
media = soma / numeros

print("A media dos numeros foi = {:.2f}".format(media))


