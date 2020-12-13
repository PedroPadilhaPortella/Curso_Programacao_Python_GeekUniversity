from random import randint


matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
find = 0
posicao = []


busca = int(input("Busque por um valor de 0 a 20: "))
for l in range(0, 5):
    for c in  range(0, 5):
            matriz[l][c] = randint(1, 20)


for l in range(0, len(matriz)):
    for c in  range(0, len(matriz)):
        print(f"[{matriz[l][c]: ^5}]", end=" ")
    print()


for l in range(0, len(matriz)):
    for c in  range(0, len(matriz)):
        if(busca == matriz[l][c]):
            posicao = [l, c]
            print(f"Valor {busca} encontrado na posicao {posicao}")
            find += 1

if(find == 0):
    print(f"Valor {busca} não encontrado!")