dados = list()

for i in range(0, 10):
    dados.append(int(input("Adicione o valor {}: ".format(i))))
    dados.sort()

print(dados)