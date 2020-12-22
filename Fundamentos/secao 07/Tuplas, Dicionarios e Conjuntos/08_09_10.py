from random import randint


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = [0, 0, 0]

for l in range(0, 3):
    for c in range(0, 3):
            matriz[l][c] = randint(1, 10)


for l in range(0, len(matriz)):
    for c in  range(0, len(matriz[l])):
        if(l < c):
            soma[0] += matriz[l][c]
        elif(l == c):
            soma[1] += matriz[l][c]
        else:
            soma[2] += matriz[l][c]
        print(f"[{matriz[l][c]: ^5}]", end=" ")
    print()
        
print(f"ACIMA: {soma[0]}")
print(f"DIAGONAL: {soma[1]}")
print(f"ABAIXO: {soma[2]}")