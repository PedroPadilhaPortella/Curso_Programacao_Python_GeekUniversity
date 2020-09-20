pares = 0
valoreslidos = 0
n = 0
while (n != 1000):
    n = int(input(f"Digite o valor {valoreslidos}: "))
    valoreslidos += 1
    if(n % 2 == 0):
        pares += 1

print("{}\nStats\nValores Lidos: {}\nValores Pares: {}".format('-'*20, valoreslidos, pares))