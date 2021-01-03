from random import randint

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
soma = 0

for l in range(0, 4):
    for c in range(0, 4):
            matriz[l][c] = randint(1, 20)


for l in range(0, len(matriz)):
    for c in  range(0, len(matriz[l])):
        print(f"[{matriz[l][c]: ^5}]", end=" ")
    print()

print("\n---Matriz Triangular Inferior---\n")

for l in range(0, len(matriz)):
    for c in  range(0, len(matriz[l])):
        if(c > l):
            matriz[l][c] = 0
        print(f"[{matriz[c][l]: ^5}]", end=" ")
    print()