cidade = input("Nome da Cidade: ")
habitantes = int(input("Total de Habitantes: "))
kwh = float(input("Valor do Kw/h: R$ "))

maior = 0
menor = 100
total = 0
tipo1 = 0
tipo2 = 0
tipo3 = 0
total1 = 0
total2 = 0
total3 = 0
unknown = 0
totalunknown = 0

for hab in range(1, habitantes + 1):
    consumo = float(input(f"\nConsumo Mensal do habitante #{hab}: "))
    tipo = int(input("Código do Consumidor\n1-Residencial\n2-Comercial\n3-Industrial\n:_"))
    total += consumo

    if(consumo > maior):
        maior = consumo
    if(consumo < menor):
        menor = consumo

    if(tipo == 1):
        tipo1 += 1
        total1 += consumo
    elif(tipo == 2):
        tipo2 += 1
        total2 += consumo
    elif(tipo == 3):
        tipo3 += 1
        total3 += consumo
    else:
        unknown += 1
        totalunknown += consumo

print(cidade)
print(f"Maior: {maior}\nMenor: {menor}")
print("Média dos Habitantes: {}".format(total / habitantes))

try:
    media1 = total1/tipo1
except:
    media1 = 0
try:
    media2 = total2/tipo2
except:
    media2 = 0
try:
    media3 = total3/tipo3
except:
    media3 = 0
try:
    media4 = totalunknown / unknown
except:
    media4 = 0

print(f"Total de Consumo:\n1-Residencial: {media1}\n2-Comercial {media2}\n3-Industrial: {media3}\n4-Outros: {media4}")