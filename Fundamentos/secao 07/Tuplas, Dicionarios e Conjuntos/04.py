from random import randint


matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior = 0
posicaomaior = []


for l in range(0, 4):
    for c in  range(0, 4):
            matriz[l][c] = randint(1, 99)


for l in range(0, len(matriz)):
    for c in  range(0, len(matriz)):
        print(f"[{matriz[l][c]: ^5}]", end=" ")
        if(matriz[l][c] > maior):
            maior = matriz[l][c]
            posicaomaior = [l, c]
    print()

print(f"\nO maior valor encontrado foi {maior} na posição {posicaomaior}")