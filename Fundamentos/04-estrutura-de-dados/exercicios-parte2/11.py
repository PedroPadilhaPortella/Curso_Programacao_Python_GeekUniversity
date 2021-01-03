from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

for l in range(0, 3):
    for c in range(0, 3):
            matriz[l][c] = randint(1, 5)


for l in range(0, len(matriz)):
    for c in  range(0, len(matriz[l])):
        print(f"[{matriz[l][c]: ^5}]", end=" ")
        if(c == (3 - 1 - l)):
            soma += matriz[l][c]
    print()

print("A soma da diagonal secundária é {}".format(soma))