vetor = []
for i in range(0, 7): 
    n = int(input("Numero: "))
    vetor.append(n)

x = int(input("Posicao de 0 a 7: "))
y = int(input("Posicao de 0 a 7: "))
soma = vetor[x] + vetor[y]
print(soma)