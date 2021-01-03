from random import randint


matriz1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
matriz3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


for l in range(0, 5):
    for c in  range(0, 5):
            matriz1[l][c] = randint(1, 100)
            matriz2[l][c] = randint(1, 100)



for l in range(0, len(matriz1)):
    for c in  range(0, len(matriz1)):
        if(matriz1[l][c] > matriz2[l][c]):
            matriz3[l][c] = matriz1[l][c]
        else:
            matriz3[l][c] = matriz2[l][c]


print("---- MATRIZ 1 -----")
for l in range(0, len(matriz1)):
    for c in  range(0, len(matriz1)):
        print(f"[{matriz1[l][c]: ^5}]", end=" ")
    print()

print("---- MATRIZ 2 -----")
for l in range(0, len(matriz2)):
    for c in  range(0, len(matriz2)):
        print(f"[{matriz2[l][c]: ^5}]", end=" ")
    print()

print("---- MATRIZ 3 -----")
for l in range(0, len(matriz3)):
    for c in  range(0, len(matriz3)):
        print(f"[{matriz3[l][c]: ^5}]", end=" ")
    print()