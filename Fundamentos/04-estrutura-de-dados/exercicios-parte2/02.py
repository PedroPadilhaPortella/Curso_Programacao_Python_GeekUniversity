from random import randint


matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for l in range(0, 5):
    for c in  range(0, 5):
        if(l == c):
            matriz[l][c] = 1
        else:
            matriz[l][c] = 0


for l in range(0, len(matriz)):
    for c in  range(0, len(matriz)):
        print(f"[{matriz[l][c]: ^5}]", end=" ")
    print()
